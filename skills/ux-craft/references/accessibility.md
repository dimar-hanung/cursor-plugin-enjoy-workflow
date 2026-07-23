# Accessibility & Inclusive Interaction

Open this file when changing keyboard behavior, focus, touch targets, contrast, labels, motion, or responsive layout. Accessibility is baseline UX, not a mode.

## Contents

- Keyboard & focus
- Labels
- Touch & hover
- Color, motion, responsive
- Inclusion
- Quick checklist

## 1. Keyboard & focus

Every primary task must be completable with Tab, Shift+Tab, Enter, Space, and Escape. No flow should require a mouse.

- Focus order follows decision order.
- Focus indicators stay visible — never remove them for aesthetics.
- Trap focus in modals while open; restore focus to the trigger on close.
- Associate errors with fields programmatically (`aria-describedby`, `aria-invalid`).

## 2. Labels

Names and structure must survive without sight or without hovering.

- Every button has an accessible name — icon-only buttons need visible text or `aria-label`.
- Every field has a persistent label above the input, not placeholder-as-label.
- Link text describes the destination — not "click here".
- Headings describe structure, not just visual size.

## 3. Touch & hover

Touch users do not have hover. Required actions must not live behind hover-only menus.

- Touch targets forgive real fingers — about 44px minimum.
- Extra spacing near destructive actions.
- Visible alternatives to gestures; swipe and long-press can be shortcuts, not the only path.

## 4. Color, motion, responsive

Visual and motion choices must work across devices, lighting conditions, and user preferences — not just on a designer's calibrated monitor.

- All readable UI copy at 16px minimum, including badges, chips, tags, helper text, and table metadata — use `text-base`; secondary text via muted color, not `text-xs`/`text-sm`.
- Meaning never carried by color alone — pair with text, icon, or shape (errors, status chips, charts).
- Honor `prefers-reduced-motion`; motion is not the only carrier of critical information.
- The task survives viewport change — primary action still findable, inputs not covered by sticky bars, keyboard type matches input (`email`, `tel`, `numeric`).
- On small screens, pick card layout or column priority instead of squeezing a desktop table into horizontal-scroll-only mobile (see tables.md).

## 5. Inclusion

Accessibility extends beyond mechanics to who the product assumes the user is — their language, culture, and emotional state when things go wrong.

- Plain language when stakes rise — shame has no place in money, health, or productivity UI.
- No idioms, jokes, or insider metaphors in billing, health, compliance, or error flows.
- Do not assume one country's name, address, phone, date, or currency format.

## 6. Quick checklist

Use this as a final pass whenever interaction behavior, layout, or visual treatment changes.

- [ ] Can every primary task be completed with keyboard only?
- [ ] Is focus order logical and are focus indicators visible?
- [ ] Does every interactive element have an accessible name?
- [ ] Are touch targets at least ~44px?
- [ ] Is meaning available without color alone?
- [ ] Does the layout work on narrow viewports without hiding required actions?
