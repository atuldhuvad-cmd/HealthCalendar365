const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const APP_ROOT = path.resolve(__dirname, '..');

const MIME = {
  '.html': 'text/html',
  '.js': 'application/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.woff2': 'font/woff2',
  '.svg': 'image/svg+xml'
};

const server = http.createServer((req, res) => {
  let cleanUrl = req.url.split('?')[0];
  let p = path.join(APP_ROOT, cleanUrl);
  if (p.endsWith(path.sep)) p = path.join(p, 'index.html');
  if (fs.existsSync(p) && fs.statSync(p).isFile()) {
    res.writeHead(200, { 'Content-Type': MIME[path.extname(p).toLowerCase()] || 'application/octet-stream' });
    fs.createReadStream(p).pipe(res);
  } else { res.writeHead(404); res.end(); }
});

server.listen(0, '127.0.0.1', async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 360, height: 740 });
  await page.goto(`http://127.0.0.1:${server.address().port}/`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(500);

  const data = await page.evaluate(() => {
    const list = [];
    const elements = [
      '.header',
      '.header-left',
      '.header-center',
      '.header-right',
      '.quick-week-bar',
      '.quick-week-label',
      '.quick-week-scroll',
      '.date-search-box',
      '.studio-layout',
      '.preview-column',
      '.preview-toolbar',
      '.toolbar-left',
      '.toolbar-center',
      '.toolbar-right',
      '.multi-observance-bar',
      '.canvas-viewport',
      '.canvas-wrapper',
      '#posterCanvas',
      '.export-action-bar',
      '.sidebar-column',
      '.sidebar-header',
      '.cards-control-grid',
      '.card-control-item'
    ];

    for (const sel of elements) {
      const el = document.querySelector(sel);
      if (el) {
        const rect = el.getBoundingClientRect();
        const style = window.getComputedStyle(el);
        list.push({
          selector: sel,
          rectWidth: Math.round(rect.width * 10) / 10,
          scrollWidth: el.scrollWidth,
          clientWidth: el.clientWidth,
          display: style.display,
          flexWrap: style.flexWrap,
          overflowX: style.overflowX,
          padding: style.padding,
          minWidth: style.minWidth
        });
      }
    }
    return list;
  });

  console.log('Component Measurements on 360px:');
  console.table(data);

  await browser.close();
  server.close();
});
