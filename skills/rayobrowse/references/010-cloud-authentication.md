# Authentication

> Source: https://docs.rayobrowse.com/cloud/authentication/

All cloud API requests require authentication via your API key.

## How to authenticate

Section titled “How to authenticate”

There are two ways to pass your API key:

### Via SDK (recommended)

Section titled “Via SDK (recommended)”

The SDK handles authentication automatically:
    
    
    from rayobrowse import Rayobrowse
    
    
    
    
    client = Rayobrowse(
    
        endpoint="https://cloud.rayobrowse.com",
    
        api_key="your-api-key",
    
    )
    
    
    import { Rayobrowse } from 'rayobrowse';
    
    
    
    
    const client = new Rayobrowse({
    
      endpoint: 'https://cloud.rayobrowse.com',
    
      apiKey: 'your-api-key',
    
    });

The SDK sends the key as:

  - `x-api-key` HTTP header on API calls
  - `token` query parameter on `/connect` requests

### Via HTTP headers (direct API calls)

Section titled “Via HTTP headers (direct API calls)”

If calling the API directly without the SDK:

Terminal window
    
    
    curl "https://cloud.rayobrowse.com/connect?os=windows" \
    
      -H "x-api-key: your-api-key"

## Error responses

Section titled “Error responses”

Status| Error| Meaning  
---|---|---  
`401`| Unauthorized| Invalid or missing API key  
`429`| Rate limited| Too many requests, see [limits](https://docs.rayobrowse.com/cloud/limits)  
  
The SDKs throw typed errors for these cases:

  - `AuthError` (401)
  - `RateLimitError` (429)
  - `ConcurrencyLimitError` (429 with concurrency details)

## Security

Section titled “Security”

  - Keep your API key secret. Don’t commit it to version control
  - Use environment variables to store your key
  - Each API key is scoped to your account

[ Previous   
Overview ](https://docs.rayobrowse.com/cloud/overview/) [ Next   
Connecting ](https://docs.rayobrowse.com/cloud/connecting/)
