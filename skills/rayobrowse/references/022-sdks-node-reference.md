# Node.js SDK Reference

> Source: https://docs.rayobrowse.com/sdks/node/reference/

## `Rayobrowse` class

Section titled “Rayobrowse class”
    
    
    import { Rayobrowse } from 'rayobrowse';
    
    
    
    
    const client = new Rayobrowse({
    
      endpoint: 'https://cloud.rayobrowse.com', // or 'http://localhost:9222'
    
      apiKey: 'your-api-key',                 // required for cloud
    
    });

### Constructor

Section titled “Constructor”

Property| Type| Description  
---|---|---  
`endpoint`| `string`| HTTP(S) endpoint for local or cloud  
`apiKey`| `string`| API key (required for cloud, can be empty string for local)  
  
### `connectUrl(options?): Promise`

Section titled “connectUrl(options?): Promise”

Create a browser session and return the CDP WebSocket URL.

Option| Type| Description  
---|---|---  
`os`| `string`| Target OS fingerprint  
`proxy`| `string`| Proxy URL  
`headless`| `boolean`| Run headless  
`maxLifetime`| `number`| Session TTL in seconds  
`vnc`| `boolean`| Start noVNC session  
`browserLanguage`| `string`| Accept-Language header  
`uiLanguage`| `string`| UI locale  
`browserVersionMin`| `number`| Minimum browser version  
`browserVersionMax`| `number`| Maximum browser version  
`screenWidthMin`| `number`| Minimum screen width  
`screenHeightMin`| `number`| Minimum screen height  
`forceVisibility`| `boolean`| Force browser visibility  
`metadata`| `object`| Custom metadata (JSON-stringified)  
`protection`| `Record`| Per-feature protection overrides  
  
### `reconnectUrl(sessionId): Promise`

Section titled “reconnectUrl(sessionId): Promise”

Reconnect to an existing session by ID.

### `close(sessionId?): Promise`

Section titled “close(sessionId?): Promise”

Close a session. Defaults to the most recent session. Throws `RayobrowseError` if no session ID is available.

### `listBrowsers(): Promise[]>`

Section titled “listBrowsers(): Promise[]>”

List active browser sessions.

### `getHealth(): Promise`

Section titled “getHealth(): Promise”

Check service health.

### `getSessionCount(): Promise<{ limit: number; remaining: number }>`

Section titled “getSessionCount(): Promise<{ limit: number; remaining: number }>”

Check concurrent session limit and remaining capacity.

### Properties

Section titled “Properties”

Property| Type| Description  
---|---|---  
`sessionId`| `string | null`| Session ID from the most recent `connectUrl()` call  
`vncUrl`| `string | null`| VNC URL when `vnc: true` was used  
  
## Types

Section titled “Types”

### `ConnectOptions`

Section titled “ConnectOptions”
    
    
    interface ConnectOptions {
    
      os?: string;
    
      proxy?: string;
    
      headless?: boolean;
    
      maxLifetime?: number;
    
      vnc?: boolean;
    
      browserLanguage?: string;
    
      uiLanguage?: string;
    
      browserVersionMin?: number;
    
      browserVersionMax?: number;
    
      screenWidthMin?: number;
    
      screenHeightMin?: number;
    
      forceVisibility?: boolean;
    
      metadata?: Record<string, unknown>;
    
      protection?: Record<string, string>;
    
    }

### `HealthStatus`

Section titled “HealthStatus”
    
    
    interface HealthStatus {
    
      status: string;
    
      uptime: number;
    
    }

## Error classes

Section titled “Error classes”

Error| Status| Properties| Description  
---|---|---|---  
`RayobrowseError`| any| `statusCode`, `body`| Base error class  
`AuthError`| 401| | Invalid or missing API key  
`ConcurrencyLimitError`| 429| `limit`, `active`, `retryAfter`| Concurrent browser limit reached  
`RateLimitError`| 429| `retryAfter`| Request rate limit exceeded  
`BrowserCreateError`| varies| `statusCode`, `body`| Browser creation failed  
  
[ Previous   
Quickstart ](https://docs.rayobrowse.com/sdks/node/quickstart/) [ Next   
Integrations Overview ](https://docs.rayobrowse.com/integrations/overview/)
