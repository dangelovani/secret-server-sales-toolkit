// Reusable HTML -> PDF generator using Abacus HTML2PDF API.
// Usage: node gen.js <htmlFile> <outPdf> [format] [landscape]
const fs = require('fs');
const path = require('path');

// Supply credentials via the environment; never read another project's secrets.
const API_KEY = (process.env.ABACUSAI_API_KEY || process.env.ABACUS_API_KEY || '').trim();
if (!API_KEY) { console.error('Set ABACUSAI_API_KEY (or ABACUS_API_KEY) before generating PDFs.'); process.exit(1); }

const assets = JSON.parse(fs.readFileSync(path.join(__dirname, 'assets.json'), 'utf8'));

async function main() {
  const [htmlFile, outPdf, format, landscape, width, height, mode] = process.argv.slice(2);
  let html = fs.readFileSync(htmlFile, 'utf8');
  html = html.split('__LOGO_WHITE__').join(assets.white);
  html = html.split('__LOGO_TRANS__').join(assets.trans);
  if (assets.qr) html = html.split('__QR__').join(assets.qr);

  const pdf_options = {
    print_background: true,
    landscape: landscape === 'true',
    margin: { top: '0mm', right: '0mm', bottom: '0mm', left: '0mm' },
  };
  if (width && height) { pdf_options.width = width; pdf_options.height = height; }
  else { pdf_options.format = format || 'A4'; }

  if (mode === 'textfooter') {
    const conf = "<b style='color:#e7c96b;letter-spacing:1px'>CONFIDENTIAL</b> &nbsp; \u00A9 2026 The Secret Server. This document and its contents are confidential and proprietary to The Secret Server and are provided solely for the named recipient's evaluation. It may not be reproduced, distributed or disclosed, in whole or in part, without prior written consent. Any personal data referenced herein is processed in accordance with the UK GDPR and the EU General Data Protection Regulation (EU) 2016/679. All pricing, technology and methods described are commercially sensitive and remain the intellectual property of The Secret Server. &nbsp;&bull;&nbsp; <span style='color:#9fbcd6;font-weight:600'>832.637.6355 &bull; thesecretserver.co</span>";
    pdf_options.display_header_footer = true;
    pdf_options.header_template = "<div></div>";
    pdf_options.footer_template = "<div style='width:100%;box-sizing:border-box;background:#0d2a4d;color:#c7d6e6;padding:7px 40px;font-size:7.4px;line-height:1.45;text-align:justify;font-family:Inter,Arial,sans-serif;'>" + conf + "</div>";
    pdf_options.margin = { top: '0mm', right: '0mm', bottom: '24mm', left: '0mm' };
  }

  const createRes = await fetch('https://apps.abacus.ai/api/createConvertHtmlToPdfRequest', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${API_KEY}` },
    body: JSON.stringify({ html_content: html, pdf_options }),
  });
  if (!createRes.ok) { console.error('create failed', createRes.status, await createRes.text()); process.exit(1); }
  const { request_id } = await createRes.json();
  if (!request_id) { console.error('no request_id'); process.exit(1); }
  process.stdout.write(`[${path.basename(outPdf)}] req ${request_id} `);

  for (let i = 0; i < 150; i++) {
    await new Promise(r => setTimeout(r, 2000));
    const sRes = await fetch('https://apps.abacus.ai/api/getConvertHtmlToPdfStatus', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${API_KEY}` },
      body: JSON.stringify({ request_id }),
    });
    const sJson = await sRes.json();
    const status = sJson?.status || 'FAILED';
    if (status === 'SUCCESS') {
      const b64 = sJson?.result?.result;
      if (!b64) { console.error('no result data'); process.exit(1); }
      fs.writeFileSync(outPdf, Buffer.from(b64, 'base64'));
      console.log('OK ->', outPdf, `(${(fs.statSync(outPdf).size/1024).toFixed(0)}KB)`);
      return;
    }
    if (status === 'FAILED') { console.error('FAILED', JSON.stringify(sJson)); process.exit(1); }
    process.stdout.write('.');
  }
  console.error('timed out'); process.exit(1);
}
main().catch(e => { console.error(e); process.exit(1); });
