# POST /api/browser/create

> Source: https://docs.rayobrowse.com/api-reference/local/browser-create/

Creates a browser and returns structured session metadata, including the CDP WebSocket URL. Most users should start with [`GET /connect`](https://docs.rayobrowse.com/api-reference/local/connect), which returns only the CDP URL.

**URL** : `POST /api/browser/create`

**Auth** : None.

## Request body

Section titled “Request body”
    
    
    {
    
      "headless": true,
    
      "os": "windows",
    
      "browser_name": "chrome",
    
      "browser_version_min": 146,
    
      "browser_version_max": 146,
    
      "proxy": "http://user:pass@host:port"
    
    }

## Response

Section titled “Response”
    
    
    {
    
      "success": true,
    
      "data": {
    
        "sessionId": "br_59245e8658532863",
    
        "wsEndpoint": "ws://localhost:9222/cdp/br_59245e8658532863"
    
      }
    
    }

Connect to the returned `wsEndpoint` with any CDP client. The session ID acts as the auth token for the CDP connection.

[ Previous   
GET /connect ](https://docs.rayobrowse.com/api-reference/local/connect/) [ Next   
POST /api/browser/close ](https://docs.rayobrowse.com/api-reference/local/browser-delete/)
