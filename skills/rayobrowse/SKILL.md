---
name: rayobrowse
description: 
---

<prereqs>
Ensure Docker is installed and the current user can use it.
</prereqs>

<launch>
Locate the `assets` folder of this skill, then:
`docker compose up -f /path/to/assets/docker-compose.yml`
</launch>

<stealth>
Be careful to always appear as a human user to each site.
Don't do things that only a bot would do.
</stealth>
