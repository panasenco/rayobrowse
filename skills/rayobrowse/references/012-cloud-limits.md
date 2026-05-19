# Limits

> Source: https://docs.rayobrowse.com/cloud/limits/

## Concurrency limits

Section titled “Concurrency limits”

Each account has a maximum number of concurrent browser sessions. When you hit the limit, new `connect_url()` calls return a `429` error with concurrency details.

The SDKs throw a typed `ConcurrencyLimitError`:
    
    
    from rayobrowse import Rayobrowse, ConcurrencyLimitError
    
    
    
    
    try:
    
        ws_url = client.connect_url(os="windows")
    
    except ConcurrencyLimitError as e:
    
        print(f"Limit reached: {e.active}/{e.limit}")
    
        print(f"Retry after: {e.retry_after}s")
    
    
    import { ConcurrencyLimitError } from 'rayobrowse';
    
    
    
    
    try {
    
      const wsUrl = await client.connectUrl({ os: 'windows' });
    
    } catch (err) {
    
      if (err instanceof ConcurrencyLimitError) {
    
        console.log(`Limit: ${err.active}/${err.limit}, retry in ${err.retryAfter}s`);
    
      }
    
    }

## Rate limiting

Section titled “Rate limiting”

API requests are also subject to per-second rate limiting. When exceeded, you receive a `429` response with a `Retry-After` header.

The SDKs throw a `RateLimitError`:
    
    
    from rayobrowse import RateLimitError
    
    
    
    
    try:
    
        ws_url = client.connect_url(os="windows")
    
    except RateLimitError as e:
    
        print(f"Rate limited. Retry after: {e.retry_after}s")

## Error summary

Section titled “Error summary”

HTTP Status| SDK Error| Meaning  
---|---|---  
`401`| `AuthError`| Invalid or missing API key  
`429` (with `limit` in body)| `ConcurrencyLimitError`| Too many concurrent browsers  
`429` (without `limit`)| `RateLimitError`| Too many requests per second  
Other| `BrowserCreateError`| Browser creation failed  
  
## Increasing limits

Section titled “Increasing limits”

Contact [[email protected]](https://docs.rayobrowse.com/cdn-cgi/l/email-protection#4a392b262f390a382b332528333e2f64292527) to increase your concurrency limits.

[ Previous   
Connecting ](https://docs.rayobrowse.com/cloud/connecting/) [ Next   
Overview ](https://docs.rayobrowse.com/features/fingerprinting/)
