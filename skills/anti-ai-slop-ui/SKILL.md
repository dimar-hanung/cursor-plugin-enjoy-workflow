---
name: anti-ai-slop-ui
description: >-
  Prevent and remove generic AI-generated UI ("AI slop"): violet/indigo gradients,
  Inter-only type, three equal cards, accent border-left/top stripes, emoji badges,
  shadcn defaults, fade-in-up everywhere, and boilerplate SaaS copy. Use when
  generating, reviewing, refactoring, or polishing UI/landing pages/components;
  when the user mentions AI slop, generic SaaS look, vibe-coded UI, or wants the
  interface to look intentional rather than default.
---

# Anti AI Slop UI Design

You enforce **intentional design over statistical defaults**. AI slop is not broken UI — it is the centroid of training data: functional, forgettable, and instantly recognizable as unguided generation.

**Rule of thumb:** one default can be coincidence. **Four or more** stacked tells = slop. Fix the combination, not a single symptom.

If a project already has a design system, tokens, or brand guidelines — **preserve them**. This skill breaks *defaults*, not established craft.

For motion craft beyond slop removal, prefer `emil-design-eng` / `improve-animations`. For Apple-like interaction physics, prefer `apple-design`.

## When to Use

- Generating new UI, landing pages, dashboards, or marketing sections
- Reviewing agent/v0/Lovable/Bolt output before ship
- User asks to de-slop, de-genericize, Improve UI, or make UI look less AI-made
- Auditing a screen that "looks like every other SaaS site"

## Workflow

