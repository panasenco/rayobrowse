# GET /connect

> Source: https://docs.rayobrowse.com/api-reference/cloud/connect/

Creates a browser on the cloud platform and returns the direct CDP WebSocket URL. After this call, your CDP traffic goes directly to the browser. The gateway is not in the data path.

**URL** : `GET /connect`

**Auth** : `x-api-key` header and/or `token` query parameter

## Query parameters

Section titled “Query parameters”

Cloud supports the same parameters as the local `/connect` endpoint. Use your API key with the `x-api-key` header, `Authorization: Bearer`, or `token` query parameter.

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
  
## Response

Section titled “Response”

**Body** : Plain text CDP WebSocket URL

**Headers** :

Header| Description  
---|---  
`x-session-id`| Unique session identifier (use for reconnection)  
`x-vnc-url`| noVNC URL (when `vnc=true`)  
  
## Example

Section titled “Example”

Terminal window
    
    
    curl -v "https://cloud.rayobrowse.com/connect?os=windows&vnc;=true" \
    
      -H "x-api-key: your-key"

Response:
    
    
    < x-session-id: br_a7f3e91c20d84b01
    
    < x-vnc-url: https://143.198.72.51:6080/vnc.html?path=vnc/br_a7f3e91c20d84b01
    
    <
    
    wss://143.198.72.51:9222/cdp/br_a7f3e91c20d84b01

[ Previous   
GET /health ](https://docs.rayobrowse.com/api-reference/local/health/) [ Next   
POST /api/browser/close ](https://docs.rayobrowse.com/api-reference/cloud/browser-close/)
