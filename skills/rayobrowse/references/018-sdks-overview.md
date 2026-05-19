# SDKs Overview

> Source: https://docs.rayobrowse.com/sdks/overview/

rayobrowse provides official SDKs for Python and Node.js/TypeScript. Both work with local self-hosted instances and rayobrowse Cloud.

Python SDK

Terminal window
    
    
    pip install rayobrowse

[Python quickstart →](https://docs.rayobrowse.com/sdks/python/quickstart)

Node.js SDK

Terminal window
    
    
    npm install rayobrowse

[Node.js quickstart →](https://docs.rayobrowse.com/sdks/node/quickstart)

## Do I need the SDK?

Section titled “Do I need the SDK?”

The `/connect` endpoint works **without any SDK**. Make an HTTP request, take the returned CDP WebSocket URL, and pass it to your CDP client. The SDKs are useful when you want:

  - Programmatic control over browser creation and lifecycle
  - Session reconnection
  - VNC URL retrieval
  - Typed error handling (auth, rate limits, concurrency)
  - Cloud integration with the same local API shape

## SDK vs /connect

Section titled “SDK vs /connect”

Feature| HTTP `/connect`| SDK  
---|---|---  
Create browser| `GET /connect` returns a CDP URL| `connect_url()` returns a CDP URL  
Close browser| Automatic on disconnect| Explicit `close()` call  
Reconnect| `sessionId` query parameter| `reconnect_url(session_id)`  
VNC URL| `x-vnc-url` response header| Available via `last_vnc_url` / `vncUrl`  
Error handling| HTTP status codes| Typed exceptions  
Works with| Any CDP client directly| Any CDP client (returns URL)  
  
[ Previous   
Human Mouse ](https://docs.rayobrowse.com/features/human-mouse/) [ Next   
Quickstart ](https://docs.rayobrowse.com/sdks/python/quickstart/)
