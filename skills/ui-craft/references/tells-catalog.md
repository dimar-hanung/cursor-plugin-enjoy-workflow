# AI Slop Tells Catalog

Open this file when generating, auditing, or de-slopping UI — landing pages, dashboards, marketing sites, or any surface that might regress to training-data defaults.

A tell is a *default without compensating craft*. One tell ≠ slop; a bundle is. Root cause: slop is the absence of a decision — with no direction the model emits the statistical average, and every unprompted page emits the same average. "Clean / modern / premium" is not a direction.

Use per generation-loop moment:

1. **Before generating** — lock the Decide-first decisions.
2. **While generating** — the never-emit patterns below are stop signals; about to emit one without a decision → stop and decide.
3. **After / auditing** — grep the fingerprints, score severity, run the de-slop pass.

**Every new generation regresses to defaults** — re-apply constraints (constraint block / theme tokens) on every edit, not just the first.

## Contents

- Decide first
- Color
- Typography
- Layout
- Surfaces & components
- Motion
- Copy & chrome
- Greppable fingerprints
- Severity guide
- De-slop pass
- Craft credits

## 1. Decide first

Skip a decision and you will emit its default. Lock each choice before writing CSS or JSX.

- **LOCK the palette** (hex; dominant + neutral + accent) — or you emit blue/indigo 200–290°, Tailwind scale, pure `#fff`/`#000`
- **LOCK light/dark stance** — or you emit dark-by-default + neon glow
- **LOCK type pair + scale** — or you emit Inter-only, weight 700, default ladder
- **LOCK layout stance** — or you emit centered stack, `max-w-7xl`, three equal cards
- **LOCK section order as the product's argument** — or you emit the canonical SaaS order
- **LOCK hover/motion recipe per element role** — or you emit `transition-all` + fade-up + `hover:scale-105` everywhere
- **LOCK voice (buyer + outcome)** — or you emit mad-lib headlines, "Get started", sparkle eyebrows

## 2. Color

Color is the fastest fingerprint — unconstrained generation clusters in the same hue band and the same flat neutrals.

- Flat brand primary; hue outside the ~200–290° band unless brand-owned — not violet↔indigo / blue↔indigo hero or CTA
- Drop purple↔pink gradients (`from-purple-500 to-pink-500`) or brand-justify them explicitly
- Tinted neutrals: off-white, near-black, hued neutral ramp — not pure `#fff`/`#000` or raw `gray-50`/`slate-50`
- Named CSS variables / theme tokens — not `blue-500`/`violet-500` as the brand with no tokens
- Restrained emphasis; saturated shadow auras and neon glow only when they carry meaning
- Real product or context imagery — not floating gradient orbs behind the hero
- ~60/30/10 dominant + neutral + accent; extend via tints/shades, never new hues — not a shallow flat palette with no structure
- Dark mode only when brand-justified, with a designed dark palette — not dark-by-default with neon-on-dark and glowing card borders
- Brand accent on actions, selection, and focus; tinted borders (`border-{accent}-200/300`) or surface shift for panel edges — "clean" is not colorless all-neutrals soup

## 3. Typography

Type defaults read as "template" before the user reads a word — the face, weight ladder, and size scale must be deliberate.

- Characterful display paired with readable body — not Inter/Geist/Poppins/Roboto/DM Sans/Montserrat as the sole face
- Deliberate weight + size + color scale on a chosen ratio — not one weight (~700) and the default ladder (h1 3rem / body 1rem)
- Tightened display tracking; body line-height ~1.5–1.65 — not flat line-height/tracking everywhere
- `text-wrap: balance` on multi-line display when it helps
- One all-caps micro-label only where hierarchy needs it — not stamped above every section heading
- Monospace reserved for actual code/data — not decorative "hacker vibe"
- Commit to a real pairing — not one serif-italic accent word dropped into a sans headline
- All readable UI copy at ≥16px, including badges, chips, tags, helper text, and table metadata — `text-base` or omit size class; hierarchy via `text-lg`/`text-xl` up or muted color, not `text-xs`/`text-sm`/`text-[11–14px]`

## 4. Layout

Layout tells reveal whether the page was composed for this product or copied from the average SaaS landing page.

- Unequal hierarchy; content-shaped grid — not three equal feature cards
- Editorial / asymmetric grids — not dead-center everything
- Padding matched to each section's job — not identical `py-20`/`py-24` on every section
- Deliberate measure (65ch prose, 1080 content) — not `max-w-7xl mx-auto` on all containers
- Section order that argues *this* product's case — not the canonical SaaS order (hero → logos → features → testimonials → pricing → CTA)
- One focal composition — not bentos of equal rounded cells
- Real, load-bearing stats only; one strong number beats a reflex stat banner
- Gaps sized to content; 1–2px nudges where the eye demands — not every gap locked to `gap-6`/`gap-8` on a strict 4px grid

## 5. Surfaces & components

Surface defaults stack into "cardocalypse" — boxes inside boxes, gray borders everywhere, radius and shadow applied uniformly.

