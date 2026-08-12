---
name: search-performance-can-improve
description: Find one real, likely performance win from conversation context; flag if the fix would be a breaking change.
---

Hunt **one** performance improvement from the current conversation context (or `$ARGUMENTS` path if given). Be useful, not pedantic.

## Priority: likely wins only

Focus on costs that would actually hurt normal use:

- N+1 / repeated queries or fetches in a loop
- Missing index / full scan on a hot path (when evidence points there)
- Over-fetching (wide selects, payloads, or re-renders of large trees)
- Sync work on the critical path that could be deferred, cached, or batched
- Waterfalls (await A then B when A∥B is safe)
- Unbounded work (no pagination, no limit, loading everything into memory)
- Hot path doing expensive work per item that could be once / map / set

**Do not** chase micro-optimizations, premature caching, exotic algorithms, or “what if we get 10M users” fantasies unless the symptom or hot path clearly points there.

Prefer: measured or obvious hot paths, list/detail screens, loops over I/O, request waterfalls, large payloads, repeated identical work.

## Method

### 1. Symptom / hot path first

Write one sentence: *what feels slow (or would), when, and what “fast enough” means*.

Jump to that path’s entry point (handler, click, job, page load) — not the whole folder tree.

### 2. Follow cost, not architecture

Trace one concrete request/flow end-to-end:

`trigger → compute/fetch → transform → store/API → response/UI`

Pause where work multiplies (loops, fans-out, re-renders) or waits in series.

### 3. Cost classes on the skim

Prioritize: I/O in loops, duplicate fetches, missing batch/cache with a clear key, oversized payloads, sync CPU on the critical path, unbounded collections — only on this path.

### 4. 3-pass skim (keep short)

1. **Shape** — names, flow, callers  
2. **Cost** — what runs per request / per item / per render  
3. **Suspects** — 2–3 places that can dominate *this* path  

Stop when you have one falsifiable hypothesis.

### 5. Scientific loop

**Symptom → Scope → Hypothesis → Evidence**

- One hypothesis at a time  
- Predict what must be true if it’s right (e.g. N queries for N items)  
- Point to the smallest check that would prove/disprove it (log, query count, profile, Network tab)  
- Name the class early: query | network | cpu | memory | render | cache | concurrency  

**Don’t tune by reading everything; tune by disproving.**

### 6. Breaking flag (required)

Set **Breaking** on that one fix:

| Signal | Usually |
|--------|---------|
| Public / exported API, HTTP/RPC/event/DB contract, response shape, outside callers must change | **Yes** |
| Pure internal batch/cache/index/defer; same observable results; no exported surface change | **No** |
| Unclear boundary, cache semantics, or unknown external callers | **Maybe** |

One-line why. Prefer a non-breaking move when both exist.

## Output

1. **Hot path** — one sentence  
2. **Bottleneck** — what’s slow/wasteful, where (file/symbol), why it’s likely  
3. **Class** — query / network / cpu / memory / render / cache / concurrency  
4. **Evidence** — what in the code supports this (not speculation)  
5. **Fix** — smallest concrete change (batch, index hint, defer, cache key, parallelize, paginate)  
6. **Breaking** — `Yes` | `No` | `Maybe` — one-line why  
7. **Ask** — whether the user wants it improved  

If nothing solid turns up, say so briefly and name the next best place to look — do not invent a weak micro-optimization.
