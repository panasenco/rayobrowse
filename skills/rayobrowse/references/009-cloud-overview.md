# Cloud Overview

> Source: https://docs.rayobrowse.com/cloud/overview/

rayobrowse Cloud is a managed browser service in early access. Instead of running Docker yourself, you connect to `https://cloud.rayobrowse.com` with an API key. No SDK required.

## How it works

Section titled “How it works”

  1. Make an HTTP GET to the `/connect` endpoint with your API key:

Terminal window
         
         curl "https://cloud.rayobrowse.com/connect?os=windows" \
         
           -H "x-api-key: YOUR_API_KEY"

  2. The response body is a direct CDP WebSocket URL to the browser

  3. Connect to that URL with Playwright, Puppeteer, Selenium, or any CDP client

  4. When you disconnect, the browser is cleaned up automatically

After the initial `/connect` request, your CDP client connects to the returned browser endpoint.

Tip 

The cloud `/connect` endpoint accepts the same parameters as local mode (`os`, `proxy`, `headless`, etc.). Add your API key with `x-api-key`, `Authorization: Bearer`, or the `token` query parameter.

## When to use cloud vs local

Section titled “When to use cloud vs local”

| Local Mode| Cloud Mode  
---|---|---  
**Setup**|  Docker on your machine| API key only  
**Connection**| `GET http://localhost:9222/connect?...` returns a CDP URL| `GET https://cloud.rayobrowse.com/connect?...` returns a CDP URL  
**Scaling**|  Limited by your hardware| Scales automatically  
**Cost**|  Free and unlimited self-hosted use| Early access managed service  
**Maintenance**|  You manage Docker updates| Managed for you  
**Best for**|  Development, small-scale, full control| Production, scaling, no infra management  
  
## Getting started

Section titled “Getting started”

  1. Get an API key by contacting [[email protected]](https://docs.rayobrowse.com/cdn-cgi/l/email-protection#e49785888197a496859d8b869d9081ca878b89)
  2. Follow the [cloud quickstart](https://docs.rayobrowse.com/quickstart-cloud) for working code in under 2 minutes

[ Previous   
Upgrading ](https://docs.rayobrowse.com/local/upgrading/) [ Next   
Authentication ](https://docs.rayobrowse.com/cloud/authentication/)
