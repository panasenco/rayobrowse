# GET /connect

> Source: https://docs.rayobrowse.com/api-reference/local/connect/

Creates a browser and returns its CDP WebSocket URL as plain text. Pass that returned URL to Playwright, Puppeteer, Selenium, or any CDP client.

**URL** : `GET http://localhost:9222/connect`

**Auth** : None.

## Query parameters

Section titled “Query parameters”

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
  
## Example

Section titled “Example”

Terminal window
    
    
    curl "http://localhost:9222/connect?headless=true&os;=windows&proxy;=http://user:pass@host:port"

[ Previous   
Overview ](https://docs.rayobrowse.com/api-reference/overview/) [ Next   
POST /api/browser/create ](https://docs.rayobrowse.com/api-reference/local/browser-create/)
