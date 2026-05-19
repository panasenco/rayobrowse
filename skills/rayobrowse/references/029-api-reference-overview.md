# API Reference Overview

> Source: https://docs.rayobrowse.com/api-reference/overview/

rayobrowse exposes the same HTTP `/connect` flow for local and cloud usage. `GET /connect` creates a browser and returns a CDP WebSocket URL as plain text.

## Authentication

Section titled “Authentication”

  - **Local mode** : No authentication required
  - **Cloud mode** : Requires `x-api-key`, `Authorization: Bearer`, or `token` query parameter

## Base URLs

Section titled “Base URLs”

Mode| Base URL  
---|---  
Local| `http://localhost:9222` (or custom port via `RAYOBROWSE_PORT`)  
Cloud| `https://cloud.rayobrowse.com`  
  
## Error format

Section titled “Error format”

API errors return JSON:
    
    
    {
    
      "error": {
    
        "message": "Description of the error",
    
        "code": "ERROR_CODE"
    
      }
    
    }

Common HTTP status codes:

Status| Meaning  
---|---  
`200`| Success  
`401`| Invalid or missing API key  
`429`| Rate limited or concurrency limit reached  
`500`| Internal server error  
  
[ Previous   
Scrapy ](https://docs.rayobrowse.com/integrations/scrapy/) [ Next   
GET /connect ](https://docs.rayobrowse.com/api-reference/local/connect/)
