# Local Mode Overview

> Source: https://docs.rayobrowse.com/local/overview/

In local mode, rayobrowse runs as a Docker container on your own machine or server. Your automation code asks the daemon for a browser with `GET /connect`, then connects to the returned CDP WebSocket URL.

## Architecture

Section titled “Architecture”
    
    
    ┌─────────────────────────────────────────────┐
    
    │  Your host machine                          │
    
    │                                             │
    
    │  ┌───────────────────┐                      │
    
    │  │  Your code        │                      │
    
    │  │  (Playwright,     │                      │
    
    │  │   Puppeteer, etc) │                      │
    
    │  └────────┬──────────┘                      │
    
    │           │ HTTP GET /connect               │
    
    │           ▼                                 │
    
    │  ┌───────────────────────────────────────┐  │
    
    │  │  rayobrowse container (:9222)         │  │
    
    │  │                                       │  │
    
    │  │  ┌─────────┐  ┌──────────────────┐    │  │
    
    │  │  │ Daemon  │  │ Fingerprint DB   │    │  │
    
    │  │  │ server  │  │ (thousands of    │    │  │
    
    │  │  │         │  │  real profiles)  │    │  │
    
    │  │  └────┬────┘  └──────────────────┘    │  │
    
    │  │       │                               │  │
    
    │  │       │ returns CDP URL               │  │
    
    │  │       ▼                               │  │
    
    │  │  ┌──────────────────┐                 │  │
    
    │  │  │ Chromium (custom  │                │  │
    
    │  │  │ patched binary)   │                │  │
    
    │  │  └──────────────────┘                 │  │
    
    │  │                                       │  │
    
    │  │  noVNC viewer (:6080)                 │  │
    
    │  └───────────────────────────────────────┘  │
    
    └─────────────────────────────────────────────┘

## Components

Section titled “Components”

Component| Where it lives| What it does  
---|---|---  
**Daemon server**|  Inside Docker container| Manages browser lifecycle, exposes `/connect` and REST API  
**Chromium binary**|  Inside Docker container| Custom-patched Chromium with anti-detection modifications  
**Fingerprint engine**|  Inside Docker container| Assigns real-world device profiles to each session  
**Python/Node SDK**|  Installed via pip/npm on host| Optional lightweight client that talks to the daemon  
**noVNC**|  Inside Docker container| Web viewer for watching sessions live on port 6080  
  
Note 

Zero system dependencies on your host machine beyond Docker. No Xvfb, no font packages, no Chromium install needed.

## Two ways to create browsers

Section titled “Two ways to create browsers”

Method| How it works| Best for  
---|---|---  
**HTTP`/connect` endpoint** _(recommended)_|  Call `GET http://localhost:9222/connect?...`, receive a CDP WebSocket URL, then connect your automation client to that returned URL. No SDK needed.| Quick scripts, any CDP client (Playwright, Puppeteer, Selenium), third-party tools (OpenClaw, Scrapy)  
**SDK`connect_url()`**| Install the SDK, call `connect_url()`, get the same CDP WebSocket URL back| Fine-grained control, multiple browsers, custom lifecycle management  
  
Tip 

Start with the HTTP `/connect` endpoint. It works with any language and any CDP client with zero extra dependencies. You can always switch to the SDK later if you need more control.

## Requirements

Section titled “Requirements”

  - **Docker** to run the container
  - **Any CDP client** (Playwright, Puppeteer, Selenium, etc.) for automation
  - **2GB+ RAM** available (~300MB per browser instance)

Works on Linux, Windows (native or WSL2), and macOS. Both **x86_64** and **ARM64** (Apple Silicon, AWS Graviton) are supported.

[ Previous   
Quickstart (Cloud) ](https://docs.rayobrowse.com/quickstart-cloud/) [ Next   
Installation ](https://docs.rayobrowse.com/local/installation/)
