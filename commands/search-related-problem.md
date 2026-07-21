---
name: search-related-problem
description: Find a real, likely bug from conversation context by skimming the failing path — not obscure edge cases.
---

Hunt **one** related problem or bug from the current conversation context. Be useful, not pedantic.

## Priority: likely bugs only

Focus on defects that would actually break normal use:

- Wrong branch / condition on a common path
- Data shape change at a seam (null↔object, string↔number, list↔item)
- Stale UI/cache after a write
- Swallowed errors / ignored promises
- Wrong identity (`id` vs `slug`, user vs session)
- Permission checked in UI only
- Recent regression (“what changed?”)

**Do not** chase obscure edge cases, rare race fantasies, or “what if the universe flips bits” issues unless the symptom clearly points there.

Prefer: newest code, most complex branch on the failing path, system boundaries, silent failure paths.

## Method

### 1. Symptom first

Write one sentence: *what breaks, when, and what was expected*.

Jump to that path’s entry point (handler, click, job, cron) — not the whole folder tree.

### 2. Follow data, not architecture

Trace one concrete input end-to-end:

`request/event → validation → transform → store/API → response/UI`

Pause where data changes shape.

### 3. Unhappy paths on the skim (common ones)

Prioritize guards, early returns, `catch`/error mapping, empty/null branches, defaults/`else`, retries/timeouts/fallbacks — only where they sit on the failing path.

### 4. Seams

Harder look at API↔DB, FE↔BE, sync↔async, cache↔source of truth, auth, dates/money/units — again only if relevant to the symptom.

### 5. 3-pass skim (keep short)

1. **Shape** — names, flow, callers  
2. **Contracts** — types, “must always…” invariants  
3. **Suspects** — 2–3 places that can produce *this* symptom  

Stop when you have one falsifiable hypothesis.

### 6. Scientific loop

**Symptom → Scope → Hypothesis → Evidence**

- One hypothesis at a time  
- Predict what must be true if it’s right  
- Point to the smallest check that would prove/disprove it  
- Name the bug class early: logic | state | data | integration | env/config | concurrency  

**Don’t debug by reading everything; debug by disproving.**

## Output

1. **Symptom** — one sentence  
2. **Bug** — what’s wrong, where (file/symbol), why it’s likely  
3. **Class** — logic / state / data / integration / env / concurrency  
4. **Repro** — smallest steps (one failing input vs one working if useful)  
5. **Evidence** — what in the code supports this (not speculation)  
6. **Ask** — whether the user wants it fixed  

If nothing solid turns up, say so briefly and name the next best place to look — do not invent a weak edge-case finding.
