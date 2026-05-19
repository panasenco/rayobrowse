# Quickstart (Cloud)

> Source: https://docs.rayobrowse.com/quickstart-cloud/

Connect to rayobrowse Cloud early access. No Docker, no SDK required. Just an API key and any CDP client.

## Prerequisites

Section titled “Prerequisites”

  - A rayobrowse Cloud API key. Contact [[email protected]](https://docs.rayobrowse.com/cdn-cgi/l/email-protection#d4a7b5b8b1a794a6b5adbbb6ada0b1fab7bbb9) for early access.
  - Python 3.10+ or Node.js 18+

## Option A: Connect directly (no SDK)

Section titled “Option A: Connect directly (no SDK)”

The cloud `/connect` endpoint is an HTTP GET that creates a browser and returns a direct CDP WebSocket URL as plain text. You then connect your CDP client to that URL.

  1. **Request a browser and connect**

Make an HTTP GET to `/connect` with your API key, then pass the returned CDP URL to your automation tool:

     - Python (Playwright) 
     - Node.js (Playwright) 
     - Node.js (Puppeteer) 
    
    # pip install httpx playwright && playwright install
    
    import httpx
    
    from playwright.sync_api import sync_playwright
    
    
    
    
    resp = httpx.get(
    
        "https://cloud.rayobrowse.com/connect",
    
        params={"os": "windows", "headless": "false"},
    
        headers={"x-api-key": "YOUR_API_KEY"},
    
        timeout=120,
    
    )
    
    resp.raise_for_status()
    
    cdp_url = resp.text.strip()
    
    vnc_url = resp.headers.get("x-vnc-url")
    
    
    
    
    with sync_playwright() as p:
    
        browser = p.chromium.connect_over_cdp(cdp_url)
    
        context = browser.contexts[0] if browser.contexts else browser.new_context()
    
        page = context.pages[0] if context.pages else context.new_page()
    
        page.goto("https://example.com")
    
        print(page.title())
    
        if vnc_url:
    
            print(f"To view your browser in VNC go to: {vnc_url}")
    
        browser.close()
    
    // npm install playwright
    
    const { chromium } = require('playwright');
    
    
    
    
    (async () => {
    
      const resp = await fetch(
    
        'https://cloud.rayobrowse.com/connect?os=windows&headless;=false',
    
        { headers: { 'x-api-key': 'YOUR_API_KEY' } }
    
      );
    
      const cdpUrl = (await resp.text()).trim();
    
      const vncUrl = resp.headers.get('x-vnc-url');
    
    
    
    
      const browser = await chromium.connectOverCDP(cdpUrl);
    
      const context = browser.contexts()[0] || await browser.newContext();
    
      const page = context.pages()[0] || await context.newPage();
    
      await page.goto('https://example.com');
    
      console.log(await page.title());
    
      if (vncUrl) console.log(`To view your browser in VNC go to: ${vncUrl}`);
    
      await browser.close();
    
    })();
    
    // npm install puppeteer-core
    
    const puppeteer = require('puppeteer-core');
    
    
    
    
    (async () => {
    
      const resp = await fetch(
    
        'https://cloud.rayobrowse.com/connect?os=windows&headless;=false',
    
        { headers: { 'x-api-key': 'YOUR_API_KEY' } }
    
      );
    
      const cdpUrl = (await resp.text()).trim();
    
    
    
    
      const browser = await puppeteer.connect({ browserWSEndpoint: cdpUrl });
    
      const page = (await browser.pages())[0] || await browser.newPage();
    
      await page.goto('https://example.com');
    
      console.log(await page.title());
    
      await browser.disconnect();
    
    })();

The response also includes `x-session-id` and `x-vnc-url` headers for session management and live viewing.

  2. **Add a proxy or change fingerprint (optional)**

Append parameters to the `/connect` URL:
         
         https://cloud.rayobrowse.com/connect?os=windows&proxy;=http://user:pass@host:port&headless;=true

## Option B: Use the SDK (optional)

Section titled “Option B: Use the SDK (optional)”

The rayobrowse SDK wraps the `/connect` HTTP call for you and adds session management, VNC URLs, and lifecycle control. Install it only if you need those features.

  1. **Install the SDK**

     - Python 
     - Node.js 

Terminal window
    
    pip install rayobrowse playwright && playwright install

Terminal window
    
    npm install rayobrowse playwright

  2. **Connect and automate**

     - Python 
     - Node.js 
    
    from rayobrowse import Rayobrowse
    
    from playwright.sync_api import sync_playwright
    
    
    
    
    client = Rayobrowse(
    
        endpoint="https://cloud.rayobrowse.com",
    
        api_key="YOUR_API_KEY",
    
    )
    
    ws_url = client.connect_url(os="windows")
    
    
    
    
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
    
      apiKey: 'YOUR_API_KEY',
    
    });
    
    
    
    
    const wsUrl = await client.connectUrl({ os: 'windows' });
    
    
    
    
    const browser = await chromium.connectOverCDP(wsUrl);
    
    const page = await browser.newPage();
    
    await page.goto('https://example.com');
    
    console.log(await page.title());
    
    await browser.close();
    
    
    
    
    await client.close();

  3. **View with VNC (optional)**

Pass `vnc=True` (Python) or `vnc: true` (Node) to `connect_url()` to get a live browser view:
         
         ws_url = client.connect_url(os="windows", vnc=True)
         
         print(f"Watch live: {client.last_vnc_url}")

## How cloud mode differs from local

Section titled “How cloud mode differs from local”

| Local| Cloud  
---|---|---  
**Infrastructure**|  You run Docker on your own machine| Managed by rayobrowse  
**Scaling**|  Limited by your hardware| Scales automatically  
**Authentication**|  No key required| API key required  
**Connection**| `GET http://localhost:9222/connect?...` returns a CDP URL| `GET https://cloud.rayobrowse.com/connect?...` returns a CDP URL  
**Usage model**|  Free and unlimited self-hosted use| Early access managed service  
  
## Next steps

Section titled “Next steps”

  - [Authentication](https://docs.rayobrowse.com/cloud/authentication) for API key details
  - [Session management](https://docs.rayobrowse.com/features/session-management) for close, reconnect, status
  - [Limits](https://docs.rayobrowse.com/cloud/limits) for concurrency and rate limiting
  - [SDK reference (Python)](https://docs.rayobrowse.com/sdks/python/reference)
  - [SDK reference (Node.js)](https://docs.rayobrowse.com/sdks/node/reference)

[ Previous   
Quickstart (Local) ](https://docs.rayobrowse.com/quickstart-local/) [ Next   
Overview ](https://docs.rayobrowse.com/local/overview/)
