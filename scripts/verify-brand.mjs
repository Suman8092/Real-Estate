import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import sharp from 'sharp';

const palette = JSON.parse(readFileSync('brand-palette.json', 'utf8'));
const logo = readFileSync(palette.source);
assert.equal(createHash('sha256').update(logo).digest('hex'), palette.sha256, 'Logo differs from documented extraction');
const { data, info } = await sharp(logo).ensureAlpha().raw().toBuffer({ resolveWithObject: true });
const allowed = new Set([...palette.neutrals, ...['charcoal', 'gold', 'highlight'].map(key => palette[key].hex)]);
for (const key of ['charcoal', 'gold', 'highlight']) {
  const entry = palette[key], index = (entry.sample.y * info.width + entry.sample.x) * 4;
  const sampled = '#' + [...data.subarray(index, index + 3)].map(value => value.toString(16).padStart(2, '0')).join('').toUpperCase();
  assert.equal(sampled, entry.hex, `${key}: sampled RGB differs`);
  assert.equal(data[index + 3], 255, `${key}: sample must be fully opaque`);
}
for (const file of ['css/brand-tokens.css', 'css/home-identity.css', 'css/site-identity.css', 'css/property-listings.css', 'css/custom.css']) {
  const css = readFileSync(file, 'utf8');
  for (const match of css.matchAll(/#[\da-f]{3,8}\b/gi)) {
    const hex = match[0].length === 4 ? '#' + [...match[0].slice(1)].map(value => value.repeat(2)).join('') : match[0];
    assert(allowed.has(hex.toUpperCase()), `${file}: unapproved color ${match[0]}`);
  }
  assert(!/(?:linear|radial|conic)-gradient\(/.test(css), `${file}: unexpected gradient`);
}
const luminance = hex => {
  const values = hex.slice(1).match(/../g).map(value => parseInt(value, 16) / 255).map(value => value <= .04045 ? value / 12.92 : ((value + .055) / 1.055) ** 2.4);
  return values[0] * .2126 + values[1] * .7152 + values[2] * .0722;
};
for (const [foreground, background] of [[palette.gold.hex, '#FFFFFF'], [palette.highlight.hex, '#000000'], [palette.charcoal.hex, '#FFFFFF'], ['#FFFFFF', '#000000']]) {
  const [a, b] = [luminance(foreground), luminance(background)];
  assert((Math.max(a, b) + .05) / (Math.min(a, b) + .05) >= 4.5, `${foreground}/${background}: insufficient normal-text contrast`);
}
console.log('Passed: exact opaque logo samples, unchanged source logo, approved CSS palette, no gradients and normal-text contrast pairs.');
