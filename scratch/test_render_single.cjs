const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

// Simple static server
const MIME = {
  '.html': 'text/html',
  '.js': 'application/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.woff2': 'font/woff2'
};

const server = http.createServer((req, res) => {
  let p = path.join(__dirname, '..', req.url.split('?')[0]);
  if (p.endsWith(path.sep)) p = path.join(p, 'index.html');
  if (fs.existsSync(p) && fs.statSync(p).isFile()) {
    const ext = path.extname(p).toLowerCase();
    res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
    fs.createReadStream(p).pipe(res);
  } else {
    res.writeHead(404);
    res.end('Not found: ' + req.url);
  }
});

server.listen(0, '127.0.0.1', async () => {
  const port = server.address().port;
  console.log('Serving on port', port);
  try {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'networkidle' });
    await page.waitForFunction(() => window.HEALTH_CALENDAR_DATA && window.HealthPosterRenderer);

    const dataUrl = await page.evaluate(async () => {
      const r = new HealthPosterRenderer();
      const day = window.HEALTH_CALENDAR_DATA.find(d => d.id === '10-15');
      const c = await r.renderPoster(day, { format: 'square', language: 'bilingual' });
      return c.toDataURL('image/png');
    });

    const base64 = dataUrl.replace(/^data:image\/png;base64,/, '');
    fs.writeFileSync(path.join(__dirname, 'test_10_15_square.png'), Buffer.from(base64, 'base64'));
    console.log('Rendered test_10_15_square.png successfully, size:', base64.length);
    await browser.close();
  } catch (err) {
    console.error('Error during render:', err);
  } finally {
    server.close();
  }
});
