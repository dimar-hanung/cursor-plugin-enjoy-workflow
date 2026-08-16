---
name: search-idea
description: Find one real improvement or feature idea with clear leverage from conversation context — not a bug, smell, or perf fix.
---

Hunt **one** idea — an improvement, feature, or leverage opportunity — from the current conversation context (or `$ARGUMENTS` path if given). Be useful, not pedantic.

Not a bug hunt (`/search-related-problem`), perf hunt (`/search-performance-can-improve`), contract smell (`/search-data-smell`), or simplification (`/search-overengineering`) — this hunts **new value**, not fixes.

## Priority: leverage only

Focus on ideas where small effort meets real payoff:

- Workflow gaps — repeated manual steps that could be one action
- Adjacent features — something already built is one small step from much more useful
- Friction on a common path — dead ends, empty states, missing feedback or confirmation
- Unused data — already collected or stored, could power something users want
- Missing guardrails — mistakes that already happened, where a cheap check prevents the next one
- "Export to Excel" moments — users doing work outside the product that belongs inside

**Do not** chase moonshots, rewrites, new-infrastructure bets, or "wouldn't it be cool if" ideas with no anchor in how the product is actually used.

Prefer: hot user paths, newest features, places users already go, capabilities that exist but are underused.

## Method

### 1. Context first

Write one sentence: *what this area does, who uses it, and what "valuable" means here*.

Jump to that area's main flow — not the whole folder tree.

### 2. Follow one real journey

Trace one concrete user flow end-to-end:

`intent → action → feedback → result → next step`

Pause at friction, waiting, manual work, and dead ends.

### 3. Leverage checks on the skim

Prioritize: repeated steps, underused data, adjacent capabilities, error/empty states, workarounds users likely have — only on this path.

### 4. 3-pass skim (keep short)

1. **Shape** — what exists today  
2. **Gaps** — what's missing, annoying, or manual  
3. **Candidates** — 2–3 ideas; pick the one with the best impact-to-effort ratio  

Stop when you have one defensible idea with evidence.

### 5. Sanity check

1. Who benefits, and how often do they hit this?
2. What's the smallest version that delivers the value?
3. Does it build on what exists, or demand new infrastructure?
4. Why hasn't it been done already — is there a real constraint?

## Output

1. **Context** — one sentence  
2. **Idea** — what to build or change, where (file/symbol/flow), why it's worth it  
3. **Class** — workflow-gap | adjacent-feature | friction | unused-data | guardrail | workaround  
4. **Evidence** — what in the code/product supports this (real paths, not vibes)  
5. **Impact × Effort** — who benefits + rough size (`S` / `M` / `L`)  
6. **First step** — smallest concrete move to try it  
7. **Ask** — whether the user wants it explored or built  

If nothing solid turns up, say so briefly and name the next best place to look — do not invent a weak "wouldn't it be cool" idea.
