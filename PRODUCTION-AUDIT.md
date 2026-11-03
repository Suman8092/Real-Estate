# Production preparation audit

**Current scope:** Only the homepage uses the new black-and-white design. The other eight pages have been restored to their layouts and styles from commit `388c3a7`, before the site-wide redesign, using isolated styles in `css/legacy/`. The separately requested footer logo, single email and combined About paragraph are retained. New-palette browser checks apply only to the homepage.
Prepared locally on 3 November 2026. No deployment has been performed and no production domain or provider has been assumed.

## Implemented

- All eight existing homepage sections alternate pure #FFFFFF/#000000, starting white. Every other page has an alternating white introduction and black content area; the shared white header/footer are excluded from body-section numbering.
- Existing header geometry, category URLs, project information and project images are retained. Two inherited mobile-drawer logos now use the actual company logo.
- Gallery cards open their own local project listing. All nine homepage project targets exist. All five category destinations remain separate.
- Tailwind is compiled and minified at build time; its development CDN script and unused font requests are removed. Unused reference styles and images do not ship in the production bundle.
- Seven referenced image assets were optimized, reducing the referenced source-image total from 3,170,875 to 2,188,221 bytes (about 31%). Logo artwork stays lossless. Image geometry and lazy loading are configured.
- Contact and modal forms now open validated email drafts instead of doing nothing or falsely claiming receipt. Modal drafts preserve name, phone, email, selected property and message. The homepage retains required consent and its email-draft action.
- Unverified WhatsApp and generic social-network homepage links are removed. Only verified phone and email destinations remain.
- Unique titles/descriptions, balanced heading tags, input accessible names, image alt text, robots.txt and Open Graph text are present. Real-domain canonical URLs, social image URLs and sitemap generation are implemented but await SITE_URL.
- Production assets use fingerprinted names and relative paths. The legacy vacant-plots.php compatibility build is retained. No source maps, development runtime, local backups, credentials or test artifacts are included in dist.

## Verification

The latest static audit checks nine HTML pages, 362 local references and 58 image instances, verified contact destinations, metadata, heading balance and absence of dummy service links. Isolated SEO tests exercise canonical/social URLs, a nine-page sitemap and removal of domain-specific metadata without modifying the real project or making network requests.

Browser tests run at 1440, 1280, 768 and 390px. The complete test matrix includes all nine pages, dropdown opening/closing and actual category clicks, active navigation states, nine project anchors, details disclosure, homepage filters, image loading, overflow, header geometry and all three enquiry paths. Reports are generated in artifacts/browser-audit.json with screenshots. Email drafts are intercepted; no messages are sent. Google Maps embeds are mocked for deterministic layout checks.

All four browser viewport runs passed: 36 page/view combinations, all five category clicks at each width, nine project targets at each width, and all three enquiry paths. No page/console errors, failed tested asset requests, broken visible images or horizontal page overflow were recorded. The pure-white footer was also visually reviewed at desktop and mobile widths.

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

## Exact-brand design refinement

BRAND-COLORS.md and brand-palette.json document full-resolution opaque pixel samples, frequencies, coordinates and the source logo hash. The UI uses only #000000, #FFFFFF, #4C4B47, #9A6C14 and #BE851A. Brand accents are never synthesized by lightening, opacity or gradients. Images retain their original colors.

The layout now has a split image-led hero, a broad featured project row, paired open project listings, an asymmetric gallery, numbered process rows and a two-column contact area. Per-page snapshots confirmed that no existing text, project image reference or link destination was removed. The extra hero image/caption uses the existing Vrindaan asset and published project text.

Computed color checks covered all nine pages at desktop width plus the homepage at 320, 390 and 768px. No out-of-palette foreground/background/border colors or page overflow were recorded for rendered UI elements. Intrinsic image colors, external iframe contents and browser-native control internals are excluded. No gradients were introduced.
