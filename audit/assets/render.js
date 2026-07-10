const { chromium } = require('playwright-core');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--no-sandbox'] });
  const files = ['sig_Loyk_Duporge','sig_Lyes_Ouhaddad'];
  for (const f of files){
    const p = await b.newPage({ deviceScaleFactor: 2 });
    await p.goto('file://' + process.cwd() + '/' + f + '.html');
    await p.waitForTimeout(300);
    const el = await p.$('#sig');
    await el.screenshot({ path: f + '.png' });
    // also a transparent-trim not needed
    await p.close();
    console.log('rendered', f + '.png');
  }
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
