# Cognitive Load & Simplicity

Open when a screen feels dense, a settings page overwhelms, or the user must make too many decisions at once. "Simple" = few decisions per moment, not few features.

## Core idea

- **DO** show only what the user needs for the *current* decision. **DON'T** dump the whole product on one screen.
- **DO** progressive disclosure — defer optional/advanced behind "Advanced" or a later moment. **DON'T** hide required steps behind non-obvious affordances (icon-only, hover-only, gestures without hints).
- **DO** split hard questions into several easy ones. **DON'T** make the user calculate, remember, compare, or infer too much in one field.
- **DO** recommend safe defaults and retrieve known data. **NEVER** ask what you can infer.
- **DO** recognition over recall — show options, recent choices, suggestions. **DON'T** make users remember internal names or codes.
- **DO** chunk long forms into stages answerable in ~30s each, with visible progress. **DON'T** split a ≤7-field form into steps for looks.
- **DO** defaults for the 80% case; settings for the 20%. **DON'T** make the obvious behavior require configuration.
- **DO** reuse the same control for the same idea everywhere — "Save" always saves, never sometimes-submits.
- **DO** cut choices before cutting copy — removing two options helps more than removing two sentences.
- **DO** simplify the underlying rule before adding another tooltip or wizard step. **DON'T** polish around a confusing policy.

## Defaults are decisions

Whatever is pre-selected, pre-filled, or pre-checked, you chose for the majority. **DO** choose deliberately. **DON'T** pick the default that benefits the business while surprising the user ("dark pattern defaults").

## Respect attention

Every modal, toast, badge, sound, and vibration withdraws from a finite budget. **DON'T** interrupt for low-stakes actions. **DO** modals only when the decision blocks the next step — never for marketing, never for low-stakes confirm.
