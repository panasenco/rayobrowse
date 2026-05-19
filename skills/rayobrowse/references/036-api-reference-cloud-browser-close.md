# POST /api/browser/close

> Source: https://docs.rayobrowse.com/api-reference/cloud/browser-close/

Terminates a browser session by ID.

**URL** : `POST /api/browser/close`

**Auth** : `x-api-key` header

## Request body

Section titled “Request body”
    
    
    {
    
      "browserId": "session-id-here"
    
    }

## Example

Section titled “Example”

Terminal window
    
    
    curl -X POST https://cloud.rayobrowse.com/api/browser/close \
    
      -H "x-api-key: your-key" \
    
      -H "Content-Type: application/json" \
    
      -d '{"sessionId": "abc123"}'

[ Previous   
GET /connect ](https://docs.rayobrowse.com/api-reference/cloud/connect/) [ Next   
GET /api/browser/:id/status ](https://docs.rayobrowse.com/api-reference/cloud/browser-status/)
