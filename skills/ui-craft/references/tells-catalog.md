# AI Slop Tells Catalog

Open this when auditing a dense page or when the quick checklist is not enough. A tell is a *default without compensating craft*. One tell ≠ slop; a bundle is.

## Color

| ID | Tell | Why it fires | Prefer |
| --- | --- | --- | --- |
| C1 | Violet↔indigo / blue↔indigo CTA or hero | Training + shadcn/Tailwind demo centroid | Brand primary; flat or one-hue |
| C2 | Purple↔pink (`from-purple-500 to-pink-500`) | Loud generator signature | Drop gradient or brand-justify |
| C3 | Pure `#fff` / `#000` neutrals | Mechanical palette | Tinted off-white / near-black |
| C4 | Primary = `blue-500` / `violet-500` with no tokens | Tailwind scale as brand | Named CSS variables / theme |
| C5 | Neon glow / saturated box-shadow aura | v0/Cursor dark aesthetic | Restraint; meaning-bearing emphasis |
| C6 | Floating gradient orbs behind hero | Decorative atmosphere without product | Real product/context imagery |

## Typography

| ID | Tell | Why it fires | Prefer |
| --- | --- | --- | --- |
| T1 | Inter (or Geist/Poppins/Roboto) only | Ubiquitous starter default | Display + body pair |
| T2 | One weight (~700) everywhere | No hierarchy craft | Weight + size + color scale |
| T3 | Flat line-height / tracking | No optical tuning | Tight display tracking; body ~1.5–1.65 |
| T4 | Missing `text-wrap: balance` on multi-line display | Optional smell | Balance headlines when it helps |

## Layout

| ID | Tell | Why it fires | Prefer |
| --- | --- | --- | --- |
| L1 | Three equal feature cards | Template symmetry | Unequal hierarchy; content-shaped grid |
| L2 | Dead-center everything | Safe composition | Editorial / asymmetric grids |
| L3 | Identical `py-20`/`py-24` every section | Template rhythm | Padding matches section job |
| L4 | `max-w-7xl mx-auto` on all containers | Tailwind example reflex | Deliberate measure (e.g. 65ch prose, 1080 content) |
| L5 | Canonical SaaS section order only | Interchangeable pages | Order that fits the product story |
| L6 | Bento of equal rounded cells, each wanting hero | Dashboard collage on marketing | One focal composition |

## Surfaces & components

| ID | Tell | Why it fires | Prefer |
| --- | --- | --- | --- |
| S1 | Thick `border-left` / `border-top` accent on rounded card | **Strongest stripe tell**; safe hierarchy hack | Hairline all around; space/bg; semantic only |
| S2 | Gray 1px border on every card | Cardocalypse | Space → bg shift → elevation; border last |
| S3 | `rounded-2xl` + `shadow-md` everywhere | One radius/shadow habit | Radius scale; crafted shadow or hairlines |
| S4 | Nested card-in-card | Box-in-a-box chrome | One frame + divide-y / flat list |
| S5 | `backdrop-blur` nav/panels by default | Glassmorphism overuse | Solid high-contrast surfaces; blur when layered |
| S6 | Unmodified shadcn class soup on buttons | Generator fingerprint | Retokenize; simplify class strings |
| S7 | Pill badges (`rounded-full`) as decoration | Chrome noise | Use sparingly; prefer text hierarchy |
| S8 | Terminal mock with 3 dots as empty hero art | Stock generator chrome | Real product UI or omit |

## Motion

| ID | Tell | Why it fires | Prefer |
| --- | --- | --- | --- |
| M1 | `transition-all duration-300 ease-in-out` | Animates unintended layout props | Explicit properties + durations |
| M2 | Fade-in-up on every section | One primitive stamped everywhere | Intentional entrances; often none |
| M3 | Linear stagger (exactly 0.1s each) | Mechanical reveal | Short stagger or none; never block input |
| M4 | Hover only, no `:active` / focus-visible | Incomplete interaction | Full microstates |
| M5 | No `prefers-reduced-motion` | Accessibility miss | Reduce/disable motion when requested |

## Copy & chrome

| ID | Tell | Why it fires | Prefer |
| --- | --- | --- | --- |
| X1 | Eyebrow pill + ✨/🚀/"New: AI-powered…" | Sparkle tax | Specific, dated, or omit |
| X2 | "Get started" / "Learn more" / "Watch demo" only | Microcopy centroid | Outcome-specific CTAs |
| X3 | "Everything you need to…" / "Built for the future of…" | Vague uplift | Concrete claim; pass the competitor swap test |
| X4 | Emoji as icons | Cheap iconography | One icon family, consistent weight |
| X5 | Lucide everywhere with no custom marks | Fine alone; smell with other tells | Brand-aligned icons when craft matters |
| X6 | Testimonials: circular avatars, no metrics | Generic social proof | Named outcomes, before/after, roles |
| X7 | Pricing: Starter/Pro/Enterprise, middle glow | Template commerce | Real packaging |
| X8 | Footer: Product · Company · Resources · Legal | Sitemap filler | Links the product actually needs |
| X9 | How-it-works: exactly 3 numbered steps | Template pedagogy | Real steps; count can be 2/4/5 |

## Severity guide

- **High:** C1–C2, C6, T1+L1 together, S1, X1, M2 on a whole landing page
- **Med:** S2–S5, L2–L5, X2–X8, M1
- **Low / smell:** T4, X5, M3 — OK if color, type, and layout already show craft

## Craft credits (offset defaults)

If the page has real craft, do not over-flag:

- Custom display face + tracking
- Brand palette with tinted neutrals
- Radius hierarchy and deliberate elevation
- Asymmetric or content-led layout
- Specific voice in headlines/CTAs
- Designed hover/focus/active states

Purple + Inter can still score "clean" when these credits are present. Slop is **defaults with nothing compensating**.
