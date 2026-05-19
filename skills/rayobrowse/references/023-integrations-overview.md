# Integrations Overview

> Source: https://docs.rayobrowse.com/integrations/overview/

rayobrowse works with **any tool that speaks CDP** (Chrome DevTools Protocol). The `/connect` endpoint is the universal entry point. Point any CDP client at it and you have a browser that passes detection.

Tool| Language| Guide  
---|---|---  
**Playwright**|  Python, Node.js| [Guide →](https://docs.rayobrowse.com/integrations/playwright)  
**Puppeteer**|  Node.js| [Guide →](https://docs.rayobrowse.com/integrations/puppeteer)  
**Selenium**|  Python| [Guide →](https://docs.rayobrowse.com/integrations/selenium)  
**OpenClaw**|  Python| [Guide →](https://docs.rayobrowse.com/integrations/openclaw)  
**Scrapy**|  Python| [Guide →](https://docs.rayobrowse.com/integrations/scrapy)  
  
All integrations use the `/connect` endpoint, so there’s nothing extra to install beyond the tool itself and a running rayobrowse container (or cloud API key).

More integrations (Firecrawl, LangChain, etc.) are coming. If you’d like a specific tool supported, open a [GitHub issue](https://github.com/rayobyte-data/rayobrowse/issues).
