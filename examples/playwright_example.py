import logging
import sys

import httpx
from playwright.sync_api import sync_playwright

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Example script showcasing rayobrowse with Playwright.

    This script creates a stealth browser, navigates to example.com, and waits
    for you to press Enter. You should see info logs showing the browser
    creation via the daemon.

    Prerequisites:
        pip install httpx playwright
    """

    endpoint = "http://localhost:9222"
    params = {
        "os": "windows",
        "headless": "false",
        "vnc": "true",
        "browser_name": "chrome",
        "browser_version_min": "146",
        "browser_version_max": "146",
        # "proxy": "http://username:password@host:port",
    }

    logging.info("Requesting browser via HTTP /connect")

    try:
        resp = httpx.get(
            f"{endpoint}/connect",
            params=params,
            timeout=120,
        )
        resp.raise_for_status()
        cdp_url = resp.text.strip()
        vnc_url = resp.headers.get("x-vnc-url") or "http://localhost:6080/vnc.html"
        logging.info("Browser ready: %s", cdp_url)
        logging.info("To view your browser in VNC go to: %s", vnc_url)

        # Connect to the browser via CDP WebSocket
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(cdp_url)

            # Get the default page (or create one)
            context = browser.contexts[0] if browser.contexts else browser.new_context()
            page = context.pages[0] if context.pages else context.new_page()

            wait = 30000

            # Navigate to example.com
            page.goto("https://example.com", wait_until="commit", timeout=wait)
            page.wait_for_load_state("domcontentloaded", timeout=wait)
            page.wait_for_timeout(3000)

            logging.info(f"Page title: {page.title()}")

            try:
                if sys.stdin.isatty():
                    input("[INFO] Press Enter to close the browser...")
                else:
                    page.wait_for_timeout(3000)
            except EOFError:
                page.wait_for_timeout(3000)

            # Closing the Playwright connection triggers daemon auto-cleanup
            # (2 second grace period, then the daemon kills the browser process)
            browser.close()

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
