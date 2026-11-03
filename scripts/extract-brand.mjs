import sharp from 'sharp';
import { readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const source = 'images/premium-property-depot-logo.png';
const bytes = readFileSync(source);
const { data, info } = await sharp(bytes).ensureAlpha().raw().toBuffer({ resolveWithObject: true });
const frequencies = new Map();
for (let i = 0; i < data.length; i += 4) {
  if (data[i + 3] !== 255) continue;
  const hex = '#' + [...data.subarray(i, i + 3)].map(value => value.toString(16).padStart(2, '0')).join('').toUpperCase();
  if (!frequencies.has(hex)) frequencies.set(hex, { hex, pixels: 0, sample: { x: (i / 4) % info.width, y: Math.floor(i / 4 / info.width) } });
  frequencies.get(hex).pixels++;
}
const sorted = [...frequencies.values()].sort((a, b) => b.pixels - a.pixels);
const gold = sorted.filter(({ hex }) => {
  const [r, g, b] = hex.slice(1).match(/../g).map(value => parseInt(value, 16));
  return r > g && g > b && r - b > 50;
});
const palette = {
  source, sha256: createHash('sha256').update(bytes).digest('hex'), width: info.width, height: info.height,
  method: 'Count exact full-resolution RGB values of fully opaque pixels; no resizing, clustering, quantization or color adjustment. Gold candidates satisfy R > G > B and R - B > 50.',
  charcoal: sorted[0], gold: gold[0], highlight: gold[1], neutrals: ['#000000', '#FFFFFF']
};
writeFileSync('brand-palette.json', JSON.stringify(palette, null, 2) + '\n');
writeFileSync('css/brand-tokens.css', `/* Generated from exact logo pixels by npm run brand:extract. */\n:root{--brand-black:#000000;--brand-white:#FFFFFF;--brand-charcoal:${palette.charcoal.hex};--brand-gold:${palette.gold.hex};--brand-highlight:${palette.highlight.hex}}\n`);
console.log(JSON.stringify(palette, null, 2));
