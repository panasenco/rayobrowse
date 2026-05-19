# GET /health

> Source: https://docs.rayobrowse.com/api-reference/local/health/

Returns the daemon’s health status. No authentication required.

**URL** : `GET /health`

## Example

Section titled “Example”

Terminal window
    
    
    curl http://localhost:9222/health

## Response

Section titled “Response”
    
    
    {
    
      "success": true,
    
      "data": {
    
        "status": "healthy"
    
      }
    
    }

[ Previous   
GET /api/browsers ](https://docs.rayobrowse.com/api-reference/local/browsers-list/) [ Next   
GET /connect ](https://docs.rayobrowse.com/api-reference/cloud/connect/)
