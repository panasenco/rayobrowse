# AI Agents

> Source: https://docs.rayobrowse.com/use-cases/ai-agents/

AI agents need to browse real websites to do useful work. Standard headless Chromium gets detected and blocked on most sites, which means your agent can’t complete tasks.

rayobrowse gives agents a browser that passes detection. Request a browser from the HTTP `/connect` endpoint, then pass the returned CDP WebSocket URL to your agent framework:

Terminal window
    
    
    curl "http://localhost:9222/connect?headless=true&os;=windows"

Any framework that uses CDP can connect. Self-hosted rayobrowse is free and unlimited, which is enough to run something like OpenClaw as a personal assistant at zero cost.

## Integrations

Section titled “Integrations”

  - [OpenClaw](https://docs.rayobrowse.com/integrations/openclaw) has a full setup guide with config examples
  - More agent framework integrations (LangChain, CrewAI, etc.) are coming

## Running agents 24/7

Section titled “Running agents 24/7”

For always-on agents, [cloud early access](https://docs.rayobrowse.com/cloud/overview) handles the infrastructure so you don’t have to manage Docker yourself.

[ Previous   
Web Scraping ](https://docs.rayobrowse.com/use-cases/web-scraping/) [ Next   
Automated Testing ](https://docs.rayobrowse.com/use-cases/automated-testing/)
