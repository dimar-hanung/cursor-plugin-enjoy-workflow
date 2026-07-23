---
name: ui-craft
description: >-
  ALWAYS apply when creating, updating, improving, refining, reviewing, polishing,
  or restyling any UI — components, pages, layouts, CSS/Tailwind, design systems,
  landing pages, or animation/motion. Unified craft: anti-AI-slop visuals, Emil
  motion decisions, Apple gesture physics, animation audit/review, and motion
  vocabulary. Use for any UI/UX visual or interaction work; skip only for pure
  backend/data tasks with no UI surface.
---

# UI Craft

One skill for visual UI and motion. Existing design systems / brand guidelines win over defaults here.

**Why slop happens:** slop is the absence of a decision — an unconstrained ask lands on the training-data average. The cure is committed constraints, not a better adjective ("cleaner" / "more premium" are vibes; vibes don't converge).

**Clean ≠ colorless.** "Clean modern" is not all gray neutrals with no accent. **DO** commit a brand accent on primary actions, active nav, focus, and key highlights. **DO** mark panel/section boundaries with a noticeable but restrained border — e.g. `border-border`, `border-{accent}-200/300`, or a tinted hairline — when the area needs to read as one unit. **DON'T** confuse minimal with mute; **DON'T** border every row in flat gray.

## Default workflow (create / update / refine UI)

1. **Decide first** — lock palette (hex), type pair, density, radius scale, motion presets before CSS/JSX. Every skipped decision becomes a default in the output.
2. **Never-emit** — the quick reject checklist below is patterns not to emit; about to emit one without a decision → stop and decide.
3. **Motion gate** — only animate what survives frequency → purpose → speed → function.
4. **Implement** — property-specific transitions; springs for interruptible gestures; `prefers-reduced-motion`.
5. **Self-check** — re-scan output against the checklist before presenting; every generation regresses to defaults, so re-apply constraints on each edit.
6. **Brand test** — without nav/logo, would the first viewport still read as this product?

Open references only when the task needs depth (see [References](#references)).

## Quick reject checklist (visual)

- **NEVER** violet↔indigo / purple↔pink hero or CTA gradient. **DO** flat brand hue or real brand gradient.
- **DON'T** ship Inter / Geist / Poppins / Roboto as sole face. **DO** display + body pair; tracking on large type.
- **DON'T** ship exactly 3 equal feature cards. **DO** content-led / asymmetric layout.
- **NEVER** colored `border-left`/`border-top` on cards. **DO** hairline, space, or semantic alert only.
- **DON'T** put an eyebrow pill + emoji above the H1. **DO** a specific claim; no sparkle tax.
- **DON'T** apply `rounded-2xl` + `shadow-md` everywhere. **DO** radius/elevation by intent.
- **NEVER** `transition-all` + fade-in-up on every section. **DO** specific props; purposeful motion.
- **DON'T** default to dark mode + neon glow unasked. **DO** dark only when brand-justified, with a designed dark palette.
- **DON'T** put `animate-pulse`/glow on the "popular" pricing tier. **DO** static contrast: weight, offset, structure.
- **NEVER** nest boxes or cards inside boxes or cards. **DO** one outer frame + hairline separators (`divide-y`, `border-b`, `Separator`) between rows/sections.
- **NEVER** body or UI copy below 16px (`text-xs`, `text-sm`, `text-[11–14px]`, inline `font-size`, `size="sm"` on text-heavy UI). **DO** `text-base` (or omit); hierarchy via `text-lg`/`text-xl` up or muted color — not smaller size.
- **DON'T** ship generic CTA / SaaS section templates. **DO** product-specific copy and structure.

**Four or more** stacked tells = slop; the signature is the bundle, so fix the combination. Full catalog + de-slop pass: [tells-catalog.md](references/tells-catalog.md).

## Hard rules (always)

### Visual

- **MUST** use brand hex tokens; tint neutrals. **NEVER** default purple→indigo / neon glow "premium".
- **MUST** use the accent deliberately — primary CTA, active/selected states, links, focus, one focal highlight per viewport; section/panel boundaries via tinted border (`border-{accent}-200/300`) or surface shift when the area must read as a unit.
- **MUST** pair characterful display + readable body (or a deliberate single-family scale).
- **MUST** keep readable UI copy at ≥16px — default `text-base`; secondary via muted color, not `text-xs`/`text-sm`.
- **Cards:** default **no card**; never cards in hero unless the system requires it. **NEVER** nest card/box inside card/box — one frame, separators between items.
- **Composition:** one job per section; first viewport = brand, one headline, one support line, one CTA group, one dominant visual.
- **Copy:** concrete outcomes; swap test (competitor name still works → rewrite).

### Motion

- **MUST** answer why it animates (feedback / spatial / state / jarring bridge / explanation / delight).
- **100+/day or keyboard-initiated** → **no animation**.
- **UI under ~300ms**; enter/exit → `ease-out` (custom curves). **NEVER** `ease-in` on UI. **NEVER** `transition-all`. **NEVER** `scale(0)` — use `scale(0.9–0.97)` + opacity.
- Popovers/menus scale from **trigger** origin; modals stay centered.
- Animate **transform/opacity** only; honor `prefers-reduced-motion` (gentler, not zero feedback).
- Gestures: interruptible springs, velocity handoff, rubber-band edges — see [apple-motion.md](references/apple-motion.md).

### Constraint block (new UI)

```text
Palette: primary ___ / surface ___ / text ___ / accent ___ (hex)
Accent use: CTA + active nav + focus + boundaries (e.g. border-{accent}-300 on panels)
Type: display ___ / body ___
Density: compact | balanced | airy
Radius: sm / md / lg
Motion: hover __ms / panel __ms / easing ___
Do not use: violet-indigo gradients, Inter-only, 3 equal cards, border-left accents, emoji eyebrow pills, unasked dark mode, nested cards/boxes, text below 16px
```

Add one line of rationale per token ("terracotta — physical goods brand"); unexplained tokens drift back to defaults on the next generation.

## Modes

| User intent | Do | Open |
| --- | --- | --- |
| Build / update / refine UI | Follow default workflow; implement | tells-catalog if needed; emil-craft for component recipes |
| De-slop / looks generic | Checklist + review table; run the de-slop pass (never re-roll whole page) | [tells-catalog.md](references/tells-catalog.md) |
| Gesture / sheet / spring / Apple-like feel | Springs, interruptibility, materials | [apple-motion.md](references/apple-motion.md) |
| Deep polish / component feel | Buttons, origins, clip-path, a11y | [emil-craft.md](references/emil-craft.md) |
| "What should animate?" | Gate ruthlessly; max 5–7 ideas; **do not implement** unless asked | [find-opportunities.md](references/find-opportunities.md) |
| Audit / improve motion codebase | Read-only; write plans under `plans/` | [motion-improve.md](references/motion-improve.md), [motion-audit.md](references/motion-audit.md), [motion-plan-template.md](references/motion-plan-template.md) |
| Review motion in a diff | Flag by default; cite standards | [motion-review.md](references/motion-review.md), [motion-standards.md](references/motion-standards.md) |
| "What's that motion called?" | Name only; do not design/build | [vocabulary.md](references/vocabulary.md) |

## Review tables

**Visual audit**

| Location | Tell | Severity | Fix |
| --- | --- | --- | --- |

Verdict: `Clean` · `Needs pass` · `Pure slop`.

**Motion / craft review**

| Before | After | Why |
| --- | --- | --- |

## Exceptions

- Brand purple / Inter-as-body / shadcn are fine when customized into a real system.
- Existing design system **wins**.

## References

- [tells-catalog.md](references/tells-catalog.md) — full AI-slop tells and replacements
- [emil-craft.md](references/emil-craft.md) — Emil component + motion craft detail
- [apple-motion.md](references/apple-motion.md) — Apple fluid UI, springs, gestures, materials
- [find-opportunities.md](references/find-opportunities.md) — find motion opportunities (read-only)
- [motion-improve.md](references/motion-improve.md) — motion audit workflow (read-only)
- [motion-audit.md](references/motion-audit.md) — audit categories and target values
- [motion-plan-template.md](references/motion-plan-template.md) — self-contained motion fix plans
- [motion-review.md](references/motion-review.md) — motion diff review method
- [motion-standards.md](references/motion-standards.md) — precise curves, durations, a11y
- [vocabulary.md](references/vocabulary.md) — name a motion effect
