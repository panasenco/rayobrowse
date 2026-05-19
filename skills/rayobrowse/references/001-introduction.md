# Introduction

> Source: https://docs.rayobrowse.com/

**rayobrowse** is a Chromium-based stealth browser built for web scraping, AI agents, and automation. It runs on headless Linux servers (no GPU required) and works with anything that speaks CDP: Playwright, Puppeteer, Selenium, you name it.

Standard headless Chromium gets blocked almost immediately by modern bot detection. rayobrowse fixes that. Each session gets a full device fingerprint with 50+ spoofed signals (user agent, screen resolution, WebGL, canvas, fonts, timezone, audio, and dozens more) that are all consistent with each other. Detection systems cross-check these signals against one another, so getting individual values right isn’t enough. The whole fingerprint has to tell the story of a single, real device. That’s what we do, and it’s the core focus of the product. If your browser is blocked, nothing else matters.

## Two ways to use rayobrowse

Section titled “Two ways to use rayobrowse”

Local Mode (Self-Hosted)

Run rayobrowse as a Docker container on your own machine or server. Free and unlimited for self-hosted use.

[Get started locally →](https://docs.rayobrowse.com/quickstart-local)

Cloud Early Access

Connect to the managed rayobrowse cloud service. No Docker required, just an API key.

[Get started with cloud →](https://docs.rayobrowse.com/quickstart-cloud)

## The `/connect` endpoint

Section titled “The /connect endpoint”

The fastest way to get going. Request `GET /connect` over HTTP, receive a CDP WebSocket URL as plain text, then connect your CDP client to that returned URL. Local and cloud use the same flow.

  - Python (Playwright) 
  - Node.js (Playwright) 
  - Node.js (Puppeteer) 

    
    
    import httpx
    
    from playwright.sync_api import sync_playwright
    
    
    
    
    resp = httpx.get(
    
        "http://localhost:9222/connect",
    
        params={"os": "windows", "headless": "false"},
    
        timeout=120,
    
    )
    
    resp.raise_for_status()
    
    cdp_url = resp.text.strip()
    
    
    
    
    with sync_playwright() as p:
    
        browser = p.chromium.connect_over_cdp(cdp_url)
    
        context = browser.contexts[0] if browser.contexts else browser.new_context()
    
        page = context.pages[0] if context.pages else context.new_page()
    
        page.goto("https://example.com")
    
        print(page.title())
    
        browser.close()
    
    
    const { chromium } = require('playwright');
    
    
    
    
    (async () => {
    
      const resp = await fetch(
    
        'http://localhost:9222/connect?headless=false&os;=windows'
    
      );
    
      const cdpUrl = (await resp.text()).trim();
    
    
    
    
      const browser = await chromium.connectOverCDP(cdpUrl);
    
      const context = browser.contexts()[0] || await browser.newContext();
    
      const page = context.pages()[0] || await context.newPage();
    
      await page.goto('https://example.com');
    
      console.log(await page.title());
    
      await browser.close();
    
    })();
    
    
    const puppeteer = require('puppeteer-core');
    
    
    
    
    (async () => {
    
      const resp = await fetch(
    
        'http://localhost:9222/connect?headless=false&os;=windows'
    
      );
    
      const cdpUrl = (await resp.text()).trim();
    
      const browser = await puppeteer.connect({ browserWSEndpoint: cdpUrl });
    
      const page = (await browser.pages())[0] || await browser.newPage();
    
      await page.goto('https://example.com');
    
      console.log(await page.title());
    
      await browser.disconnect();
    
    })();

That’s it. No API key, no SDK, no setup beyond Docker for local use. See [/connect endpoint](https://docs.rayobrowse.com/local/connect-endpoint) for all available parameters (proxy, OS fingerprint, language, screen size, etc.).

## Optional: SDKs

Section titled “Optional: SDKs”

For programmatic control over browser lifecycle, reconnection, and VNC viewing, use the [Python](https://docs.rayobrowse.com/sdks/python/quickstart) or [Node.js](https://docs.rayobrowse.com/sdks/node/quickstart) SDK. The SDKs are optional; they’re a convenience wrapper for when you need more than `/connect`.

## Works with everything

Section titled “Works with everything”

rayobrowse is compatible with any tool that speaks CDP:

[ Playwright ](https://docs.rayobrowse.com/integrations/playwright) Python and Node.js browser automation

[ Puppeteer ](https://docs.rayobrowse.com/integrations/puppeteer) Node.js browser automation

[ Selenium ](https://docs.rayobrowse.com/integrations/selenium) WebDriver/CDP automation

[ OpenClaw ](https://docs.rayobrowse.com/integrations/openclaw) AI agent framework

[ Scrapy ](https://docs.rayobrowse.com/integrations/scrapy) Web scraping with scrapy-playwright

## Why rayobrowse exists

Section titled “Why rayobrowse exists”

Every tool that needs to interact with the real web (scrapers, AI agents, workflow automations) depends on a browser. The problem is that standard headless Chromium is trivially detected and blocked by most websites. If your browser gets blocked, your whole pipeline stops.

rayobrowse gives those tools a browser that passes detection. Each session looks like a real device, with a matching fingerprint across 50+ signals that anti-bot systems check. We obsess over this because it’s the foundation everything else is built on.

It’s developed as part of [Rayobyte’s scraping platform](https://rayobyte.com/products/web-scraping-api) and is used by Rayobyte at billion-page-per-month scale.

[ Next   
Quickstart (Local) ](https://docs.rayobrowse.com/quickstart-local/)
