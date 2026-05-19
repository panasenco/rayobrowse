# Upgrading

> Source: https://docs.rayobrowse.com/local/upgrading/

## Upgrade the Docker image

Section titled “Upgrade the Docker image”

Terminal window
    
    
    docker compose pull && docker compose up -d

## Upgrade the SDK

Section titled “Upgrade the SDK”

Terminal window
    
    
    # Python
    
    pip install --upgrade rayobrowse
    
    
    
    
    # Node.js
    
    npm update rayobrowse

## Versioning

Section titled “Versioning”

The Docker image and SDKs are versioned independently:

Component| Distribution| Contains  
---|---|---  
**Docker image** (`rayobyte/rayobrowse:latest`)| Docker Hub| Chromium binary, fingerprint engine, daemon server  
**Python SDK** (`rayobrowse`)| PyPI| Lightweight HTTP client  
**Node.js SDK** (`rayobrowse`)| npm| Lightweight HTTP client  
  
The SDKs maintain backward compatibility with older daemon versions, but upgrading both together is recommended for the best experience.

[ Previous   
Configuration ](https://docs.rayobrowse.com/local/configuration/) [ Next   
Overview ](https://docs.rayobrowse.com/cloud/overview/)
