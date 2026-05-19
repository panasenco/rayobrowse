# OpenClaw

> Source: https://docs.rayobrowse.com/integrations/openclaw/

[OpenClaw](https://openclaw.ai) is an AI agent framework for browser automation. rayobrowse gives OpenClaw a stealth-fingerprinted browser that passes detection.

Self-hosted rayobrowse is free and unlimited, enough to run OpenClaw as a personal assistant at zero cost.

## Quick start

Section titled “Quick start”

  1. **Start rayobrowse**

Terminal window
         
         docker compose up -d
         
         curl -s http://localhost:9222/health

  2. **Request a browser**

OpenClaw expects a CDP WebSocket URL. Request one from rayobrowse first:

Terminal window
         
         export RAYOBROWSE_CDP_URL="$(curl -s 'http://localhost:9222/connect?headless=true&os;=windows&keepAlive;=true')"
         
         echo "$RAYOBROWSE_CDP_URL"

  3. **Configure OpenClaw**

Add a `rayobrowse` browser profile to `~/.openclaw/openclaw.json`:
         
         {
         
           "browser": {
         
             "enabled": true,
         
             "defaultProfile": "rayobrowse",
         
             "profiles": {
         
               "rayobrowse": {
         
                 "cdpUrl": "PASTE_THE_RETURNED_CDP_URL_HERE"
         
               }
         
             }
         
           }
         
         }

Or via CLI:

Terminal window
         
         openclaw config set browser.enabled true
         
         openclaw config set browser.defaultProfile rayobrowse
         
         openclaw config set 'browser.profiles.rayobrowse.cdpUrl' \
         
           "$RAYOBROWSE_CDP_URL"

  4. **Verify**

Terminal window
         
         openclaw browser --browser-profile rayobrowse status

## Remote setup

Section titled “Remote setup”

For rayobrowse Cloud or an authenticated remote deployment, request the CDP URL with your API key:

Terminal window
    
    
    export RAYOBROWSE_CDP_URL="$(
    
      curl -s 'https://cloud.rayobrowse.com/connect?headless=true&os;=windows&keepAlive;=true' \
    
        -H 'x-api-key: your-secret-key'
    
    )"

## How it works

Section titled “How it works”

`GET /connect` creates a browser and returns the CDP WebSocket URL. OpenClaw connects to that returned URL. Use `keepAlive=true` if you want the session to survive an OpenClaw reconnect.

[ Previous   
Selenium ](https://docs.rayobrowse.com/integrations/selenium/) [ Next   
Scrapy ](https://docs.rayobrowse.com/integrations/scrapy/)
