---
name: search-data-smell
description: Find one real bad data contract / shape smell from conversation context; flag if the fix would be a breaking change.
---

Hunt **one** data smell from the current conversation context (or `$ARGUMENTS` path if given). Be useful, not pedantic.

## Priority: contract bugs that bite

Focus on shapes and identities that cause real bugs or silent wrongness:

- Null ambiguity — `null` / missing / empty string / `0` mean different things with no rule
- Stringly typed IDs or enums — IDs as free strings, status as magic strings without a closed set
- Money / quantity as float (or mixed units with no explicit unit)
- Date/time without timezone (or mixing date-only and datetime)
- Same concept, different names or shapes across FE↔BE↔DB (`userId` vs `user_id` vs nested object)
- List vs single item flip at a seam (sometimes array, sometimes object)
- Optional fields that are actually required on a common path (or required fields that are often empty)
- Dual sources of truth for one fact (derived + stored, cache + DB) with no owner

**Do not** chase pure naming taste, speculative schema for futures, or “normalize everything” rewrites unless the hot path clearly hurts.

Prefer: newest seams, API↔DB, FE↔BE, forms→payload, money/dates/IDs, places where shape changes.

## Method

### 1. Seam first

Write one sentence: *which data crosses which boundary, and what “correct shape” should be*.

Jump to that seam (handler, serializer, DTO, model, form submit) — not the whole schema.

### 2. Follow the value

Trace **one** field or identity end-to-end:

`input/UI → validate → transform → store/API → read back → UI`

Pause where type, nullability, units, or cardinality change.

### 3. Contract checks on the skim

Prioritize: null/empty rules, ID identity, enums/status, money/dates/units, list↔item, rename/remap at boundaries — only on this path.

### 4. 3-pass skim (keep short)

1. **Shape** — type, nullability, cardinality  
2. **Meaning** — what each sentinel means (`null` vs `""` vs absent)  
3. **Suspects** — 2–3 places this contract can lie  

Stop when you have one defensible smell with evidence.

### 5. Breaking flag (required)

Set **Breaking** on that one fix:

| Signal | Usually |
|--------|---------|
| DB column/type, API/JSON/event shape, serialized format, outside callers must change | **Yes** |
| Pure internal parse/normalize with same external contract | **No** |
| Unclear producers/consumers or dual clients | **Maybe** |

One-line why. Prefer a non-breaking move (validate/normalize at the edge) when both exist.

If the fix involves table/column structure and the user asks to explain it, follow the workspace table-structure diagram rule (column-level Mermaid).

## Output

1. **Seam** — one sentence  
2. **Smell** — what’s wrong with the data contract, where (file/symbol/field), why it hurts  
3. **Class** — null | identity | enum | money/units | datetime | cardinality | dual-truth | reshape  
4. **Evidence** — what in the code/types/payloads supports this (not speculation)  
5. **Fix** — smallest concrete contract fix (type, validate, normalize, rename at boundary, single owner)  
6. **Breaking** — `Yes` | `No` | `Maybe` — one-line why  
7. **Ask** — whether the user wants it fixed  

If nothing solid turns up, say so briefly and name the next best seam to look — do not invent a weak naming nit.
