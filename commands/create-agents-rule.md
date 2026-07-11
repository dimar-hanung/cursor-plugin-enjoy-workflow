---
name: create-agents-rule
description: Add an AGENTS.md rule requiring skills under .agents/skills for major features or modules.
---

# create-agents-rule

Add to AGENTS.md:
```
Every conversation or development cycle must create or update skills inside `.agents/skills`.

Format:
.agents/skills/develop-feature-[module-name]/SKILL.md
.agents/skills/develop-module-[feature-name]/SKILL.md

Scope:
This applies only to major features or modules.

Guidelines:
- Create skills at a higher level without getting too detailed (e.g., focus on relevant file locations rather than specific code implementations). but if there is any useful thing to know, add it.
The goal is to prevent the agent from needing to gather or explore too much context at the start.
- Use english language.


Required Structure:
```
## When to Use

## Overview

## Key locations

## Behavior agents must know

```

You can add another section if needed and important.
```