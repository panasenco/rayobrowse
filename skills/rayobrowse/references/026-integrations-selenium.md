# Selenium

> Source: https://docs.rayobrowse.com/integrations/selenium/

Selenium can connect to rayobrowse via a CDP shim that bridges ChromeDriver to the daemon’s WebSocket endpoints.

Note 

Because rayobrowse uses a CDP proxy path (`ws://host:port/cdp/`) rather than a bare port, a lightweight local HTTP shim is needed to bridge Selenium/ChromeDriver. The example below includes this shim.

## Prerequisites

Section titled “Prerequisites”

Terminal window
    
    
    pip install rayobrowse selenium webdriver-manager

## Example

Section titled “Example”
    
    
    from rayobrowse import Rayobrowse
    
    from selenium import webdriver
    
    from selenium.webdriver.chrome.options import Options
    
    from selenium.webdriver.chrome.service import Service
    
    from webdriver_manager.chrome import ChromeDriverManager
    
    
    
    
    client = Rayobrowse(endpoint="http://localhost:9222")
    
    ws_url = client.connect_url(os="windows", headless=False)
    
    
    
    
    # The full Selenium example with CDP shim is available at:
    
    # https://github.com/rayobyte-data/rayobrowse/blob/main/examples/selenium_example.py

The complete example includes a `cdp_shim` context manager that:

  1. Starts a minimal local HTTP server
  2. Proxies ChromeDriver’s `/json/version` and `/json/list` requests to the daemon
  3. Allows Selenium to connect via `options.debugger_address`

See the [full example on GitHub](https://github.com/rayobyte-data/rayobrowse/blob/main/examples/selenium_example.py).

[ Previous   
Puppeteer ](https://docs.rayobrowse.com/integrations/puppeteer/) [ Next   
OpenClaw ](https://docs.rayobrowse.com/integrations/openclaw/)
