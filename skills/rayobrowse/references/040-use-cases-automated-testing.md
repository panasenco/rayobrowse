# Automated Testing

> Source: https://docs.rayobrowse.com/use-cases/automated-testing/

rayobrowse can be used for E2E testing when you need a browser that behaves like a real user’s device rather than a detectable automation tool.

## When this is useful

Section titled “When this is useful”

  - Testing sites that behave differently for bot traffic
  - Verifying that your own bot detection is working correctly
  - Running tests through proxies with geographic fingerprint matching
  - Visual testing with realistic screen resolutions and fonts

## Example

Section titled “Example”
    
    
    import httpx
    
    from playwright.sync_api import sync_playwright
    
    
    
    
    resp = httpx.get(
    
        "http://localhost:9222/connect",
    
        params={"headless": "true", "os": "windows"},
    
        timeout=120,
    
    )
    
    resp.raise_for_status()
    
    cdp_url = resp.text.strip()
    
    
    
    
    with sync_playwright() as p:
    
        browser = p.chromium.connect_over_cdp(cdp_url)
    
        context = browser.contexts[0] if browser.contexts else browser.new_context()
    
        page = context.pages[0] if context.pages else context.new_page()
    
        page.goto("https://your-app.com")
    
    
    
    
        assert page.title() == "Expected Title"
    
        assert page.locator("#login-button").is_visible()
    
    
    
    
        browser.close()

[ Previous   
AI Agents ](https://docs.rayobrowse.com/use-cases/ai-agents/) [ Next   
Plans & Pricing ](https://docs.rayobrowse.com/plans/)
