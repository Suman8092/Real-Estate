import assert from 'node:assert/strict';
import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { mkdtempSync, mkdirSync, copyFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { execFileSync } from 'node:child_process';

const pages = readdirSync('.').filter(file => file.endsWith('.html'));
let links = 0, images = 0;
for (const file of pages) {
  const html = readFileSync(file, 'utf8');
  assert(!/cdn\.tailwindcss\.com|https:\/\/(?:facebook|twitter|instagram|linkedin)\.com["/]/.test(html), `${file}: development or dummy service link`);
  assert(!/wa\.me\//.test(html), `${file}: unverified WhatsApp destination`);
  assert.equal([...html.matchAll(/<h1(?:\s|>)/g)].length, 1, `${file}: exactly one h1`);
  const headings = [];
  for (const tag of html.matchAll(/<(\/?)h([1-6])\b[^>]*>/g)) {
    if (!tag[1]) headings.push(tag[2]);
    else assert.equal(headings.pop(), tag[2], `${file}: mismatched heading tag`);
  }
  assert.equal(headings.length, 0, `${file}: unclosed heading`);
  for (const tag of ['<title>', 'name="description"', 'property="og:title"', 'property="og:description"']) assert(html.includes(tag), `${file}: missing ${tag}`);
  for (const match of html.matchAll(/<(?:a|img|script|link)\b[^>]*?(?:href|src)="([^"]*)"/g)) {
    const href = match[1].replaceAll('&amp;', '&');
    if (/^(?:https?:|mailto:|tel:|data:)/.test(href)) {
      if (href.startsWith('tel:')) assert(['tel:+919415378938', 'tel:+919305486716'].includes(href), `${file}: unverified phone`);
      if (href.startsWith('mailto:')) assert(href.startsWith('mailto:info@premiumpropertydepot.com'), `${file}: unverified email`);
      continue;
    }
    assert(href && href !== '#', `${file}: empty link`);
    const [path, fragment] = href.split('#');
    const target = path ? decodeURIComponent(path.split('?')[0]) : file;
    assert(existsSync(target), `${file}: missing ${target}`);
    if (fragment) assert(readFileSync(target, 'utf8').includes(`id="${fragment}"`), `${file}: missing anchor ${href}`);
    links++;
  }
  for (const match of html.matchAll(/<img\b[^>]*>/g)) {
    for (const attribute of ['alt', 'width', 'height']) assert(new RegExp(`\\b${attribute}="[^\"]+"`).test(match[0]), `${file}: image missing ${attribute}`);
    images++;
  }
}
const home = readFileSync('index.html', 'utf8');
const content = home.match(/<div class="hp-home">([\s\S]*?)<\/template>/)[1];
assert.equal([...content.matchAll(/<section\b/g)].length, 8, 'Preserve eight homepage sections');
const main = readFileSync('js/main.js', 'utf8');
assert(!main.includes('has been received'), 'Forms must not claim server delivery');
assert(main.includes("getElementById('contact-page-form')"), 'Contact form handler missing');
assert(existsSync('public/robots.txt'), 'robots.txt missing');
if (process.env.SITE_URL) assert(existsSync('public/sitemap.xml'), 'sitemap missing');
for (const dir of ['js', 'css']) for (const file of readdirSync(dir).filter(file => /\.(js|css)$/.test(file))) {
  const source = readFileSync(`${dir}/${file}`, 'utf8');
  assert(!/sk_live_[A-Za-z0-9]{12,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----/.test(source), `Potential credential in ${dir}/${file}`);
}
console.log(`Passed: ${pages.length} pages, ${links} local references, ${images} images, verified contacts, metadata, no runtime Tailwind or dummy service links.`);

// Exercise domain-dependent SEO in an isolated fixture; never set a deployment URL in this project.
const fixture = mkdtempSync(join(tmpdir(), 'premium-seo-test-'));
mkdirSync(join(fixture, 'images'));
for (const file of pages) copyFileSync(file, join(fixture, file));
copyFileSync('images/premium-property-depot-logo.png', join(fixture, 'images/premium-property-depot-logo.png'));
const command = resolve('scripts/seo.mjs');
const env = { ...process.env, SITE_URL: 'https://production-fixture.test/estate/' };
execFileSync(process.execPath, [command], { cwd: fixture, env, stdio: 'pipe' });
const sitemap = readFileSync(join(fixture, 'public/sitemap.xml'), 'utf8');
assert.equal([...sitemap.matchAll(/<url>/g)].length, 10);
assert(sitemap.includes('https://production-fixture.test/estate/residential.html'));
const fixtureHome = readFileSync(join(fixture, 'index.html'), 'utf8');
assert(fixtureHome.includes('rel="canonical" href="https://production-fixture.test/estate/"'));
assert(fixtureHome.includes('https://production-fixture.test/estate/social/brand.png'));
execFileSync(process.execPath, [command], { cwd: fixture, env: { ...env, SITE_URL: '' }, stdio: 'pipe' });
assert(!existsSync(join(fixture, 'public/sitemap.xml')));
assert(!readFileSync(join(fixture, 'index.html'), 'utf8').includes('rel="canonical"'));
console.log('Passed: isolated canonical, social image, sitemap and domain-reset generation; no real hosting target assumed.');
