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
- If the module involves an external service or multiple codebases, mention only the project path or project name, and briefly describe the purpose of that project or codebase as it relates to the module.

Required Structure:
```
## When to Use

## Overview

## Key locations

## Behavior agents must know

```

You can add another section if needed and important.
```

Just add it to the AGENTS.md, not the cursor rules.