- Tables and cards need a visible hue or value shift from the page background; add a restrained hairline or elevation when color contrast alone does not establish the boundary
- Input, select, and textarea fills need a visible hue or value shift from their surrounding surface; borders reinforce the boundary instead of carrying it alone
- Resting, focus, error, and disabled field states remain distinguishable without making focus the only moment an input becomes visible
- Regions meant to blend into the page should use an open layout instead of card styling
- Hairline all around, space/bg shift; color strips for semantic state only — not colored `border-left`/`border-top` on cards
- Separate by space → bg shift → elevation; one intentional boundary border last — not border every card in flat gray 1px
- Radius scale by role; crafted shadow or hairlines — not `rounded-2xl` + `shadow-md` everywhere
- One outer frame; hairline dividers (`divide-y`, `border-b`, `Separator`) between rows — not nested card/box inside card/box
- Solid surfaces; blur only when layers demand it — not default nav/panels with `backdrop-blur`
- Retokenized, simplified class strings — not unmodified shadcn class soup
- Badges sparingly; text hierarchy first — not scattered pill badges as decoration
- Real output or omit — not a terminal mock with 3 traffic-light dots as empty hero art
- Static contrast on pricing tiers: weight, offset, structure — not `animate-pulse`/glow on the "popular" tier
- Meaning-bearing icons, inline marks, or none — not a big rounded Lucide icon centered above every feature heading
- Real product UI or a typographic hero — not 3D blobs, plastic AI illustrations, or generic stock

## 6. Motion

Motion tells are loud because they repeat on every interaction — blanket transitions signal that no element role was decided.

- Explicit properties + durations — not `transition-all duration-300 ease-in-out`
- Intentional entrances; often none — not fade-in-up on every section
- Short stagger or none; never block input — not linear-stagger at exactly 0.1s each
- Full microstates: `:active`, `:focus-visible` — not hover-only styling
- Reduce or disable when `prefers-reduced-motion` is requested
- Hover per element role; a 1px lift is often enough — not `hover:scale-105` + shadow on every card
- Hero static above the fold; save entrances for state changes below — not fade/slide the hero in on load

## 7. Copy & chrome

Copy defaults are interchangeable — if swapping the competitor name still works, the headline was never written for this product.

- Specific, dated eyebrows, or omit — not ✨/🚀/"New: AI-powered…" pills above the H1
- Outcome-specific CTA verbs — not "Get started" / "Learn more" as the only CTAs
- Concrete claim that fails the competitor swap test — not "Everything you need to…" or mad-lib "The AI-powered [X] for modern [Y]"
- One icon family, consistent weight — not emoji as icons
- Brand-aligned icons when craft matters — not Lucide everywhere with no custom marks
- Named outcomes and roles; one strong quote beats a carousel — not circle avatars, five stars, no metrics
- Real packaging; two tiers is often honest — not Starter/Pro/Enterprise with a glowing middle
- Link only what the product needs — not a footer stuffed with Product · Company · Resources · Legal
- Real steps; count can be 2/4/5 — not exactly 3 numbered how-it-works steps
- Plain verbs; say what happens — not "Effortlessly" / "Seamlessly" / "Streamline" / "Unlock" / "Supercharge"

## 8. Greppable fingerprints

Scan first when auditing. A hit is a lead, not a verdict — check for compensating craft before flagging.

Auto-fix on any hit:

- `transition-all`
- `border-l-4|border-t-4`
- nested `Card`/`rounded-* shadow` inside another
- `text-xs|text-sm|text-\[1[0-4]px\]` on body/UI copy
- copy `Effortlessly|Seamlessly|Streamline|Supercharge|Unlock the power`

Tell when uniform/everywhere:

- `rounded-2xl`
- `backdrop-blur`
- `max-w-7xl`
- `grid-cols-3`
- `hover:scale-105`
- `py-20|py-24`
- fonts `Inter|Geist|Poppins|Roboto|DM Sans|Montserrat`

Context-check:

- `from-(blue|indigo|violet|purple)-\d+`
- `animate-pulse` outside loading
- `Get started|Learn more` as only CTAs

Absence is the tell:

- `prefers-reduced-motion`
- `focus-visible` styling

## 9. Severity guide

Not all tells weigh equally — a bundle of high-severity defaults is slop even when low-severity smells are present.

- **High:** cliché gradients or hero art; unasked neon dark mode; generic typography paired with equal-card layouts; colored edge strips; nested cards; animated pricing emphasis; generic AI imagery; emoji eyebrows; page-wide fade-up motion
- **Medium:** shallow palettes; colorless hierarchy; uniform cards, blur, icons, or spacing; undersized body copy; generic section order, CTAs, testimonials, pricing, footers, and motion recipes
- **Low / smell:** isolated type flourishes, optical spacing, icon-family choices, or short stagger patterns — acceptable when the overall color, type, and composition show deliberate craft

## 10. De-slop pass (order matters)

Re-rolling the whole page produces a different average page, not a better one. Keep what works; fix section by section.

1. **Promise** — headline = one outcome for a specific buyer
2. **Hero shape** — off-center, real product, no blob/eyebrow
3. **Theme** — 2–3 real hexes, tinted neutrals, hue outside 200–290°
4. **Type** — display + body pair, per-level tracking/line-height
5. **Symmetry** — content-shaped layout, varied padding, reordered sections
6. **Motion** — strip `transition-all` and blanket fade-ups

Then re-audit. The signature is the combination — removing Inter or the gradient alone saves nothing.

## 11. Craft credits (offset defaults)

Presence of these offsets defaults — do not over-flag when they are present; absence alongside tells confirms nothing was decided.

- Custom display face + tracking; brand palette with tinted neutrals **and a committed accent in use**
- Accent on CTA/active/focus; panel boundaries via tinted border or surface shift — not colorless gray soup
- Radius hierarchy, deliberate elevation, asymmetric/content-led layout
- Specific voice in headlines/CTAs
- Designed states: hover, `:active`, `:focus-visible`, disabled, loading, empty
- Styled `::selection`; dark palette designed separately (not inverted); 1–2px optical nudges

Purple + Inter can still score "clean" with these credits. Slop is **defaults with nothing compensating**.
