# POST /api/browser/close

> Source: https://docs.rayobrowse.com/api-reference/local/browser-delete/

Terminates a browser session by ID.

**URL** : `POST /api/browser/close`

**Auth** : None.

## Example

Section titled “Example”

Terminal window
    
    
    curl -X POST http://localhost:9222/api/browser/close \
    
      -H "Content-Type: application/json" \
    
      -d '{"sessionId": "br_59245e8658532863"}'

[ Previous   
POST /api/browser/create ](https://docs.rayobrowse.com/api-reference/local/browser-create/) [ Next   
GET /api/browsers ](https://docs.rayobrowse.com/api-reference/local/browsers-list/)
