# AI Slop Tells Catalog

A tell is a *default without compensating craft*. One tell ≠ slop; a bundle is. Root cause: slop is the absence of a decision — with no direction the model emits the statistical average, and every unprompted page emits the same average. "Clean / modern / premium" is not a direction.

Use per generation-loop moment:

1. **Before generating** — lock the Decide-first decisions.
2. **While generating** — the DON'Ts below are never-emit patterns; about to emit one without a decision → stop and decide.
3. **After / auditing** — grep the fingerprints, score severity, run the de-slop pass.

**Every new generation regresses to defaults** — re-apply constraints (constraint block / theme tokens) on every edit, not just the first.

## Decide first

Lock each decision before writing CSS/JSX. Skip one and you WILL emit its default:

- **LOCK the palette** (hex; dominant + neutral + accent) — or you emit blue/indigo 200–290°, Tailwind scale, pure `#fff`/`#000` (C1–C4, C7)
- **LOCK light/dark stance** — or you emit dark-by-default + neon glow (C5, C8)
- **LOCK type pair + scale** — or you emit Inter-only, weight 700, default ladder (T1–T3)
- **LOCK layout stance** — or you emit centered stack, `max-w-7xl`, three equal cards (L1–L4, L6)
- **LOCK section order as the product's argument** — or you emit the canonical SaaS order (L5)
- **LOCK hover/motion recipe per element role** — or you emit `transition-all` + fade-up + `hover:scale-105` everywhere (M1–M3, M6–M7)
- **LOCK voice (buyer + outcome)** — or you emit mad-lib headlines, "Get started", sparkle eyebrows (X1–X3, X10)

## Color

- **NEVER** violet↔indigo / blue↔indigo hero or CTA (hue ~200–290°). **DO** flat brand primary; hue outside the band unless brand-owned. (C1)
- **NEVER** purple↔pink gradients (`from-purple-500 to-pink-500`). **DO** drop the gradient or brand-justify it. (C2)
- **DON'T** use pure `#fff`/`#000` or raw `gray-50`/`slate-50` neutrals. **DO** tint: off-white, near-black, hued neutral ramp. (C3)
- **DON'T** make `blue-500`/`violet-500` the brand with no tokens. **DO** name CSS variables / theme tokens. (C4)
- **DON'T** add neon glow / saturated shadow auras. **DO** restrain; emphasis must carry meaning. (C5)
- **DON'T** float gradient orbs behind the hero. **DO** show real product/context imagery. (C6)
- **DON'T** emit a shallow flat palette with no structure. **DO** ~60/30/10 dominant + neutral + accent; extend via tints/shades, never new hues. (C7)
- **DON'T** default to dark mode with neon-on-dark and glowing card borders. **DO** go dark only when brand-justified, with a designed dark palette — never inversion. (C8)

## Typography

- **DON'T** ship Inter/Geist/Poppins/Roboto/DM Sans/Montserrat as the sole face. **DO** pair a characterful display with a readable body. (T1)
- **DON'T** use one weight (~700) and the default ladder (h1 3rem / body 1rem). **DO** build a weight + size + color scale on a deliberate ratio. (T2)
- **DON'T** leave line-height/tracking flat. **DO** tighten display tracking; body ~1.5–1.65. (T3)
- **DO** add `text-wrap: balance` on multi-line display when it helps. (T4)
- **DON'T** stamp an all-caps micro-label above every section heading. **DO** use one only where hierarchy needs it. (T5)
- **DON'T** use monospace decoratively for "hacker vibe". **DO** reserve mono for actual code/data. (T6)
- **DON'T** drop one serif-italic accent word into a sans headline. **DO** commit to a real pairing. (T7)

## Layout

- **DON'T** ship three equal feature cards. **DO** unequal hierarchy; content-shaped grid. (L1)
- **DON'T** dead-center everything. **DO** editorial / asymmetric grids. (L2)
- **DON'T** repeat identical `py-20`/`py-24` on every section. **DO** match padding to the section's job. (L3)
- **DON'T** slap `max-w-7xl mx-auto` on all containers. **DO** pick a deliberate measure (65ch prose, 1080 content). (L4)
- **DON'T** follow the canonical SaaS order (hero → logos → features → testimonials → pricing → CTA). **DO** order sections to argue *this* product's case. (L5)
- **DON'T** build bentos of equal rounded cells. **DO** one focal composition. (L6)
- **DON'T** add a stat banner (3–4 big numbers) by reflex. **DO** show only real, load-bearing stats; one strong number wins. (L7)
- **DON'T** lock every gap to `gap-6`/`gap-8` on a strict 4px grid. **DO** size gaps to content; nudge 1–2px where the eye demands. (L8)

## Surfaces & components

- **NEVER** put a colored `border-left`/`border-top` strip on a card — the strongest stripe tell. **DO** hairline all around, space/bg shift; color strips for semantic state only. (S1)
- **DON'T** border every card in gray 1px ("cardocalypse"). **DO** separate by space → bg shift → elevation; border last. (S2)
- **DON'T** apply `rounded-2xl` + `shadow-md` everywhere. **DO** radius scale by role; crafted shadow or hairlines. (S3)
- **DON'T** nest card-in-card. **DO** one frame + divide-y / flat list. (S4)
- **DON'T** default nav/panels to `backdrop-blur`. **DO** solid surfaces; blur only when layers demand it. (S5)
- **DON'T** ship unmodified shadcn class soup. **DO** retokenize; simplify class strings. (S6)
- **DON'T** scatter pill badges as decoration. **DO** use sparingly; prefer text hierarchy. (S7)
- **DON'T** use a terminal mock with 3 traffic-light dots as empty hero art. **DO** show real output or omit. (S8)
- **DON'T** put `animate-pulse`/glow on the "popular" pricing tier. **DO** static contrast: weight, offset, structure. (S9)
- **DON'T** center a big rounded Lucide icon above every feature heading. **DO** meaning-bearing icons, inline marks, or none. (S10)
- **DON'T** use 3D blobs / plastic AI illustrations / generic stock as hero art. **DO** real product UI or a typographic hero. (S11)

