import { resolve } from 'path';
import { defineConfig } from 'vite';
import { copyFileSync, existsSync, readdirSync } from 'node:fs';

const propertyInputs = {};
const propsDir = resolve(__dirname, 'properties');
if (existsSync(propsDir)) {
  for (const file of readdirSync(propsDir)) {
    if (file.endsWith('.html')) {
      const key = 'property_' + file.replace(/\.html$/, '');
      propertyInputs[key] = resolve(propsDir, file);
    }
  }
}

export default defineConfig({
  root: './',
  base: './',
  plugins: [{
    name: 'legacy-vacant-plots-url',
    closeBundle() {
      // PHP-capable hosts can serve this HTML alias without runtime compilation.
      const src = resolve(__dirname, 'dist/vacant-plots.html');
      const dest = resolve(__dirname, 'dist/vacant-plots.php');
      if (existsSync(src)) copyFileSync(src, dest);
    }
  }],
  server: {
    port: 3000,
    open: true
  },
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        vacantPlots: resolve(__dirname, 'vacant-plots.html'),
        about: resolve(__dirname, 'about.html'),
        contact: resolve(__dirname, 'contact.html'),
        gallery: resolve(__dirname, 'gallery.html'),
        residential: resolve(__dirname, 'residential.html'),
        commercial: resolve(__dirname, 'commercial.html'),
        farmhouses: resolve(__dirname, 'farmhouses.html'),
        industrial: resolve(__dirname, 'industrial.html'),
        ...propertyInputs
      }
    }
  }
});
