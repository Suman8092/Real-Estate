import sharp from 'sharp';
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';

const references = new Set();
for (const file of readdirSync('.').filter(file => file.endsWith('.html'))) {
  for (const match of readFileSync(file, 'utf8').matchAll(/(?:src|href)="(images\/[^"?#]+)"/g)) references.add(match[1]);
}
let before = 0, after = 0, changed = 0;
for (const file of references) {
  if (!/\.(webp|png|jpe?g)$/i.test(file)) continue;
  const original = readFileSync(file);
  const image = sharp(original);
  const metadata = await image.metadata();
  // Preserve logo pixels and transparent artwork. Resize only photographic content.
  let output;
  if (/\.png$/i.test(file)) output = await image.png({ compressionLevel: 9 }).toBuffer();
  else {
    const resized = image.rotate().resize({ width: 1600, height: 1600, fit: 'inside', withoutEnlargement: true });
    output = /\.webp$/i.test(file) ? await resized.webp({ quality: 86, effort: 6 }).toBuffer() : await resized.jpeg({ quality: 86, mozjpeg: true }).toBuffer();
  }
  before += original.length;
  if (output.length < original.length * .9) { writeFileSync(file, output); after += output.length; changed++; }
  else after += original.length;
}
console.log(JSON.stringify({ referencedImages: references.size, optimized: changed, bytesBefore: before, bytesAfter: after, savedBytes: before - after }));
