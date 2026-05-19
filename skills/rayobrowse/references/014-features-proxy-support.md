# Proxy Support

> Source: https://docs.rayobrowse.com/features/proxy-support/

rayobrowse supports HTTP proxies at the browser level. All traffic from the session is routed through the proxy, and the fingerprint’s timezone and locale are automatically matched to the proxy’s geolocation.

## Usage

Section titled “Usage”

### Via HTTP /connect

Section titled “Via HTTP /connect”

Terminal window
    
    
    curl "http://localhost:9222/connect?headless=true&os;=windows&proxy;=http://user:pass@host:port"

### Via SDK

Section titled “Via SDK”
    
    
    client = Rayobrowse()
    
    ws_url = client.connect_url(os="windows", proxy="http://user:pass@host:port")
    
    
    const wsUrl = await client.connectUrl({
    
      os: 'windows',
    
      proxy: 'http://user:pass@host:port',
    
    });

## Self-hosted usage

Section titled “Self-hosted usage”

Self-hosted rayobrowse is free and unlimited whether you bring your own proxies or use [Rayobyte rotating proxies](https://rayobyte.com/products/). Cloud early access includes managed proxy options for teams that want browser infrastructure and proxies in one place.

## Proxy format

Section titled “Proxy format”
    
    
    http://username:password@hostname:port

SOCKS proxies are not currently supported.

[ Previous   
Overview ](https://docs.rayobrowse.com/features/fingerprinting/) [ Next   
Headless & Headful ](https://docs.rayobrowse.com/features/headless-headful/)
