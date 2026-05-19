# Quickstart (Local)

> Source: https://docs.rayobrowse.com/quickstart-local/

Get rayobrowse running locally in under 5 minutes. All you need is Docker and any CDP client (Playwright, Puppeteer, Selenium, etc.). No SDK required.

  1. **Set up environment**

Terminal window
         
         git clone https://github.com/rayobyte-data/rayobrowse.git
         
         cd rayobrowse
         
         cp .env.example .env

By using rayobrowse, you agree to the [license](https://docs.rayobrowse.com/licensing). The default `.env.example` works for local development.

  2. **Start the container**

Terminal window
         
         docker compose up -d

Docker automatically pulls the correct image for your architecture (x86_64 or ARM64).

  3. **Verify it’s running**

Terminal window
         
         curl http://localhost:9222/health
         
         # Should return: {"success": true, "data": {"status": "healthy", ...}}

  4. **Request a browser, then connect**

`/connect` is an HTTP endpoint. It creates a fresh browser and returns a CDP WebSocket URL as plain text. Pass that returned URL to your automation client.

     - Python (Playwright) 
     - Node.js (Playwright) 
     - Node.js (Puppeteer) 
    
    # pip install httpx playwright && playwright install
    
    import httpx
    
    from playwright.sync_api import sync_playwright
    
    
    
    
    resp = httpx.get(
    
        "http://localhost:9222/connect",
    
        params={"headless": "false", "os": "windows", "vnc": "true"},
    
        timeout=120,
    
    )
    
    resp.raise_for_status()
    
    
    
    
    cdp_url = resp.text.strip()
    
    vnc_url = resp.headers.get("x-vnc-url") or "http://localhost:6080/vnc.html"
    
    
    
    
    with sync_playwright() as p:
    
        browser = p.chromium.connect_over_cdp(cdp_url)
    
        context = browser.contexts[0] if browser.contexts else browser.new_context()
    
        page = context.pages[0] if context.pages else context.new_page()
    
        page.goto("https://example.com")
    
        print(page.title())
    
        print(f"To view your browser in VNC go to: {vnc_url}")
    
        browser.close()
    
    // npm install playwright
    
    const { chromium } = require('playwright');
    
    
    
    
    (async () => {
    
      const resp = await fetch(
    
        'http://localhost:9222/connect?headless=false&os;=windows&vnc;=true'
    
      );
    
      const cdpUrl = (await resp.text()).trim();
    
      const vncUrl = resp.headers.get('x-vnc-url') || 'http://localhost:6080/vnc.html';
    
    
    
    
      const browser = await chromium.connectOverCDP(cdpUrl);
    
      const context = browser.contexts()[0] || await browser.newContext();
    
      const page = context.pages()[0] || await context.newPage();
    
      await page.goto('https://example.com');
    
      console.log(await page.title());
    
      console.log(`To view your browser in VNC go to: ${vncUrl}`);
    
      await browser.close();
    
    })();
    
    // npm install puppeteer-core
    
    const puppeteer = require('puppeteer-core');
    
    
    
    
    (async () => {
    
      const resp = await fetch(
    
        'http://localhost:9222/connect?headless=false&os;=windows'
    
      );
    
      const cdpUrl = (await resp.text()).trim();
    
      const browser = await puppeteer.connect({ browserWSEndpoint: cdpUrl });
    
      const page = (await browser.pages())[0] || await browser.newPage();
    
      await page.goto('https://example.com');
    
      console.log(await page.title());
    
      await browser.disconnect();
    
    })();

View the browser live at <http://localhost:6080/vnc.html> (noVNC).

Tip 

rayobrowse also provides [Python](https://docs.rayobrowse.com/sdks/python/reference) and [Node.js](https://docs.rayobrowse.com/sdks/node/reference) SDKs for advanced use cases like managing multiple browsers, custom lifecycle control, and session management. The SDKs are optional. The HTTP `/connect` endpoint is all you need to get started.

## Next steps

Section titled “Next steps”

  - [/connect parameters](https://docs.rayobrowse.com/local/connect-endpoint) for customizing fingerprints, proxy, headless mode
  - [Configuration](https://docs.rayobrowse.com/local/configuration) for environment variables, ports, noVNC
  - [SDKs](https://docs.rayobrowse.com/sdks/overview) for optional Python and Node.js clients
  - [Integrations](https://docs.rayobrowse.com/integrations/overview) for Playwright, Puppeteer, Selenium, OpenClaw, Scrapy

[ Previous   
Introduction ](https://docs.rayobrowse.com/) [ Next   
Quickstart (Cloud) ](https://docs.rayobrowse.com/quickstart-cloud/)
