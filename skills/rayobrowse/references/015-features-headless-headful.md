# Headless & Headful Modes

> Source: https://docs.rayobrowse.com/features/headless-headful/

## Headless mode

Section titled “Headless mode”

The default. Runs without a GUI, uses fewer resources.

Terminal window
    
    
    curl "http://localhost:9222/connect?headless=true&os;=windows"

## Headful mode

Section titled “Headful mode”

Runs a visible browser inside the container via Xvnc. You can watch sessions live through the built-in noVNC viewer.

Terminal window
    
    
    curl "http://localhost:9222/connect?headless=false&os;=windows&vnc;=true"

Use the `x-vnc-url` response header to open the browser view.

## VNC (noVNC viewer)

Section titled “VNC (noVNC viewer)”

VNC lets you view the browser from inside your own browser. It’s primarily useful for troubleshooting and debugging, so you can see exactly what the browser is doing.

VNC is requested per browser with `vnc=true`. The daemon returns the viewer URL in the `x-vnc-url` response header:
    
    
    x-vnc-url: http://localhost:6080/vnc.html?path=vnc/&token;=

Why VNC looks laggy 

The VNC stream may appear slow or choppy. This is because the framebuffer from a headless Linux server has to be compressed and transmitted over the network to your local browser. The actual browser on the remote server is running at full speed, and target websites see a fast, responsive browser. The lag is only in the display, not in the browser itself.

Pass `vnc=True` to `connect_url()` and use the returned VNC URL:
    
    
    ws_url = client.connect_url(os="windows", vnc=True)
    
    print(f"Watch live: {client.last_vnc_url}")
    
    
    const wsUrl = await client.connectUrl({ os: 'windows', vnc: true });
    
    console.log(`Watch live: ${client.vncUrl}`);

## When to use each

Section titled “When to use each”

Mode| Use case  
---|---  
Headless| Production scraping, CI/CD, performance-sensitive workloads  
Headful + VNC| Debugging, demos, visual verification, development  
  
[ Previous   
Proxy Support ](https://docs.rayobrowse.com/features/proxy-support/) [ Next   
Session Management ](https://docs.rayobrowse.com/features/session-management/)
