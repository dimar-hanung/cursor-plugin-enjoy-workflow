# Accessibility & Inclusive Interaction

Open when changing keyboard behavior, focus, touch targets, contrast, labels, motion, or responsive layout. Accessibility is baseline UX, not a mode.

## Keyboard & focus

- **DO** complete every primary task with Tab, Shift+Tab, Enter, Space, Escape. **NEVER** ship a flow that requires a mouse.
- **DO** focus order that follows decision order; **NEVER** remove focus indicators for aesthetics.
- **DO** trap focus in modals while open; **DO** restore focus to the trigger on close.
- **DO** associate errors with fields programmatically (`aria-describedby`, `aria-invalid`).

## Labels

- **NEVER** icon-only buttons without accessible names. **DO** persistent labels on every field — not placeholder-as-label.
- **DO** link text that describes destination. **DON'T** "click here".
- **DO** headings that describe structure, not just visual size.

## Touch & hover

- **NEVER** hide required actions behind hover-only menus — touch users don't have hover.
- **DO** touch targets that forgive real fingers (~44px min); **DO** extra spacing near destructive actions.
- **DO** visible alternatives to gestures; swipe/long-press can be shortcuts, not the only path.

## Color, motion, responsive

- **NEVER** carry meaning with color alone — pair with text, icon, or shape (errors, status chips, charts).
- **NEVER** skip `prefers-reduced-motion`; **DON'T** use motion as the only carrier of critical info.
- **DO** make the task survive viewport change — primary action still findable, inputs not covered by sticky bars, keyboard type matches input (`email`, `tel`, `numeric`).
- **DON'T** squeeze a desktop table into horizontal-scroll-only mobile — pick card layout or column priority (see tables.md).

## Inclusion

- **DON'T** idioms, jokes, or insider metaphors in billing, health, compliance, or error flows.
- **DON'T** assume one country's name/address/phone/date/currency format.
- **DO** plain language when stakes rise; shame has no place in money, health, or productivity UI.