## Motion

- **NEVER** `transition-all duration-300 ease-in-out`. **DO** explicit properties + durations. (M1)
- **DON'T** fade-in-up every section. **DO** intentional entrances; often none. (M2)
- **DON'T** linear-stagger at exactly 0.1s each. **DO** short stagger or none; never block input. (M3)
- **DON'T** style hover only. **DO** full microstates: `:active`, `:focus-visible`. (M4)
- **NEVER** skip `prefers-reduced-motion`. **DO** reduce/disable when requested. (M5)
- **DON'T** put `hover:scale-105` + shadow on every card. **DO** hover per element role; a 1px lift is often enough. (M6)
- **DON'T** fade/slide the hero in above the fold. **DO** keep the hero static; save entrances for state changes below the fold. (M7)

## Copy & chrome

- **DON'T** add an eyebrow pill with ✨/🚀/"New: AI-powered…". **DO** be specific, dated, or omit. (X1)
- **DON'T** use "Get started" / "Learn more" as the only CTAs. **DO** outcome-specific verbs. (X2)
- **DON'T** write "Everything you need to…" or mad-lib "The AI-powered [X] for modern [Y]". **DO** a concrete claim that fails the competitor swap test. (X3)
- **DON'T** use emoji as icons. **DO** one icon family, consistent weight. (X4)
- **DON'T** rely on Lucide everywhere with no custom marks. **DO** brand-aligned icons when craft matters. (X5)
- **DON'T** ship testimonials with circle avatars, five stars, no metrics. **DO** named outcomes and roles; one strong quote beats a carousel. (X6)
- **DON'T** default to Starter/Pro/Enterprise with a glowing middle. **DO** real packaging; two tiers is often honest. (X7)
- **DON'T** fill the footer with Product · Company · Resources · Legal. **DO** link only what the product needs. (X8)
- **DON'T** force exactly 3 numbered how-it-works steps. **DO** real steps; count can be 2/4/5. (X9)
- **NEVER** write "Effortlessly" / "Seamlessly" / "Streamline" / "Unlock" / "Supercharge". **DO** plain verbs; say what happens. (X10)

## Greppable fingerprints

Scan first when auditing; a hit is a lead, not a verdict — check for compensating craft.

- Auto-fix on any hit: `transition-all` (M1) · `border-l-4|border-t-4` (S1) · copy `Effortlessly|Seamlessly|Streamline|Supercharge|Unlock the power` (X10)
- Tell when uniform/everywhere: `rounded-2xl` (S3) · `backdrop-blur` (S5) · `max-w-7xl` (L4) · `grid-cols-3` (L1) · `hover:scale-105` (M6) · `py-20|py-24` (L3) · fonts `Inter|Geist|Poppins|Roboto|DM Sans|Montserrat` (T1)
- Context-check: `from-(blue|indigo|violet|purple)-\d+` (C1/C2) · `animate-pulse` outside loading (S9) · `Get started|Learn more` as only CTAs (X2)
- Absence is the tell: `prefers-reduced-motion` (M5) · `focus-visible` styling (M4)

## Severity guide

- **High:** C1–C2, C6, C8, T1+L1 together, S1, S9, S11, X1, M2 page-wide
- **Med:** C7, S2–S5, S10, L2–L5, L7, X2–X8, X10, M1, M6–M7
- **Low / smell:** T4–T7, L8, X5, M3 — OK if color, type, layout already show craft

## De-slop pass (order matters)

**NEVER** re-roll the whole page — that produces a different average page. Keep what works; fix section by section:

1. **Promise** — headline = one outcome for a specific buyer (kills X1–X3, X10)
2. **Hero shape** — off-center, real product, no blob/eyebrow (kills C6, S11, L2, X1)
3. **Theme** — 2–3 real hexes, tinted neutrals, hue outside 200–290° (kills C1–C4, C7)
4. **Type** — display + body pair, per-level tracking/line-height (kills T1–T3)
5. **Symmetry** — content-shaped layout, varied padding, reordered sections (kills L1–L7)
6. **Motion** — strip `transition-all` and blanket fade-ups (kills M1–M3, M6–M7)

Then re-audit. The signature is the combination — removing Inter or the gradient alone saves nothing.

## Craft credits (offset defaults)

Presence of these = do not over-flag; absence alongside tells confirms nothing was decided:

- Custom display face + tracking; brand palette with tinted neutrals
- Radius hierarchy, deliberate elevation, asymmetric/content-led layout
- Specific voice in headlines/CTAs
- Designed states: hover, `:active`, `:focus-visible`, disabled, loading, empty
- Styled `::selection`; dark palette designed separately (not inverted); 1–2px optical nudges

Purple + Inter can still score "clean" with these credits. Slop is **defaults with nothing compensating**.
