# Installation

> Source: https://docs.rayobrowse.com/local/installation/

1. **Clone the repository**

Terminal window
         
         git clone https://github.com/rayobyte-data/rayobrowse.git
         
         cd rayobrowse

  2. **Configure environment**

Terminal window
         
         cp .env.example .env

By using rayobrowse, you agree to the [license](https://docs.rayobrowse.com/licensing). The default `.env.example` works for local development.

  3. **Start the container**

Terminal window
         
         docker compose up -d

Docker automatically pulls the `rayobyte/rayobrowse:latest` image for your architecture (x86_64 or ARM64).

  4. **Verify**

Terminal window
         
         curl http://localhost:9222/health

Expected response:
         
         {"success": true, "data": {"status": "healthy", ...}}

## What’s running

Section titled “What’s running”

After `docker compose up -d`, you have:

Port| Service  
---|---  
`9222`| Daemon API + CDP WebSocket proxy  
`6080`| noVNC viewer when requested with `vnc=true`  
  
## Docker Compose details

Section titled “Docker Compose details”

The `docker-compose.yml` from the repository:

  - **Image** : `rayobyte/rayobrowse:latest`
  - **Restart policy** : `unless-stopped`
  - **Shared memory** : `2g` (required for Chromium)
  - **Security** : `seccomp=unconfined` (required for Chrome sandbox)
  - **Volume** : `rayobrowse-data` mounted at `/data`
  - **Environment** : loaded from `.env`

## Install the SDK (optional)

Section titled “Install the SDK (optional)”

The `/connect` endpoint works without any SDK. For programmatic control, install the SDK:

Terminal window
    
    
    # Python
    
    pip install rayobrowse
    
    
    
    
    # Node.js
    
    npm install rayobrowse

Tip 

The SDK is intentionally minimal. It issues HTTP requests to the daemon and returns CDP WebSocket URLs. All browser-level logic runs inside the container.

## Troubleshooting

Section titled “Troubleshooting”

### Can’t connect to daemon

Section titled “Can’t connect to daemon”

Terminal window
    
    
    curl http://localhost:9222/health

If this fails, check that the container is running:

Terminal window
    
    
    docker compose ps
    
    docker compose logs -f

### Environment variable changes not taking effect

Section titled “Environment variable changes not taking effect”

The container reads `.env` at startup. After editing, recreate the container:

Terminal window
    
    
    docker compose up -d

[ Previous   
Overview ](https://docs.rayobrowse.com/local/overview/) [ Next   
/connect Endpoint ](https://docs.rayobrowse.com/local/connect-endpoint/)
