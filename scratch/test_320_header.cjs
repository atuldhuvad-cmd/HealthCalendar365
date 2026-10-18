const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const APP_ROOT = path.resolve(__dirname, '..');

const server = http.createServer((req, res) => {
  let p = path.join(APP_ROOT, req.url.split('?')[0]);
  if (p.endsWith(path.sep)) p = path.join(p, 'index.html');
  if (fs.existsSync(p) && fs.statSync(p).isFile()) {
    const ext = path.extname(p).toLowerCase();
    const mime = { '.html': 'text/html', '.js': 'application/javascript', '.css': 'text/css', '.json': 'application/json', '.woff2': 'font/woff2' };
    res.writeHead(200, { 'Content-Type': mime[ext] || 'application/octet-stream' });
    fs.createReadStream(p).pipe(res);
  } else { res.writeHead(404); res.end(); }
});

server.listen(0, '127.0.0.1', async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 320, height: 600 });
  await page.goto(`http://127.0.0.1:${server.address().port}/`, { waitUntil: 'networkidle' });

  const widths = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('.segmented-control')).map((el, i) => ({
      index: i,
      scrollWidth: el.scrollWidth,
      rectWidth: el.getBoundingClientRect().width,
      buttons: Array.from(el.querySelectorAll('button')).map(b => ({
        text: b.innerText.trim().replace(/\n/g, ' '),
        width: b.getBoundingClientRect().width
      }))
    }));
  });

  console.log('Segmented Controls at 320px:');
  console.log(JSON.stringify(widths, null, 2));

  await browser.close();
  server.close();
});
