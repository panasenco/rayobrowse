# Web Scraping

> Source: https://docs.rayobrowse.com/use-cases/web-scraping/

rayobrowse is built for scraping at scale. Rayobyte uses it in production at billion-page-per-month scale across heavily protected sites.

## Why you need a stealth browser

Section titled “Why you need a stealth browser”

Modern bot detection checks dozens of signals: user agent, WebGL renderer, canvas fingerprint, font list, screen resolution, timezone, WebRTC leaks, and more. Vanilla headless Chromium fails these checks immediately, which means your scraper stops before it starts.

rayobrowse handles all of this at the browser level. Each session gets a realistic device fingerprint from a database of thousands of real profiles, with 50+ signals that are all consistent with each other. Your scraping code connects via CDP and operates normally.

## Getting started

Section titled “Getting started”
    
    
    import httpx
    
    from playwright.sync_api import sync_playwright
    
    
    
    
    resp = httpx.get(
    
        "http://localhost:9222/connect",
    
        params={
    
            "headless": "true",
    
            "os": "windows",
    
            "proxy": "http://user:pass@host:port",
    
        },
    
        timeout=120,
    
    )
    
    resp.raise_for_status()
    
    cdp_url = resp.text.strip()
    
    
    
    
    with sync_playwright() as p:
    
        browser = p.chromium.connect_over_cdp(cdp_url)
    
        context = browser.contexts[0] if browser.contexts else browser.new_context()
    
        page = context.pages[0] if context.pages else context.new_page()
    
        page.goto("https://target-site.com")
    
        content = page.content()
    
        browser.close()

## Scaling up

Section titled “Scaling up”

  - Use [Scrapy + scrapy-playwright](https://docs.rayobrowse.com/integrations/scrapy) for crawling
  - Route through [Rayobyte proxies](https://docs.rayobrowse.com/features/proxy-support) or your own proxies
  - Use [cloud early access](https://docs.rayobrowse.com/cloud/overview) for managed infrastructure

[ Previous   
GET /api/browser/:id/status ](https://docs.rayobrowse.com/api-reference/cloud/browser-status/) [ Next   
AI Agents ](https://docs.rayobrowse.com/use-cases/ai-agents/)
