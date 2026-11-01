// Serves ../site locally, then saves screenshots and a PDF of every page for review.
const http = require('http'), fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '..', 'site');
const out = path.resolve(__dirname, '..', 'preview');
const types = { '.html': 'text/html', '.css': 'text/css', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.xml': 'application/xml', '.txt': 'text/plain' };
const server = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0].split('#')[0]);
  let f = path.join(root, p);
  if (fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html');
  if (!fs.existsSync(f)) { res.writeHead(404); return res.end(fs.readFileSync(path.join(root, '404.html'))); }
  res.writeHead(200, { 'Content-Type': types[path.extname(f)] || 'application/octet-stream' });
  res.end(fs.readFileSync(f));
});
const order = ['', 'about', 'hip-replacement', 'revision-hip-replacement', 'knee-replacement', 'partial-knee-replacement',
  'revision-knee-replacement', 'knee-arthroscopy-meniscal-surgery', 'robotic-hip-and-knee-replacement', 'hip-arthritis', 'knee-arthritis',
  'meniscal-tear', 'problem-joint-replacement', 'second-opinion', 'hip-knee-clinic', 'fees-insurance', 'outcomes-reviews',
  'your-operation', 'gps-physiotherapists', 'contact', 'privacy'];
server.listen(8765, async () => {
  const browser = await chromium.launch();
  try {
    const desk = await browser.newPage({ viewport: { width: 1366, height: 900 } });
    await desk.goto('http://localhost:8765/', { waitUntil: 'networkidle' });
    await desk.screenshot({ path: path.join(out, 'home-desktop.png') });
    await desk.goto('http://localhost:8765/knee-replacement/', { waitUntil: 'networkidle' });
    await desk.screenshot({ path: path.join(out, 'knee-replacement-desktop.png') });
    const mob = await browser.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
    await mob.goto('http://localhost:8765/', { waitUntil: 'networkidle' });
    await mob.screenshot({ path: path.join(out, 'home-mobile.png') });
    const pdfPage = await browser.newPage({ viewport: { width: 1200, height: 1697 } });
    await pdfPage.emulateMedia({ media: 'screen' });
    let i = 0;
    for (const slug of order) {
      await pdfPage.goto(`http://localhost:8765/${slug ? slug + '/' : ''}`, { waitUntil: 'networkidle' });
      // header is sticky on screen; make it static so it is not repeated on every PDF page
      await pdfPage.addStyleTag({ content: '.site-header{position:static !important}' });
      i++;
      await pdfPage.pdf({ path: path.join(out, `p${String(i).padStart(2, '0')}.pdf`), width: '1200px', height: '1697px', printBackground: true, margin: { top: '0', bottom: '0' } });
    }
    console.log('rendered', i, 'pages');
  } finally { await browser.close(); server.close(); }
});
