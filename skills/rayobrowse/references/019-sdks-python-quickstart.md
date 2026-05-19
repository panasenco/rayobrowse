# Python Quickstart

> Source: https://docs.rayobrowse.com/sdks/python/quickstart/

1. **Install**

Terminal window
         
         pip install rayobrowse playwright && playwright install

  2. **Local usage**
         
         from rayobrowse import Rayobrowse
         
         from playwright.sync_api import sync_playwright
         
         
         
         
         client = Rayobrowse()  # defaults to http://localhost:9222
         
         ws_url = client.connect_url(os="windows")
         
         
         
         
         with sync_playwright() as p:
         
             browser = p.chromium.connect_over_cdp(ws_url)
         
             page = browser.new_page()
         
             page.goto("https://example.com")
         
             print(page.title())
         
             browser.close()

  3. **Cloud usage**
         
         from rayobrowse import Rayobrowse
         
         
         
         
         client = Rayobrowse(
         
             endpoint="https://cloud.rayobrowse.com",
         
             api_key="your-api-key",
         
         )
         
         ws_url = client.connect_url(os="windows", proxy="http://user:pass@host:port")
         
         
         
         
         # Use ws_url with Playwright, Puppeteer, or any CDP client

  4. **VNC (visual browser access)**
         
         ws_url = client.connect_url(os="windows", vnc=True)
         
         print(f"CDP: {ws_url}")
         
         print(f"VNC: {client.last_vnc_url}")
         
         
         
         
         client.close()

## Next steps

Section titled “Next steps”

  - [Full API reference](https://docs.rayobrowse.com/sdks/python/reference)
  - [Fingerprint spoofing](https://docs.rayobrowse.com/features/fingerprinting)

[ Previous   
Overview ](https://docs.rayobrowse.com/sdks/overview/) [ Next   
Reference ](https://docs.rayobrowse.com/sdks/python/reference/)
