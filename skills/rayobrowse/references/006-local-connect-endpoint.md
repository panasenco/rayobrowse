# /connect Endpoint

> Source: https://docs.rayobrowse.com/local/connect-endpoint/

The `/connect` endpoint is the simplest way to use rayobrowse. Make an HTTP `GET` request, receive a CDP WebSocket URL as plain text, then pass that URL to Playwright, Puppeteer, Selenium, or any other CDP client.

The same protocol works locally and in cloud. Local uses `http://localhost:9222`; cloud uses `https://cloud.rayobrowse.com` plus your API key.

## Basic usage

Section titled “Basic usage”

Terminal window
    
    
    curl "http://localhost:9222/connect?headless=true&os;=windows"
    
    # ws://localhost:9222/cdp/

No SDK needed. Any CDP-capable tool can use the returned URL.

  - Python (Playwright) 
  - Node.js (Playwright) 
  - Node.js (Puppeteer) 

    
    
    # pip install httpx playwright && playwright install
    
    import httpx
    
    from playwright.sync_api import sync_playwright
    
    
    
    
    resp = httpx.get(
    
        "http://localhost:9222/connect",
    
        params={"headless": "true", "os": "windows"},
    
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
    
    
    // npm install playwright
    
    const { chromium } = require('playwright');
    
    
    
    
    (async () => {
    
      const resp = await fetch(
    
        'http://localhost:9222/connect?headless=true&os;=windows'
    
      );
    
      const cdpUrl = (await resp.text()).trim();
    
    
    
    
      const browser = await chromium.connectOverCDP(cdpUrl);
    
      const context = browser.contexts()[0] || await browser.newContext();
    
      const page = context.pages()[0] || await context.newPage();
    
      await page.goto('https://example.com');
    
      console.log(await page.title());
    
      await browser.close();
    
    })();
    
    
    // npm install puppeteer-core
    
    const puppeteer = require('puppeteer-core');
    
    
    
    
    (async () => {
    
      const resp = await fetch(
    
        'http://localhost:9222/connect?headless=true&os;=windows'
    
      );
    
      const cdpUrl = (await resp.text()).trim();
    
      const browser = await puppeteer.connect({ browserWSEndpoint: cdpUrl });
    
      const page = (await browser.pages())[0] || await browser.newPage();
    
      await page.goto('https://example.com');
    
      console.log(await page.title());
    
      await browser.disconnect();
    
    })();

## Parameters

Section titled “Parameters”

Parameter | Default | Example | Description  
---|---|---|---  
`headless`| `true`| `headless=false`| Run with or without a visible browser window.  
`os`| `linux`| `os=windows`| Fingerprint OS: `windows`, `linux`, `android`, `macos`.  
`browser_name`| `chrome`| `browser_name=chrome`| Browser fingerprint type.  
`browser_version_min`| latest| `browser_version_min=146`| Minimum Chrome version to emulate.  
`browser_version_max`| latest| `browser_version_max=146`| Maximum Chrome version to emulate.  
`proxy`| none| `proxy=http://user:pass@host:port`| Route browser traffic through an HTTP proxy.  
`browser_language`| auto| `browser_language=en-US`| Accept-Language value.  
`ui_language`| auto| `ui_language=en-US`| Browser UI locale.  
`screen_width_min`| auto| `screen_width_min=1366`| Minimum screen width.  
`screen_height_min`| auto| `screen_height_min=768`| Minimum screen height.  
`vnc`| `false`| `vnc=true`| Return an `x-vnc-url` header for live viewing.  
`keepAlive`| `false`| `keepAlive=true`| Keep the browser open across CDP disconnects.  
`sessionId`| none| `sessionId=br_...`| Reconnect to an existing keep-alive session.  
`maxLifetime`| none| `maxLifetime=300`| Hard session TTL in seconds.  
`token`| none| `token=YOUR_API_KEY`| API key query parameter for cloud or authenticated deployments.  
  
### Examples

#### Windows fingerprint with proxy
    
    
    curl "http://localhost:9222/connect?headless=true&os;=windows&proxy;=http://user:pass@host:port"

#### Headful browser with VNC
    
    
    curl -i "http://localhost:9222/connect?headless=false&os;=windows&vnc;=true"

Read the `x-vnc-url` response header and open that URL in your browser.

#### Reconnect to a keep-alive session
    
    
    curl "http://localhost:9222/connect?sessionId=br_59245e8658532863&vnc;=true"

Tip 

For optimal fingerprint matching, set `browser_version_min` and `browser_version_max` to **146** (the current Chromium version). Using a mismatched version may trigger detection on some sites.

## Lifecycle

Section titled “Lifecycle”

  1. **Created** when you call `GET /connect`.
  2. **Returned** as a CDP WebSocket URL in the response body.
  3. **Automated** by connecting your CDP client to the returned URL.
  4. **Closed** when the CDP client disconnects or when you call `POST /api/browser/close`.

Each connection gets a fresh browser instance with a new fingerprint profile.

[ Previous   
Installation ](https://docs.rayobrowse.com/local/installation/) [ Next   
Configuration ](https://docs.rayobrowse.com/local/configuration/)
