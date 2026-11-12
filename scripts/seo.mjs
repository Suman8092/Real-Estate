import { readdirSync, readFileSync, writeFileSync, mkdirSync, existsSync, unlinkSync, copyFileSync } from 'node:fs';

// Set SITE_URL only after the real HTTPS deployment address has been selected.
const value = process.env.SITE_URL?.trim();
let base;
if (value) {
  const url = new URL(value);
  if (url.protocol !== 'https:' || url.username || url.password || url.search || url.hash || /localhost|example\.(com|org)|127\.0\.0\.1/.test(url.hostname)) throw new Error('SITE_URL must be the real public HTTPS deployment URL, without credentials, query or fragment.');
  base = url.href.replace(/\/?$/, '/');
}
const escape = value => value.replaceAll('&', '&amp;').replaceAll('"', '&quot;').replaceAll('<', '&lt;');
const descriptions = {
  'residential.html': 'Explore residential property options including Vrindaan, Aurya City, Vantara Heritage, BNX Group and Godrej Tropical Isle.',
  'commercial.html': 'Explore Lifestyle Central, BNX Group and EON Fairfox. Review commercial project information and contact Premium Properties.',
  'farmhouses.html': 'Explore farmhouse and holiday-home project information for Vantara Heritage, Anantara and Casa Corbett.',
  'industrial.html': 'Contact Premium Properties for industrial property enquiries. No verified industrial listings are currently published.',
  'properties.html': 'Browse all listed Premium Property Depot projects and view property details, photos and locations.'
};
const pages = readdirSync('.').filter(file => file.endsWith('.html'));
for (const file of pages) {
  let html = readFileSync(file, 'utf8').replace(/\s*<!-- production-seo:start -->[\s\S]*?<!-- production-seo:end -->/g, '');
  if (!/<meta name="description"/.test(html)) html = html.replace('</title>', `</title>\n  <meta name="description" content="${escape(descriptions[file])}" />`);
  const title = html.match(/<title>(.*?)<\/title>/s)[1];
  const description = html.match(/<meta name="description" content="([^"]*)"/)[1];
  let tags = `\n  <!-- production-seo:start -->\n  <meta property="og:type" content="website" />\n  <meta property="og:site_name" content="Premium Properties" />\n  <meta property="og:title" content="${escape(title)}" />\n  <meta property="og:description" content="${description}" />\n  <meta name="twitter:card" content="summary_large_image" />\n  <meta property="og:image:alt" content="Premium Property Depot LLP logo" />`;
  if (base) {
    const canonical = new URL(file === 'index.html' ? './' : file, base).href;
    tags += `\n  <link rel="canonical" href="${escape(canonical)}" />\n  <meta property="og:url" content="${escape(canonical)}" />\n  <meta property="og:image" content="${escape(new URL('social/brand.png', base).href)}" />`;
  }
  tags += '\n  <!-- production-seo:end -->\n';
  html = html.replace('</head>', `${tags}</head>`);
  writeFileSync(file, html);
}
mkdirSync('public', { recursive: true });
mkdirSync('public/social', { recursive: true });
copyFileSync('images/premium-property-depot-logo.png', 'public/social/brand.png');
writeFileSync('public/robots.txt', `User-agent: *\nAllow: /\n${base ? `\nSitemap: ${new URL('sitemap.xml', base).href}\n` : ''}`);
if (base) writeFileSync('public/sitemap.xml', `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${pages.map(file => `<url><loc>${escape(new URL(file === 'index.html' ? './' : file, base).href)}</loc></url>`).join('')}</urlset>\n`);
else if (existsSync('public/sitemap.xml')) unlinkSync('public/sitemap.xml');
console.log(base ? 'Production canonical URLs, sitemap and social URLs generated.' : 'Domain-neutral SEO prepared. Canonicals, sitemap and absolute social URLs await SITE_URL.');
