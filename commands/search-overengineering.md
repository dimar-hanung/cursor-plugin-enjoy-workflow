---
name: search-overengineering
description: Find one real overengineering / simplification opportunity from conversation context — not a laundry list.
---

Hunt **one** overengineering spot or thing that can be simplified from the current conversation context (or `$ARGUMENTS` path if given). Be useful, not pedantic.

Align with workspace `principles`: readable over clever, less abstraction, low cognitive load.

## Priority: accidental complexity only

Focus on complexity beyond what the **current** problem needs:

- Speculative generality (YAGNI) — built for futures that do not exist yet
- Wrong / premature abstraction — layers that cost more than they clarify
- Pass-through wrappers, one-impl interfaces, factories that only wrap `new`
- Layer cake where each layer only forwards
- Config / extension points that never vary in practice

**Do not** flag essential domain complexity, intentional boundaries (auth, money, external APIs), or abstractions with a clear second use / test seam.

Prefer: newest code, densest happy path, most hops for one small behavior, unused “flexibility.”

## Method

### 1. Scope first

Write one sentence: *what area, and what “simple enough” would look like*.

Jump to that path’s entry point — not the whole folder tree.

### 2. Follow the main path

Trace one concrete flow end-to-end. Count mental hops (files, types, wrappers). Accidental complexity = hops that do not clarify the domain.

### 3. Challenge one suspect

Pick the strongest candidate. Ask:

1. How many real variants / implementations **today**?
2. How many call sites?
3. If inlined or removed, what actually breaks?
4. Essential (domain) or accidental (implementation)?

Stop when you have one defensible finding with evidence.

### 4. Breaking flag (required)

Set **Breaking** on that one simplification:

| Signal | Usually |
|--------|---------|
| Public / exported API, HTTP/RPC/event/DB contract, outside callers must change | **Yes** |
| Pure internal inline / delete unused private layer; no exported surface change | **No** |
| Unclear boundary or unknown external callers | **Maybe** |

One-line why. Prefer a non-breaking move when both exist.

## Output

1. **Scope** — one sentence  
2. **Smell** — what’s overengineered, where (file/symbol), why it’s accidental  
3. **Evidence** — call sites, impl count, unused flexibility (not vibes)  
4. **Simplification** — the concrete move (inline, merge, delete layer, hardcode)  
5. **Breaking** — `Yes` | `No` | `Maybe` — one-line why  
6. **Ask** — whether the user wants it simplified  

If nothing solid turns up, say so briefly and name the next best place to look — do not invent a weak finding.
