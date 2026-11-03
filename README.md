# Premium Properties

Multipage real estate website with verified Sarira Demo2 content and imagery. The homepage has eight alternating pure-white/pure-black sections; other pages have a white introduction and black content area. The shared footer is pure white. An image-led split hero, an open featured-project row and an asymmetric gallery give the site its own composition. Existing page names and property categories are retained.

## Local development

Use a supported Node.js LTS release and npm:

```powershell
npm ci
npm run dev
```

Source HTML needs the dev server or a production build for module imports. Tailwind utilities are compiled locally; no development CDN script is shipped. After adding utility classes during development, run `npm run build:css` or restart the server.

## Build and checks

```powershell
npm run build
npm test
npm audit
npm run preview -- --host 127.0.0.1 --port 4201
```

In another terminal:

```powershell
npm run test:browser
npm run test:brand-browser
```

Browser QA uses installed Edge on Windows. Elsewhere install Playwright Chromium with `npx playwright install chromium`. A custom executable can be supplied as `BROWSER_EXECUTABLE`. Set `AUDIT_URL` to the actual preview URL if using another port. Reports and screenshots go to ignored `artifacts/`.

Checks cover nine HTML pages, four viewport sizes (1440, 1280, 768, 390px), category dropdown clicks and active states, nine project targets, details disclosure, filters, images, layout, console/network errors and three enquiry paths. The Google Maps iframe is mocked for deterministic tests; external service availability is not certified. Tests intercept email drafts and send no messages.

## Enquiries and verified contacts

This is a static site. There is no server-side contact endpoint, database, SMTP integration or runtime secret. Forms validate fields and open a draft in the visitor's email application addressed to info@premiumpropertydepot.com; the visitor must send that draft. Forms do not automatically deliver or store messages. Direct phone links use +91 9415378938 and +91 9305486716. Unverified WhatsApp and generic social homepages have been removed. A server-delivered enquiry workflow requires a separately configured backend before it can be claimed or tested.

## Images and assets

Only referenced images are included in the Vite output. Source project identities and logo proportions are preserved; photographs are optimized and off-screen images load lazily. `npm run optimize:images` is an explicit maintenance command, not a build step: back up files before running it again and avoid repeated lossy re-encoding. Image dimensions and fixed containers reserve layout space.

Unused inherited WordPress styles are not imported into the build. Source copies remain available for history. Google Fonts, Font Awesome CSS/fonts and the map iframe still depend on external providers. Verify those services on the eventual host.

## Domain-specific SEO: pending real address

Every page has a title, description, heading hierarchy and Open Graph title/description. Generated robots.txt is copied into the build. No reference or fabricated domain is used for canonical URLs or social URLs.

Once the actual HTTPS deployment URL (including any subdirectory) is known, run in PowerShell:

```powershell
$env:SITE_URL = Read-Host 'Actual public HTTPS website URL'
npm run build
npm test
```

This generates canonical URLs, og:url, an absolute logo image URL, the nine-page sitemap and its robots.txt declaration. Rebuild without SITE_URL to return to the current domain-neutral state. Canonical, sitemap and social preview verification awaits the real domain. SITE_URL is public build configuration, not a credential. No production runtime environment variables are required.

## Hosting handoff: no deployment performed

Deploy only the contents of `dist/` to the eventual document root or hosting base directory. Do not upload source files, node_modules, backups, .env files or test artifacts. Relative assets support domain-root or subdirectory hosting. The build emits vacant-plots.php as an HTML compatibility entry: verify that the chosen host serves that alias as HTML, or configure it to map to vacant-plots.html. Main navigation uses existing .html URLs and does not need PHP.

No hosting provider, domain, DNS, certificate, deployment credential or production backup exists yet. Nothing has been published. Before later deployment:

1. Verify the exact domain and hosting account. Back up any hosted files/databases and verify restoration before overwriting them.
2. Set SITE_URL, rebuild and rerun both test commands against that exact build.
3. Configure HTTPS and server headers using the host's supported configuration. Cache fingerprinted assets for one year with immutable; revalidate HTML, robots.txt and sitemap.xml. Cache the non-fingerprinted social logo conservatively. Enable Brotli/gzip where supported.
4. Configure X-Content-Type-Options: nosniff, a suitable Referrer-Policy and a tested Content Security Policy permitting required fonts/styles/maps. Enable HSTS only after HTTPS is verified. These settings cannot be configured or certified without a host.
5. Test every HTML URL, the legacy alias if required, actual map/font services, canonical/social URLs, robots.txt, sitemap, category/project links, mobile navigation and email/phone actions on the live domain.

See BRAND-COLORS.md for the exact sampled logo colors, extraction evidence and contrast pairings. Run `npm run brand:extract` after an intentional logo update; production builds run this automatically. The logo image and property images are not recolored.

See PRODUCTION-AUDIT.md for current results and deployment-dependent checks.
