---
name: plan-behaviour-research
description: Run behaviour research for tech the plan touches, then add a Behaviour section to the current plan.
---

Add a `## Behaviour` section to the current plan. Same research method as `/behaviour-research`, scoped to the plan and written into the plan body.

## 1–2. Research

Follow `/behaviour-research` steps 1–2, with these plan-specific constraints:

- Scope to tech the **plan** actually touches. Skip everything else.
- Search pitfalls that intersect the plan’s **Tasks** (not a vague feature dump).

## 3. Write the section into the plan

Insert after `## What Current (Technical)` and before `## What Changes (Technical)` — this section extends the `/plan-rules` and `/plan-rules-simple` body order when this command is used.

```markdown
## Behaviour

### <tech> <exact version>
- [behaviour fact] — affects [domain or Task] ([source link])
```

Rules:

- Every fact names the exact installed version and links a source. No facts from memory alone.
- Include only facts that change how a Task is executed. This is a filter, not a dump.
- If research finds nothing surprising, write one line: `Verified <tech versions>; no version-specific behaviour affects this plan.`
- Plan tone still applies — facts only, no options, questions, or "consider".
- Fix plan if the behaviour research contradicts the plan.
