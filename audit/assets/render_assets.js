const { chromium } = require('playwright-core');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--no-sandbox'] });
  const jobs = [
    {svg:'logo.svg', out:'logo.png', w:470, h:110},
    {svg:'ic_tel.svg', out:'ic_tel.png', w:28, h:28},
    {svg:'ic_mail.svg', out:'ic_mail.png', w:28, h:28},
    {svg:'ic_pin.svg', out:'ic_pin.png', w:28, h:28},
    {svg:'ic_web.svg', out:'ic_web.png', w:28, h:28},
  ];
  for (const j of jobs){
    const p = await b.newPage({ deviceScaleFactor: 2 });
    const svg = require('fs').readFileSync(j.svg,'utf8');
    await p.setContent('<!doctype html><body style="margin:0">'+svg+'</body>', {waitUntil:'load'});
    await p.setViewportSize({width:j.w, height:j.h});
    const el = await p.$('svg');
    await el.screenshot({ path: j.out, omitBackground: true });
    await p.close();
  }
  await b.close(); console.log('assets rendered');
})().catch(e=>{console.error(e);process.exit(1)});