1. **Constraints first** — before writing CSS/JSX, lock: palette (hex), type pair, density, radius scale, motion presets. Adjectives like "premium" or "modern" resolve to the centroid; never rely on them alone.
2. **Scan** — run the [Quick reject checklist](#quick-reject-checklist). Count tells.
3. **Replace** — for each hit, apply the paired fix (not a synonym default).
4. **Brand test** — remove the nav/logo in your head: would this first viewport still be recognizable as *this* product? If not, branding and composition are too weak.
5. **Report** (reviews) — use the [Review format](#review-format).

Open [references/tells-catalog.md](references/tells-catalog.md) when you need the full named-tell list or severity notes.

## Quick reject checklist

Fail fast if **any** of these appear without a documented brand reason:

| Tell | Reject / replace with |
| --- | --- |
| Violet↔indigo / blue↔indigo / purple↔pink hero or CTA gradient | Flat brand hue, one-hue wash, or real brand gradient |
| Inter / Geist / Poppins / Roboto as *sole* face, headline→footer | Display + body pairing; optical tracking on large type |
| Exactly 3 equal feature cards (`grid-cols-3`, icon+title+2 lines) | Content-led layout; unequal emphasis; list or 2/4/asymmetric grid |
| Thick colored `border-left` / `border-top` accent on rounded cards | Hairline all-around, space/bg shift, or semantic stripe only for alerts |
| Eyebrow pill + ✨/🚀 above H1 | Specific claim; no sparkle tax |
| `rounded-2xl` + `shadow-md` on every card | Radius scale by size; elevation or hairlines with intent |
| `transition-all duration-300` + fade-in-up on every section | Property-specific transitions; purposeful motion; `prefers-reduced-motion` |
| CTA copy: "Get started" / "Learn more" / "Everything you need to…" | Specific outcomes a competitor name-swap would break |
| 3-tier pricing, middle "Most popular", green checks | Real plans; highlight only if true |
| Nav → Hero → Features → Testimonials → Pricing → FAQ → CTA → Footer, unchanged | Section order and shape that fit *this* product |
| Pure `#fff` / `#000` neutrals, Tailwind blue-500/violet-500 primaries | Tinted neutrals; brand tokens not palette-scale defaults |
| Cards nested in cards; gray 1px border on every block | Prefer space → subtle bg → elevation; border last |

## Hard rules (MUST / NEVER)

### Color

- **MUST** pick a palette from the product/brand (named hex tokens), not from Tailwind's demo scale.
- **MUST** tint neutrals (warm or cool off-white / near-black). Pure `#fff`/`#000` only when brand demands it.
- **NEVER** default to purple-on-white, purple→indigo gradients, or neon glow on dark "because AI looks premium."
- **NEVER** use a decorative colored left/top stripe on cards. Reserve edge accents for true semantic state (error/warning/info).

### Typography

- **MUST** pair a characterful display face with a readable body face (or a deliberate single-family system with a real scale).
- **MUST** vary weight, size, line-height, and tracking across hierarchy (e.g. tighter tracking on large headings).
- **NEVER** set the whole UI in Inter/Geist/system with default tracking and call it done.

### Layout & components

- **MUST** let content dictate structure; prefer asymmetry when hierarchy is unequal.
- **MUST** vary section padding and max-width when sections have different jobs.
- **NEVER** ship the canonical three identical cards as a reflex.
- **NEVER** default every surface to `rounded-2xl shadow-md` / untouched shadcn chrome.
- **Cards:** default to **no card**. Use a bordered/raised container only when it helps interaction or grouping. Never cards in a hero unless the existing system requires it.

### Motion

- **MUST** animate specific properties; match duration to the interaction (hover ~150ms, state ~200–300ms).
- **MUST** respect `prefers-reduced-motion`.
- **NEVER** use `transition-all`.
- **NEVER** apply the same fade-in-up (`opacity` + `translateY(20px)`) to every section.

### Copy & chrome

- **MUST** write headlines and CTAs that name a concrete outcome, audience, or mechanism.
- **NEVER** use emoji as primary icons; use one coherent icon set.
- **NEVER** add "AI-powered" / sparkle badges unless the user explicitly wants that positioning.
- **Swap test:** replace the product name with a competitor's. If the copy still works, rewrite it.

### Composition (marketing / first viewport)

- One composition, not a dashboard collage (unless it *is* a dashboard).
- Brand or product name as a hero-level signal — not only nav text.
- First viewport budget: brand, one headline, one short support line, one CTA group, one dominant visual. No stat strips, schedule snippets, or secondary promos in the hero.
- Prefer a real visual anchor (product, place, context) over abstract gradient blobs.

## Before generation — constraint block

When generating UI from scratch, state constraints explicitly (in the plan or as CSS variables), then implement:

```text
Palette: primary ___ / surface ___ / text ___ / accent ___ (hex)
Type: display ___ @ … / body ___ @ …
Density: compact | balanced | airy
Radius: sm __ / md __ / lg __ (not one value everywhere)
Motion: hover __ms / panel __ms / easing ___
Elevation: hairline | shadow recipe | bg-shift (pick primary separator)
Do not use: violet-indigo gradients, Inter-only, 3 equal cards, border-left accents, emoji eyebrow pills
```

## Review format

When auditing existing UI, output a single markdown table:

| Location | Tell | Severity | Fix |
| --- | --- | --- | --- |
| `Hero.tsx` gradient | House indigo→violet | High | Flat brand `#0A5` CTA; remove blob |
| Features grid | Three identical cards | High | 2 featured + list of secondary |

Severity: **High** (instant fingerprint) · **Med** (common default) · **Low** (smell; OK if craft offsets it).

End with a one-line verdict: `Clean` · `Needs pass` · `Pure slop` (4+ high tells, no compensating craft).

## Exceptions

- **Brand purple is fine** if it is *their* purple with a full system (Stripe-class craft), not `#8b5cf6` + Inter + three cards.
- **Inter is fine** as body (or even UI font) when paired with a real display face, scale, and tracking.
- **shadcn/ui is fine** when tokens, radius, and typography are customized — the tell is *unmodified* defaults.
- **Existing design system wins** over this skill's preferences.

## References

- [tells-catalog.md](references/tells-catalog.md) — full tell list, why each fires, and preferred replacements
