# Scrapy

> Source: https://docs.rayobrowse.com/integrations/scrapy/

[scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) adds browser rendering to Scrapy. rayobrowse provides it with a stealth-fingerprinted browser instead of the default detectable Chromium.

## Setup

Section titled “Setup”

  1. **Install dependencies**

Terminal window
         
         pip install scrapy scrapy-playwright httpx

You don’t need `playwright install` since the browser runs inside the rayobrowse container.

  2. **Configure`settings.py`**
         
         import httpx
         
         
         
         
         _resp = httpx.get(
         
             "http://localhost:9222/connect",
         
             params={"headless": "true", "os": "windows"},
         
             timeout=120,
         
         )
         
         _resp.raise_for_status()
         
         PLAYWRIGHT_CDP_URL = _resp.text.strip()
         
         
         
         
         DOWNLOAD_HANDLERS = {
         
             "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
         
             "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
         
         }
         
         
         
         
         TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
         
         
         
         
         PLAYWRIGHT_PROCESS_REQUEST_HEADERS = None

Caution 

`PLAYWRIGHT_PROCESS_REQUEST_HEADERS = None` is important. Without it, Scrapy overrides the User-Agent that rayobrowse set on the fingerprint, causing a mismatch that detection systems flag.

  3. **Write your spider**
         
         import scrapy
         
         
         
         
         class QuotesSpider(scrapy.Spider):
         
             name = "quotes"
         
             start_urls = ["https://quotes.toscrape.com/js/"]
         
         
         
         
             def start_requests(self):
         
                 for url in self.start_urls:
         
                     yield scrapy.Request(
         
                         url,
         
                         meta={"playwright": True, "playwright_include_page": True},
         
                     )
         
         
         
         
             async def parse(self, response):
         
                 page = response.meta["playwright_page"]
         
                 await page.close()
         
         
         
         
                 for quote in response.css("div.quote"):
         
                     yield {
         
                         "text": quote.css("span.text::text").get(),
         
                         "author": quote.css("small.author::text").get(),
         
                     }

  4. **Run**

Terminal window
         
         scrapy crawl quotes -o quotes.json

## Using a proxy

Section titled “Using a proxy”
    
    
    resp = httpx.get(
    
        "http://localhost:9222/connect",
    
        params={
    
            "headless": "true",
    
            "os": "windows",
    
            "proxy": "http://user:[[email protected]](https://docs.rayobrowse.com/cdn-cgi/l/email-protection):8080",
    
        },
    
        timeout=120,
    
    )
    
    resp.raise_for_status()
    
    PLAYWRIGHT_CDP_URL = resp.text.strip()

## Remote or cloud endpoint

Section titled “Remote or cloud endpoint”
    
    
    resp = httpx.get(
    
        "https://cloud.rayobrowse.com/connect",
    
        params={"headless": "true", "os": "windows"},
    
        headers={"x-api-key": "your-secret-key"},
    
        timeout=120,
    
    )
    
    resp.raise_for_status()
    
    PLAYWRIGHT_CDP_URL = resp.text.strip()

A ready-to-run example project is available at [integrations/scrapy/](https://github.com/rayobyte-data/rayobrowse/tree/main/integrations/scrapy) in the GitHub repository.

[ Previous   
OpenClaw ](https://docs.rayobrowse.com/integrations/openclaw/) [ Next   
Overview ](https://docs.rayobrowse.com/api-reference/overview/)
