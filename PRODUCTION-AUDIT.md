# Production preparation audit

Prepared locally on 3 November 2026. No deployment has been performed and no production domain or provider has been assumed.

## Implemented

- All eight existing homepage sections alternate light/dark, starting light; the footer is light ivory with dark text and gold highlights.
- Existing header geometry, category URLs, project information and project images are retained. Two inherited mobile-drawer logos now use the actual company logo.
- Gallery cards open their own local project listing. All nine homepage project targets exist. All five category destinations remain separate.
- Tailwind is compiled and minified at build time; its development CDN script and unused font requests are removed. Unused reference styles and images do not ship in the production bundle.
- Seven referenced image assets were optimized, reducing the referenced source-image total from 3,170,875 to 2,188,221 bytes (about 31%). Logo artwork stays lossless. Image geometry and lazy loading are configured.
- Contact and modal forms now open validated email drafts instead of doing nothing or falsely claiming receipt. Modal drafts preserve name, phone, email, selected property and message. The homepage retains required consent and its email-draft action.
- Unverified WhatsApp and generic social-network homepage links are removed. Only verified phone and email destinations remain.
- Unique titles/descriptions, balanced heading tags, input accessible names, image alt text, robots.txt and Open Graph text are present. Real-domain canonical URLs, social image URLs and sitemap generation are implemented but await SITE_URL.
- Production assets use fingerprinted names and relative paths. The legacy vacant-plots.php compatibility build is retained. No source maps, development runtime, local backups, credentials or test artifacts are included in dist.

## Verification

The latest static audit checks nine HTML pages, 360 local references and 57 image instances, verified contact destinations, metadata, heading balance and absence of dummy service links. Isolated SEO tests exercise canonical/social URLs, a nine-page sitemap and removal of domain-specific metadata without modifying the real project or making network requests.

Browser tests run at 1440, 1280, 768 and 390px. The complete test matrix includes all nine pages, dropdown opening/closing and actual category clicks, active navigation states, nine project anchors, details disclosure, homepage filters, image loading, overflow, header geometry and all three enquiry paths. Reports are generated in artifacts/browser-audit.json with screenshots. Email drafts are intercepted; no messages are sent. Google Maps embeds are mocked for deterministic layout checks.

All four browser viewport runs passed: 36 page/view combinations, all five category clicks at each width, nine project targets at each width, and all three enquiry paths. No page/console errors, failed tested asset requests, broken visible images or horizontal page overflow were recorded. The light footer was also visually reviewed at desktop and mobile widths.

The production build passed; npm audit reported zero known vulnerabilities. Browser-test success and exact viewport results are recorded in the generated report. This does not certify every browser engine, physical device or external provider.

## Security and delivery limits

No exposed credential was found by the targeted source scan. No .env file, runtime environment variable, backend endpoint, database or existing hosting configuration is present. A package audit is a point-in-time check, not a guarantee against all vulnerabilities.

Forms are email-client actions. They do not automatically submit to a server or guarantee email delivery. Server-side submissions would require a configured backend and delivery testing.

The live Sarira source returned a verification screen during this session. Content was retained from complete source snapshots verified earlier in the same session; current inventory/availability cannot be independently reconfirmed from that live screen.

## Before deployment

- Supply the actual public HTTPS URL as SITE_URL and rebuild. Canonicals, sitemap.xml, robots sitemap declaration and absolute social image URLs are deliberately not fabricated while the domain is unknown.
- Choose a hosting target and configure HTTPS, compression, immutable caching for fingerprinted assets, HTML revalidation and appropriate security headers there. No provider-specific configuration has been guessed.
- Verify the legacy .php alias behavior if using that URL on a static host.
- Verify the actual map embed, font/icon providers, social previews, final-domain SEO URLs, email client behavior and all live URLs after publishing.
- Back up and verify any pre-existing hosted files and databases before overwriting them. There is currently no production website to back up.

A verified ZIP backup of the pre-change local project (including its original images, lockfile and prior build, excluding reproducible node_modules) is stored outside the repository in the sibling premiuminfradeveloper-backups folder. It must not be uploaded to the public website or repository.

See README.md for build commands, domain configuration and hosting handoff details.
