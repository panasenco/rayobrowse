# Session Management

> Source: https://docs.rayobrowse.com/features/session-management/

By default, a browser is tied to the CDP connection returned by `GET /connect`. When that connection closes, rayobrowse cleans up the browser after its grace period.

Use session management when you want to keep a browser alive across reconnects, inspect active sessions, or close a session explicitly. The same APIs work in local mode and rayobrowse Cloud.

## Keep a Session Alive

Section titled “Keep a Session Alive”

Pass `keepAlive=true` when creating the browser:

Terminal window
    
    
    curl -i "http://localhost:9222/connect?os=windows&headless;=false&keepAlive;=true&vnc;=true"

The response body is the CDP WebSocket URL. The response headers include the session ID and, if requested, the VNC URL:
    
    
    x-session-id: br_59245e8658532863
    
    x-vnc-url: http://localhost:6080/vnc.html?path=vnc/br_59245e8658532863&token;=

## Reconnect

Section titled “Reconnect”

Use the session ID with `sessionId`:

Terminal window
    
    
    curl "http://localhost:9222/connect?sessionId=br_59245e8658532863&vnc;=true"

That returns the CDP URL for the existing browser instead of creating a new one.

## SDK Example

Section titled “SDK Example”

  - Python 
  - Node.js 

    
    
    from rayobrowse import Rayobrowse
    
    from playwright.sync_api import sync_playwright
    
    
    
    
    client = Rayobrowse(endpoint="http://localhost:9222")
    
    ws_url = client.connect_url(os="windows", keep_alive=True, vnc=True)
    
    session_id = client.last_session_id
    
    
    
    
    with sync_playwright() as p:
    
        browser = p.chromium.connect_over_cdp(ws_url)
    
        page = browser.contexts[0].pages[0]
    
        page.goto("https://example.com")
    
        browser.close()
    
    
    
    
    # Later, reconnect to the same browser:
    
    ws_url = client.reconnect_url(session_id, vnc=True)
    
    print(client.last_vnc_url)
    
    
    import { Rayobrowse } from 'rayobrowse';
    
    import { chromium } from 'playwright';
    
    
    
    
    const client = new Rayobrowse({ endpoint: 'http://localhost:9222' });
    
    const wsUrl = await client.connectUrl({
    
      os: 'windows',
    
      keepAlive: true,
    
      vnc: true,
    
    });
    
    
    
    
    const sessionId = client.sessionId;
    
    const browser = await chromium.connectOverCDP(wsUrl);
    
    await browser.close();
    
    
    
    
    // Later, reconnect to the same browser:
    
    const reconnectedUrl = await client.reconnectUrl(sessionId!, { vnc: true });
    
    console.log(client.vncUrl);

## Close a Session

Section titled “Close a Session”

Most quick-start scripts can just close the CDP browser and let rayobrowse clean up. For explicit cleanup, call:

Terminal window
    
    
    curl -X POST "http://localhost:9222/api/browser/close" \
    
      -H "Content-Type: application/json" \
    
      -d '{"sessionId": "br_59245e8658532863"}'

## List and Inspect Sessions

Section titled “List and Inspect Sessions”

Terminal window
    
    
    curl "http://localhost:9222/api/browsers"
    
    curl "http://localhost:9222/api/browser/br_59245e8658532863/status"

Cloud uses the same paths with the cloud endpoint and your API key.

[ Previous   
Headless & Headful ](https://docs.rayobrowse.com/features/headless-headful/) [ Next   
Human Mouse ](https://docs.rayobrowse.com/features/human-mouse/)
