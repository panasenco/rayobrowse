# Connecting

> Source: https://docs.rayobrowse.com/cloud/connecting/

## Using `/connect` directly (recommended)

Section titled “Using /connect directly (recommended)”

The cloud `/connect` endpoint is an HTTP GET that creates a browser and returns the direct CDP WebSocket URL as plain text. No SDK required.

**Request:**

Terminal window
    
    
    curl -v "https://cloud.rayobrowse.com/connect?os=windows&vnc;=true" \
    
      -H "x-api-key: YOUR_API_KEY"

**Response:**
    
    
    < x-session-id: br_a7f3e91c20d84b01
    
    < x-vnc-url: https://1.2.3.4:6080/vnc.html?path=vnc/br_a7f3e91c20d84b01
    
    <
    
    wss://1.2.3.4:9222/cdp/br_a7f3e91c20d84b01

The response body is the CDP WebSocket URL pointing directly at the browser. The `x-vnc-url` header gives you a link to watch the session live in your browser.

Then connect your CDP client to the URL in the body. Here are some examples:

  - Python (Playwright) 
  - Node.js (Playwright) 
  - Node.js (Puppeteer) 

    
    
    import httpx
    
    from playwright.sync_api import sync_playwright
    
    
    
    
    resp = httpx.get(
    
        "https://cloud.rayobrowse.com/connect",
    
        params={"os": "windows"},
    
        headers={"x-api-key": "YOUR_API_KEY"},
    
        timeout=120,
    
    )
    
    resp.raise_for_status()
    
    cdp_url = resp.text.strip()
    
    
    
    
    with sync_playwright() as p:
    
        browser = p.chromium.connect_over_cdp(cdp_url)
    
        page = browser.new_page()
    
        page.goto("https://example.com")
    
        print(page.title())
    
        browser.close()
    
    
    const { chromium } = require('playwright');
    
    
    
    
    (async () => {
    
      const resp = await fetch(
    
        'https://cloud.rayobrowse.com/connect?os=windows',
    
        { headers: { 'x-api-key': 'YOUR_API_KEY' } }
    
      );
    
      const cdpUrl = (await resp.text()).trim();
    
    
    
    
      const browser = await chromium.connectOverCDP(cdpUrl);
    
      const page = await browser.newPage();
    
      await page.goto('https://example.com');
    
      console.log(await page.title());
    
      await browser.close();
    
    })();
    
    
    const puppeteer = require('puppeteer-core');
    
    
    
    
    (async () => {
    
      const resp = await fetch(
    
        'https://cloud.rayobrowse.com/connect?os=windows',
    
        { headers: { 'x-api-key': 'YOUR_API_KEY' } }
    
      );
    
      const cdpUrl = (await resp.text()).trim();
    
    
    
    
      const browser = await puppeteer.connect({ browserWSEndpoint: cdpUrl });
    
      const page = (await browser.pages())[0] || await browser.newPage();
    
      await page.goto('https://example.com');
    
      console.log(await page.title());
    
      await browser.disconnect();
    
    })();

### `/connect` parameters

Section titled “/connect parameters”

Cloud supports the same `/connect` parameters as local mode. Use your API key with the `x-api-key` header, `Authorization: Bearer`, or `token` query parameter.

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
  
### Response headers

Section titled “Response headers”

Header| Description  
---|---  
`x-session-id`| Unique session identifier (use for reconnection)  
`x-vnc-url`| noVNC URL (when `vnc=true`)  
  
### With proxy

Section titled “With proxy”
    
    
    https://cloud.rayobrowse.com/connect?os=windows&proxy;=http://user:pass@host:port

### With VNC

Section titled “With VNC”
    
    
    https://cloud.rayobrowse.com/connect?os=windows&vnc;=true

The VNC URL is returned in the `x-vnc-url` response header.

## Using the SDK (optional)

Section titled “Using the SDK (optional)”

The SDK wraps the `/connect` HTTP call and adds session management, reconnection, VNC URL retrieval, and typed errors. Only install it if you need those features.

  - Python 
  - Node.js 

    
    
    from rayobrowse import Rayobrowse
    
    from playwright.sync_api import sync_playwright
    
    
    
    
    client = Rayobrowse(
    
        endpoint="https://cloud.rayobrowse.com",
    
        api_key="your-api-key",
    
    )
    
    
    
    
    ws_url = client.connect_url(
    
        os="windows",
    
        proxy="http://user:pass@host:port",
    
        headless=True,
    
    )
    
    
    
    
    with sync_playwright() as p:
    
        browser = p.chromium.connect_over_cdp(ws_url)
    
        page = browser.new_page()
    
        page.goto("https://example.com")
    
        print(page.title())
    
        browser.close()
    
    
    
    
    client.close()
    
    
    import { Rayobrowse } from 'rayobrowse';
    
    import { chromium } from 'playwright';
    
    
    
    
    const client = new Rayobrowse({
    
      endpoint: 'https://cloud.rayobrowse.com',
    
      apiKey: 'your-api-key',
    
    });
    
    
    
    
    const wsUrl = await client.connectUrl({
    
      os: 'windows',
    
      proxy: 'http://user:pass@host:port',
    
      headless: true,
    
    });
    
    
    
    
    const browser = await chromium.connectOverCDP(wsUrl);
    
    const page = await browser.newPage();
    
    await page.goto('https://example.com');
    
    console.log(await page.title());
    
    await browser.close();
    
    
    
    
    await client.close();

Tip 

The SDK’s `connect_url()` / `connectUrl()` method calls the same `/connect` HTTP endpoint under the hood. It wraps it in a nicer API with error handling and session tracking.

## What happens under the hood

Section titled “What happens under the hood”

  1. Your code makes an HTTP GET to `https://cloud.rayobrowse.com/connect`
  2. The gateway creates a browser on one of the backend servers
  3. The response body contains the direct CDP WebSocket URL to the browser
  4. Response headers include `x-session-id` (for reconnection) and optionally `x-vnc-url`
  5. Your CDP client connects directly to the backend browser. The gateway is not in the data path after the initial `/connect` call

[ Previous   
Authentication ](https://docs.rayobrowse.com/cloud/authentication/) [ Next   
Limits ](https://docs.rayobrowse.com/cloud/limits/)
