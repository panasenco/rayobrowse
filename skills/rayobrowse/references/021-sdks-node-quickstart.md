# Node.js Quickstart

> Source: https://docs.rayobrowse.com/sdks/node/quickstart/

1. **Install**

Terminal window
         
         npm install rayobrowse playwright

  2. **Local usage**
         
         import { Rayobrowse } from 'rayobrowse';
         
         import { chromium } from 'playwright';
         
         
         
         
         const client = new Rayobrowse({
         
           endpoint: 'http://localhost:9222',
         
           apiKey: '',
         
         });
         
         
         
         
         const wsUrl = await client.connectUrl({ os: 'windows' });
         
         const browser = await chromium.connectOverCDP(wsUrl);
         
         const page = await browser.newPage();
         
         await page.goto('https://example.com');
         
         console.log(await page.title());
         
         await browser.close();

  3. **Cloud usage**
         
         const client = new Rayobrowse({
         
           endpoint: 'https://cloud.rayobrowse.com',
         
           apiKey: 'your-api-key',
         
         });
         
         
         
         
         const wsUrl = await client.connectUrl({
         
           os: 'windows',
         
           proxy: 'http://user:pass@host:port',
         
         });

  4. **Error handling**
         
         import { AuthError, ConcurrencyLimitError, RateLimitError } from 'rayobrowse';
         
         
         
         
         try {
         
           const wsUrl = await client.connectUrl({ os: 'windows' });
         
         } catch (err) {
         
           if (err instanceof AuthError) {
         
             console.error('Invalid API key');
         
           } else if (err instanceof ConcurrencyLimitError) {
         
             console.error(`Limit: ${err.active}/${err.limit}`);
         
           } else if (err instanceof RateLimitError) {
         
             console.error(`Rate limited, retry in ${err.retryAfter}s`);
         
           }
         
         }

## Next steps

Section titled “Next steps”

  - [Full API reference](https://docs.rayobrowse.com/sdks/node/reference)
  - [Fingerprint spoofing](https://docs.rayobrowse.com/features/fingerprinting)

[ Previous   
Reference ](https://docs.rayobrowse.com/sdks/python/reference/) [ Next   
Reference ](https://docs.rayobrowse.com/sdks/node/reference/)
