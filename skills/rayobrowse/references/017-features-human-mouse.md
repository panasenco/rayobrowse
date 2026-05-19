# Human Mouse

> Source: https://docs.rayobrowse.com/features/human-mouse/

rayobrowse includes optional human-like mouse movement and clicking, inspired by [HumanCursor](https://github.com/riflosnake/HumanCursor).

## How it works

Section titled “How it works”

Use Playwright’s `page.click()` and `page.mouse.move()` as you normally would. rayobrowse applies natural mouse curves and realistic click timing automatically. No code changes needed.

## What it does

Section titled “What it does”

  - Mouse movements follow Bezier curves instead of straight lines
  - Variable speed with acceleration and deceleration
  - Natural delay between mouse-down and mouse-up events
  - Works transparently with standard Playwright/Puppeteer/Selenium API calls
