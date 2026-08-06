---
name: search-overengineering
description: Find overengineering and simplification opportunities in scope; flag each finding if the fix would be a breaking change.
---

Hunt **overengineering** and **things that can be simplified** in the current conversation scope (or `$ARGUMENTS` path/module if given). Be useful, not pedantic — report real accidental complexity, not taste disagreements.

Align with workspace `principles`: readable over clever, less abstraction, low cognitive load. Prefer fewer moving parts over more structure.

## Arguments

Parse `$ARGUMENTS` (optional):

| Token | Meaning |
|-------|---------|
| *(path / symbol / “this file”)* | Limit search to that area |
| `--breaking` / `-b` | Only report findings where simplification **would** cause a breaking change (or high risk of one) |
| `--safe` / `-s` | Only report findings that can be simplified **without** breaking changes |

If both `--breaking` and `--safe` appear, prefer `--breaking`. If neither, report both and **always** set the Breaking flag per finding.

## What “overengineering” means here

Complexity beyond what the **current** problem needs:

- Speculative generality (YAGNI) — built for futures that do not exist yet
- Wrong / premature abstraction — layers that hide less than they cost (Sandi Metz: duplication is often cheaper than the wrong abstraction)
- Indirection without payoff — wrappers, factories, interfaces, mappers that only pass through
- Pattern worship — Strategy / Factory / Builder / etc. with no real variability today
- Config theater — knobs that never change in practice
- Layer cake — handler → service → repo where each layer only forwards

**Do not** flag essential domain complexity, intentional boundaries (auth, money, external APIs), or abstractions with clear second use / test seam justification.

## Smell catalog (scan for these)

### Abstraction & indirection

- Interface / abstract type with **one** implementation and no boundary purpose
- Factory / builder that only wraps `new` or builds one shape
- Pass-through wrapper (same signature, no policy / validation / mapping)
- Adjacent layers with the **same** mental model (thin rephrase, not a new level)
- DTO + mapper chains for the same data with no ownership change

### Structure & flow

- Deep nesting (prefer guards / early returns)
- One small behavior change touching many files (builder, mapper, DTO, facade…)
- Boolean parameter flags that fork behavior (`doThing(true, false, true)`)
- Dead code, unused extension points, commented-out “just in case” paths

### Naming / pattern noise

- `Manager` / `Helper` / `Util` / `Handler` / `Processor` with unclear single responsibility
- Design pattern names in types when a plain function would do
- Tests that only assert class structure / deep mocks instead of behavior

Confidence bar: only report findings you would defend with **evidence** (call sites, impl count, unused params). Skip confidence &lt; ~70.

## Method

### 1. Scope

One sentence: *what area, and what “simple enough” would look like for this problem*.

Use conversation context + `$ARGUMENTS`. Do not boil the ocean — prefer newest / densest / hottest path first.

### 2. Main path first

Find the primary user/system flow. Count **mental hops** (files, types, wrappers) a reader needs for one happy path. Accidental complexity shows up as hops that do not clarify the domain.

### 3. Challenge abstractions

For each suspect type / layer / config:

1. How many concrete implementations / real variants exist **today**?
2. How many call sites?
3. If removed or inlined, what breaks?
4. Does it separate concerns or only relocate them?

### 4. Essential vs accidental

Label each finding **essential** (domain) or **accidental** (implementation). Only propose moves for accidental (or for essential complexity that is *hidden* rather than clarified).

### 5. Breaking-change assessment (required)

For every proposed simplification, set **Breaking** using this checklist:

| Signal | Usually Breaking |
|--------|------------------|
| Public / exported API signature or type shape changes | Yes |
| HTTP / RPC / event / DB contract changes | Yes |
| Callers outside the module must change | Yes |
| Serialized formats, URLs, query keys, feature flags consumers rely on | Yes |
| Pure internal inline / delete unused private layer; tests still green; no exported surface change | No |
| Unclear export boundary or unknown external callers | Maybe |

State **why** in one line. Prefer safer internal collapses when both a breaking and a non-breaking move exist — mention both if useful.

## Output

Lead with a one-line verdict: overall, is this area simpler than / equal to / more complex than the problem?

Then a ranked list (max ~7; stop early if thin):

### Finding N — short title

- **Location** — file / symbol (and rough lines if known)
- **Smell** — from catalog (or short label)
- **Evidence** — call sites, impl count, unused flexibility (not vibes)
- **Simplification** — concrete move (inline, merge layer, delete interface, hardcode, flatten)
- **Breaking** — `Yes` | `No` | `Maybe` — one-line why
- **Effort** — trivial / small / medium / large
- **Confidence** — 70–100

If `--breaking` or `--safe` was set, filter the list accordingly and say so in one line at the top.

End with:

1. **Best first move** — highest value / lowest risk (prefer Breaking: No)
2. **Ask** — whether the user wants that move applied (do not refactor unless asked)

If nothing solid turns up, say so briefly — do not invent weak findings.

## Quality bar

- Findings are structural (evidence), not aesthetic preference
- Essential complexity is not “simplified away”
- Breaking flag is always present and honest
- Counterargument once when a design might be justified (test seam, real second variant, stability boundary)
)
