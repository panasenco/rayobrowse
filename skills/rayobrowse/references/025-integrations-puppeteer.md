# Puppeteer

> Source: https://docs.rayobrowse.com/integrations/puppeteer/

Puppeteer connects to rayobrowse via `puppeteer.connect()` with a `browserWSEndpoint`. First call the HTTP `/connect` endpoint to get a CDP WebSocket URL.

## Using /connect (no SDK)

Section titled “Using /connect (no SDK)”
    
    
    const puppeteer = require('puppeteer-core');
    
    
    
    
    (async () => {
    
      const resp = await fetch(
    
        'http://localhost:9222/connect?headless=false&os;=windows'
    
      );
    
      const cdpUrl = (await resp.text()).trim();
    
      const browser = await puppeteer.connect({ browserWSEndpoint: cdpUrl });
    
    
    
    
      const page = (await browser.pages())[0] || await browser.newPage();
    
      await page.goto('https://example.com', { waitUntil: 'domcontentloaded' });
    
      console.log(await page.title());
    
    
    
    
      await browser.disconnect();
    
    })();

Use `puppeteer-core` instead of `puppeteer` since the browser is provided by rayobrowse. No bundled Chromium download is needed.

## Using the API

Section titled “Using the API”

For more control, store the returned session ID for logs or reconnection:
    
    
    const puppeteer = require('puppeteer-core');
    
    
    
    
    const ENDPOINT = process.env.RAYOBYTE_ENDPOINT || 'http://localhost:9222';
    
    
    
    
    async function createBrowser() {
    
      const resp = await fetch(`${ENDPOINT}/connect?headless=false&os;=windows`);
    
      return {
    
        cdpUrl: (await resp.text()).trim(),
    
        sessionId: resp.headers.get('x-session-id'),
    
      };
    
    }
    
    
    
    
    const { cdpUrl, sessionId } = await createBrowser();
    
    const browser = await puppeteer.connect({ browserWSEndpoint: cdpUrl });
    
    console.log(`Session: ${sessionId}`);
    
    // Automate pages...
    
    await browser.disconnect();

## With proxy

Section titled “With proxy”
    
    
    const resp = await fetch(
    
      'http://localhost:9222/connect?headless=true&os;=windows&proxy;=http://user:pass@host:port'
    
    );
    
    const browser = await puppeteer.connect({
    
      browserWSEndpoint: (await resp.text()).trim(),
    
    });

[ Previous   
Playwright ](https://docs.rayobrowse.com/integrations/playwright/) [ Next   
Selenium ](https://docs.rayobrowse.com/integrations/selenium/)
