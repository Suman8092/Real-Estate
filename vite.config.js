import { resolve } from 'path';
import { defineConfig } from 'vite';
import { copyFileSync } from 'node:fs';

export default defineConfig({
  root: './',
  base: './',
  plugins: [{
    name: 'legacy-vacant-plots-url',
    closeBundle() {
      // PHP-capable hosts can serve this HTML alias without runtime compilation.
      copyFileSync(resolve(__dirname, 'dist/vacant-plots.html'), resolve(__dirname, 'dist/vacant-plots.php'));
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
        industrial: resolve(__dirname, 'industrial.html')
      }
    }
  }
});
