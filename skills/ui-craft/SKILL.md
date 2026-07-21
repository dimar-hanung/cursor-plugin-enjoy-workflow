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

## Default workflow (create / update / refine UI)

1. **Constraints first** — lock palette (hex), type pair, density, radius scale, motion presets before CSS/JSX. Never rely on "premium" / "modern" alone.
2. **Anti-slop scan** — run the quick reject checklist below; fix stacked tells.
3. **Motion gate** — only animate what survives frequency → purpose → speed → function.
4. **Implement** — property-specific transitions; springs for interruptible gestures; `prefers-reduced-motion`.
5. **Brand test** — without nav/logo, would the first viewport still read as this product?

Open references only when the task needs depth (see [References](#references)).

## Quick reject checklist (visual)

| Tell | Replace with |
| --- | --- |
| Violet↔indigo / purple↔pink hero or CTA gradient | Flat brand hue or real brand gradient |
| Inter / Geist / Poppins / Roboto as sole face | Display + body pair; tracking on large type |
| Exactly 3 equal feature cards | Content-led / asymmetric layout |
| Colored `border-left`/`border-top` on cards | Hairline, space, or semantic alert only |
| Eyebrow pill + emoji above H1 | Specific claim; no sparkle tax |
| `rounded-2xl` + `shadow-md` everywhere | Radius/elevation by intent |
| `transition-all` + fade-in-up on every section | Specific props; purposeful motion |
| Generic CTA / SaaS section template | Product-specific copy and structure |

**Four or more** stacked tells = slop. Fix the combination. Full catalog: [tells-catalog.md](references/tells-catalog.md).

## Hard rules (always)

### Visual

- **MUST** use brand hex tokens; tint neutrals. **NEVER** default purple→indigo / neon glow "premium".
- **MUST** pair characterful display + readable body (or a deliberate single-family scale).
- **Cards:** default **no card**; never cards in hero unless the system requires it.
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
Type: display ___ / body ___
Density: compact | balanced | airy
Radius: sm / md / lg
Motion: hover __ms / panel __ms / easing ___
Do not use: violet-indigo gradients, Inter-only, 3 equal cards, border-left accents, emoji eyebrow pills
```

## Modes

| User intent | Do | Open |
| --- | --- | --- |
| Build / update / refine UI | Follow default workflow; implement | tells-catalog if needed; emil-craft for component recipes |
| De-slop / looks generic | Checklist + review table | [tells-catalog.md](references/tells-catalog.md) |
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
