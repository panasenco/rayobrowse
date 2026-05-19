# Playwright

> Source: https://docs.rayobrowse.com/integrations/playwright/

Playwright connects to rayobrowse via CDP using `connect_over_cdp()` / `connectOverCDP()`. First call the HTTP `/connect` endpoint to get a CDP WebSocket URL, then pass that URL to Playwright.

## Using /connect (no SDK)

Section titled “Using /connect (no SDK)”

  - Python 
  - Node.js 

    
    
    import httpx
    
    from playwright.sync_api import sync_playwright
    
    
    
    
    resp = httpx.get(
    
        "http://localhost:9222/connect",
    
        params={"headless": "false", "os": "windows"},
    
        timeout=120,
    
    )
    
    resp.raise_for_status()
    
    cdp_url = resp.text.strip()
    
    
    
    
    with sync_playwright() as p:
    
        browser = p.chromium.connect_over_cdp(cdp_url)
    
        context = browser.contexts[0] if browser.contexts else browser.new_context()
    
        page = context.pages[0] if context.pages else context.new_page()
    
        page.goto("https://example.com")
    
        print(page.title())
    
        browser.close()
    
    
    const { chromium } = require('playwright');
    
    
    
    
    (async () => {
    
      const resp = await fetch(
    
        'http://localhost:9222/connect?headless=false&os;=windows'
    
      );
    
      const cdpUrl = (await resp.text()).trim();
    
    
    
    
      const browser = await chromium.connectOverCDP(cdpUrl);
    
      const context = browser.contexts()[0] || await browser.newContext();
    
      const page = context.pages()[0] || await context.newPage();
    
      await page.goto('https://example.com');
    
      console.log(await page.title());
    
      await browser.close();
    
    })();

## Using the SDK

Section titled “Using the SDK”

  - Python 
  - Node.js 

    
    
    from rayobrowse import Rayobrowse
    
    from playwright.sync_api import sync_playwright
    
    
    
    
    client = Rayobrowse()
    
    ws_url = client.connect_url(os="windows", headless=False)
    
    
    
    
    with sync_playwright() as p:
    
        browser = p.chromium.connect_over_cdp(ws_url)
    
        page = browser.new_page()
    
        page.goto("https://example.com")
    
        print(page.title())
    
        browser.close()
    
    
    import { Rayobrowse } from 'rayobrowse';
    
    import { chromium } from 'playwright';
    
    
    
    
    const client = new Rayobrowse({
    
      endpoint: 'http://localhost:9222',
    
      apiKey: '',
    
    });
    
    
    
    
    const wsUrl = await client.connectUrl({ os: 'windows', headless: false });
    
    const browser = await chromium.connectOverCDP(wsUrl);
    
    const page = await browser.newPage();
    
    await page.goto('https://example.com');
    
    console.log(await page.title());
    
    await browser.close();

## With proxy

Section titled “With proxy”
    
    
    resp = httpx.get(
    
        "http://localhost:9222/connect",
    
        params={
    
            "headless": "true",
    
            "os": "windows",
    
            "proxy": "http://user:pass@host:port",
    
        },
    
        timeout=120,
    
    )
    
    cdp_url = resp.text.strip()
    
    browser = p.chromium.connect_over_cdp(cdp_url)

[ Previous   
Integrations Overview ](https://docs.rayobrowse.com/integrations/overview/) [ Next   
Puppeteer ](https://docs.rayobrowse.com/integrations/puppeteer/)
