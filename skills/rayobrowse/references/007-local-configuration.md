# Configuration

> Source: https://docs.rayobrowse.com/local/configuration/

All configuration is done via environment variables in the `.env` file next to `docker-compose.yml`.

## Environment variables

Section titled “Environment variables”

Variable| Default| Description  
---|---|---  
`RAYOBROWSE_PORT`| `9222`| Host port mapped to the container  
  
Changes require a container restart:

Terminal window
    
    
    docker compose up -d

## Viewing the browser (noVNC)

Section titled “Viewing the browser (noVNC)”

Request VNC per browser by passing `vnc=true` to `/connect`:

Terminal window
    
    
    curl -i "http://localhost:9222/connect?headless=false&os;=windows&vnc;=true"

The response includes an `x-vnc-url` header. It will look like:
    
    
    x-vnc-url: http://localhost:6080/vnc.html?path=vnc/&token;=

## SDK environment variables

Section titled “SDK environment variables”

Examples and SDKs can read these variables:

Variable| Used by| Description  
---|---|---  
`RAYOBYTE_ENDPOINT`| Examples and SDKs| HTTP(S) endpoint (default: `http://localhost:9222`; cloud: `https://cloud.rayobrowse.com`)  
`RAYOBYTE_API_KEY`| Examples and SDKs| API key for rayobrowse Cloud  
  
## Docker resources

Section titled “Docker resources”

The rayobrowse container requires:

  - **Shared memory** : 2GB (`shm_size: 2g` in docker-compose.yml)
  - **RAM** : ~300MB per browser instance
  - **Security option** : `seccomp=unconfined` (for Chrome sandbox)

[ Previous   
/connect Endpoint ](https://docs.rayobrowse.com/local/connect-endpoint/) [ Next   
Upgrading ](https://docs.rayobrowse.com/local/upgrading/)
