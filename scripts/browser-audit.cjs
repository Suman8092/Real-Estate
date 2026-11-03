const { chromium } = require('@playwright/test');
const fs = require('node:fs');
const assert = require('node:assert/strict');
const path = require('node:path');

(async () => {
  const base = process.env.AUDIT_URL || 'http://127.0.0.1:4201/';
  const launch = { headless: true };
  if (process.env.BROWSER_EXECUTABLE) launch.executablePath = process.env.BROWSER_EXECUTABLE;
  else if (process.platform === 'win32') launch.channel = 'msedge';
  const browser = await chromium.launch(launch);
  const pages = fs.readdirSync('.').filter(file => file.endsWith('.html'));
  const categories = ['residential.html', 'commercial.html', 'farmhouses.html', 'vacant-plots.html', 'industrial.html'];
  const report = { base, mapEmbed: 'Google Maps iframe mocked for deterministic layout tests; external service not certified.', viewports: [] };
  fs.mkdirSync('artifacts', { recursive: true });
  try {
    for (const width of [1440, 1280, 768, 390]) {
      const context = await browser.newContext({ viewport: { width, height: 1000 }, reducedMotion: 'reduce' });
      await context.route('**/www.google.com/maps**', route => route.fulfill({ contentType: 'text/html', body: '' }));
      const page = await context.newPage();
      const result = { width, pages: [], errors: [], failed: [] };
      page.on('pageerror', error => result.errors.push(error.message));
      page.on('console', msg => { if (msg.type() === 'error') result.errors.push(msg.text()); });
      page.on('response', response => { if (response.status() >= 400) result.failed.push({ url: response.url(), status: response.status() }); });
      page.on('requestfailed', request => { if (request.failure()?.errorText !== 'net::ERR_ABORTED') result.failed.push({ url: request.url(), error: request.failure()?.errorText }); });
      for (const file of pages) {
        await page.goto(new URL(file, base).href, { waitUntil: 'networkidle' });
        await page.evaluate(() => document.fonts.ready);
        for (const img of await page.locator('img').all()) {
          if (!(await img.isVisible())) continue;
          await img.scrollIntoViewIfNeeded();
          await img.evaluate(async image => { if (!image.complete) await new Promise(resolve => { image.onload = resolve; image.onerror = resolve; }); });
          assert(await img.evaluate(image => image.naturalWidth > 0), `${width}/${file}: broken image`);
        }
        assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${width}/${file}: overflow`);
        const header = await page.locator('body > header').evaluate(element => ({ height: element.clientHeight, bg: getComputedStyle(element).backgroundColor }));
        assert.equal(header.height, width < 640 ? 68 : 84, `${width}/${file}: header geometry`);
        assert.equal(header.bg, 'rgb(255, 255, 255)', `${file}: pure white header`);
        assert.equal(await page.locator('body > footer').evaluate(element => getComputedStyle(element).backgroundColor), 'rgb(255, 255, 255)', `${file}: pure white footer`);
        if (file !== 'index.html') {
          const sections = await page.locator('main .brand-section').evaluateAll(elements => elements.map(element => getComputedStyle(element).backgroundColor));
          assert.equal(sections.length, 2, `${file}: two existing content groups`);
          sections.forEach((color, index) => assert.equal(color, index % 2 ? 'rgb(0, 0, 0)' : 'rgb(255, 255, 255)', `${file}: alternating body sections`));
        }
        assert.equal(await page.locator('#nav-menu a[aria-current="page"]').count(), 1, `${file}: desktop active link count`);
        if (categories.includes(file)) {
          assert.equal(await page.locator(`#nav-menu .group a[aria-current="page"]`).getAttribute('href'), file);
          for (const detail of await page.locator('main details').all()) { await detail.locator('summary').click(); assert(await detail.getAttribute('open') !== null); await detail.locator('summary').click(); }
        } else if (file === 'index.html') {
          assert.equal(await page.locator('#nav-menu .group a[aria-current="page"]').count(), 0);
        }
        if (await page.locator('#nav-menu .group > button').isVisible()) {
          await page.locator('#nav-menu .group > button').click();
          assert.equal(await page.locator('#nav-menu .group > button').getAttribute('aria-expanded'), 'true');
          await page.keyboard.press('Escape');
          assert.equal(await page.locator('#nav-menu .group > button').getAttribute('aria-expanded'), 'false');
        } else {
          await page.locator('#menu-toggle').click();
          if (await page.locator('.mobile-submenu-toggle').getAttribute('aria-expanded') !== 'true') await page.locator('.mobile-submenu-toggle').click();
          assert.equal(await page.locator('.mobile-submenu-toggle').getAttribute('aria-expanded'), 'true');
          assert.equal(await page.locator('#mobile-menu a:visible').count(), 9);
          await page.locator('.mobile-submenu-toggle').click();
          await page.keyboard.press('Escape');
          await page.waitForTimeout(350);
          assert(await page.locator('#mobile-overlay').isHidden());
        }
        result.pages.push({ file, header, overflow: false, visibleImagesLoaded: true });
      }
      // Click each actual dropdown item, rather than only inspecting href attributes.
      for (const target of categories) {
        await page.goto(base, { waitUntil: 'networkidle' });
        if (await page.locator('#nav-menu .group > button').isVisible()) { await page.locator('#nav-menu .group > button').click(); await page.locator(`#nav-menu .group a[href="${target}"]`).click(); }
        else { await page.locator('#menu-toggle').click(); await page.locator('.mobile-submenu-toggle').click(); await page.locator(`#mobile-menu a[href="${target}"]`).click(); }
        await page.waitForURL(`**/${target}`);
        assert.equal(new URL(page.url()).pathname.split('/').pop(), target);
      }
      await page.goto(base, { waitUntil: 'networkidle' });
      result.sections = await page.locator('.hp-home > section').evaluateAll(sections => sections.map(element => ({ background: getComputedStyle(element).backgroundColor, title: element.querySelector('h1,h2')?.textContent })));
      assert.equal(result.sections.length, 8);
      result.sections.forEach((section, index) => assert.equal(section.background, index % 2 ? 'rgb(0, 0, 0)' : 'rgb(255, 255, 255)'));
      await page.locator('.hp-hero .hp-button').click();
      assert(await page.locator('#projects').evaluate(element => Math.abs(element.getBoundingClientRect().top) < 150));
      for (const [filter, count] of Object.entries({ all: 9, residential: 5, commercial: 3, farmhouse: 3, hotel: 2 })) {
        await page.locator(`.hp-filter[data-filter="${filter}"]`).click();
        assert.equal(await page.locator('.hp-project:visible').count(), count);
      }
      await page.locator('.hp-filter[data-filter="all"]').click();
      await page.evaluate(() => { window.__drafts = []; window.open = (...args) => window.__drafts.push(args); });
      await page.locator('#name').fill('QA Test');
      await page.locator('#mobile').fill('9999999999');
      await page.locator('#email').fill('qa@example.com');
      await page.locator('#project').selectOption('EON Fairfox');
      await page.locator('#contactForm button').click();
      assert.equal(await page.evaluate(() => window.__drafts.length), 0, 'Consent must block draft');
      await page.locator('.mpa-consent-box').check();
      await page.locator('#contactForm button').click();
      assert((await page.evaluate(() => window.__drafts[0][0])).startsWith('mailto:info@premiumpropertydepot.com'));
      result.homeForm = 'required consent and email draft verified; no email sent';
      const projectLinks = await page.locator('.hp-project-link').evaluateAll(links => links.map(link => link.getAttribute('href')));
      for (const href of projectLinks) {
        await page.goto(new URL(href, base).href, { waitUntil: 'networkidle' });
        assert(await page.evaluate(() => !!document.getElementById(location.hash.slice(1))), `Missing project target ${href}`);
      }
      result.projectTargets = projectLinks.length;
      await page.goto(new URL('contact.html', base).href, { waitUntil: 'networkidle' });
      await page.evaluate(() => { window.__drafts = []; window.open = (...args) => window.__drafts.push(args); });
      for (const [name, value] of Object.entries({ name: 'QA Test', email: 'qa@example.com', phone: '9999999999', message: 'QA enquiry draft only' })) await page.locator(`#contact-page-form [name="${name}"]`).fill(value);
      await page.locator('#contact-page-form button').click();
      assert((await page.evaluate(() => window.__drafts[0][0])).startsWith('mailto:info@premiumpropertydepot.com'));
      result.contactForm = 'email draft verified; no email sent';
      await page.goto(new URL('vacant-plots.html', base).href, { waitUntil: 'networkidle' });
      await page.locator('.property-listing-card').first().locator('.property-title').click();
      assert(await page.locator('#enquiry-modal').evaluate(element => element.classList.contains('active')));
      await page.evaluate(() => { window.__drafts = []; window.open = (...args) => window.__drafts.push(args); });
      await page.locator('#property-enquiry-form [name="name"]').fill('QA Test');
      await page.locator('#property-enquiry-form [name="phone"]').fill('9999999999');
      await page.locator('#property-enquiry-form [name="email"]').fill('qa@example.com');
      await page.locator('#property-enquiry-form [name="message"]').fill('QA draft only');
      await page.locator('#property-enquiry-form button[type="submit"]').click();
      assert((await page.evaluate(() => window.__drafts[0][0])).includes('Vrindaan'));
      result.modalForm = 'project prefill, modal close and email draft verified; no email sent';
      await page.goto(base, { waitUntil: 'networkidle' });
      for (const image of await page.locator('#homepage-content img').all()) { await image.scrollIntoViewIfNeeded(); await image.evaluate(async x => { if (!x.complete) await new Promise(resolve => { x.onload = resolve; x.onerror = resolve; }); }); }
      await page.evaluate(() => scrollTo(0, 0));
      await page.screenshot({ path: path.join('artifacts', `homepage-${width}.png`), fullPage: true });
      report.viewports.push(result);
      fs.writeFileSync('artifacts/browser-audit.json', JSON.stringify(report, null, 2));
      assert.equal(result.errors.length, 0, JSON.stringify(result.errors));
      assert.equal(result.failed.length, 0, JSON.stringify(result.failed));
      console.log(`Passed ${width}px: ${pages.length} pages, all five category clicks, nine project anchors, three enquiry paths, eight alternating sections.`);
      await context.close();
    }
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
