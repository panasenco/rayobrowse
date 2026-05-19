# Python SDK Reference

> Source: https://docs.rayobrowse.com/sdks/python/reference/

## `Rayobrowse` class

Section titled “Rayobrowse class”
    
    
    from rayobrowse import Rayobrowse
    
    
    
    
    client = Rayobrowse(
    
        endpoint="http://localhost:9222",  # or "https://cloud.rayobrowse.com"
    
        api_key=None,                    # required for cloud, optional for local
    
        timeout=120.0,                   # HTTP request timeout in seconds
    
    )

### Constructor parameters

Section titled “Constructor parameters”

Parameter| Type| Default| Description  
---|---|---|---  
`endpoint`| `str`| `"http://localhost:9222"`| HTTP(S) endpoint for local or cloud  
`api_key`| `str | None`| `None`| API key for cloud or authenticated self-hosted deployments  
`timeout`| `float`| `120.0`| HTTP request timeout in seconds  
  
### `connect_url(**kwargs) -> str`

Section titled “connect_url(**kwargs) -> str”

Get a CDP WebSocket URL for a new browser session. Pass the returned URL to `playwright.chromium.connect_over_cdp()`.

Parameter| Type| Default| Description  
---|---|---|---  
`os`| `str`| `"windows"`| Target OS fingerprint: `windows`, `linux`, `android`, `macos`  
`proxy`| `str | None`| `None`| Proxy URL (`http://user:pass@host:port`)  
`headless`| `bool`| `False`| Run headless  
`browser_language`| `str | None`| `None`| Accept-Language header value  
`max_lifetime`| `int | None`| `None`| Session TTL in seconds  
`vnc`| `bool`| `False`| Start per-browser noVNC session  
`**kwargs`| | | Additional query parameters passed through  
  
`connect_url()` calls `GET /connect` on the configured endpoint and returns the CDP WebSocket URL from the response body. The same method works for local and cloud endpoints.

### `reconnect_url(session_id: str) -> str`

Section titled “reconnect_url(session_id: str) -> str”

Get the CDP URL for an existing session. Useful when a client disconnects and wants to reconnect without creating a new browser.

### `close() -> None`

Section titled “close() -> None”

Close the browser from the most recent `connect_url()` call. If no session is active, this is a no-op.

### `list_browsers() -> list[dict]`

Section titled “list_browsers() -> list[dict]”

List active browser sessions.

### `get_health() -> dict`

Section titled “get_health() -> dict”

Check service health. Returns the JSON response from `GET /health`.

### Properties

Section titled “Properties”

Property| Type| Description  
---|---|---  
`last_session_id`| `str | None`| Session ID from the most recent `connect_url()` call  
`last_vnc_url`| `str | None`| VNC URL from the most recent `connect_url(vnc=True)` call  
  
## Exceptions

Section titled “Exceptions”

Exception| When raised  
---|---  
`RayobrowseError`| Base exception for all SDK errors  
`BrowserCreateError`| Browser creation failed (includes `status_code` and `body`)  
`ConnectionFailedError`| Cannot reach the rayobrowse service  
`DaemonNotRunning`| Local daemon is not running  
`ConcurrencyLimitError`| Cloud concurrency limit reached (includes `limit`, `active`, `retry_after`)  
`RateLimitError`| Request rate limit exceeded (includes `retry_after`)  
  
[ Previous   
Quickstart ](https://docs.rayobrowse.com/sdks/python/quickstart/) [ Next   
Quickstart ](https://docs.rayobrowse.com/sdks/node/quickstart/)
