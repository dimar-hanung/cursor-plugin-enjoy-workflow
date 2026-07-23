# UX Writing & Microcopy

Open this file when writing or reviewing buttons, labels, errors, confirmations, empty states, banners, toasts, or any user-facing copy.

## Contents

- Buttons
- Errors
- Confirmations & success
- Empty states
- Terminology & tone
- Dates & numbers
- Toasts
- Quick checklist

## 1. Buttons

The button alone must answer "what does clicking this do?"

- Verb + object: "Save changes", "Delete file", "Send invoice".
- Sentence case everywhere (buttons, titles, labels) — not Title Case Every Word or ALL CAPS.
- Keep the verb during progress: "Saving…" not "Loading…".
- Consequential actions name the object on the button — not "Yes", "No", or bare "OK".
- Prefer a specific verb over bare "Submit" or "Continue" when one exists.

## 2. Errors

Calm, specific, blameless. The user should know what happened and how to fix it.

- Three parts when useful: what happened + why + how to fix.
- Never blame the user — "We couldn't find an account with that email," not "You entered an invalid email."
- No "Oops!" or "Something went wrong".
- Raw codes or jargon never stand alone; if a code helps support, append it quietly after the human sentence.
- Put the fix in the message when known ("File must be under 10 MB — this one is 14 MB").
- No exclamation marks, "please", or "sorry" padding. State it plainly.

## 3. Confirmations & success

At the moment of commitment or completion, copy must remove ambiguity about what is about to happen or what just happened.

- Name object + consequence: "Delete 'Q3 report'? This can't be undone." Buttons: "Delete report" / "Cancel" — not "Are you sure?" with Yes/No.
- State scope with numbers: "This removes 3 members from the project."
- Success messages name what happened: "Invoice #204 sent to acme.com" — plus the next action when useful ("View invoice").

## 4. Empty states

Two jobs: what this space is + how to fill it, with the CTA right there.

- Example: "No API keys yet. Create a key to start making requests." + [Create API key]
- Distinguish first-use, no-results, and error — not a lone illustration with "Nothing here!" (see states.md).

## 5. Terminology & tone

Consistent language builds trust; inconsistent language forces the user to translate your product into their mental model on every screen.

- One term per concept, everywhere — pick "project" or "workspace", never both for the same thing. Keep a terms list for the product.
- The user's nouns, not internal names ("Download report", not "Export SSRS artifact").
- Front-load the key word: "Delete account" not "Click here if you would like to delete your account".
- No marketing adverbs in product UI: "Effortlessly", "Seamlessly", "Supercharge", "Unlock". Plain verbs; say what happens.
- Tone scales with stakes — casual for routine, neutral for transactional, formal for irreversible/legal.
- Write copy you would read aloud to a stranger.

## 6. Dates & numbers

How you display time and quantity signals whether the product respects the user's context or was built for one locale and one precision level.

- Locale-aware dates and numbers; never raw ISO in body copy.
- Relative time for recent activity ("2h ago") with absolute on hover; absolute ("12 Mar 2026") for records, invoices, logs.
- Consistent precision per context; round display values, keep exact on hover/export.

## 7. Toasts

Toasts are ephemeral — useful for lightweight confirmation, dangerous for anything the user must act on or remember.

- Lead with the event: "Export finished — report.csv ready" + action ("Download").
- Do not notify what the user is already looking at.
- Errors that need action stay inline — toasts vanish (see states.md).

## 8. Quick checklist

Read every new or changed string aloud before shipping — awkward spoken copy is almost always wrong written copy.

- [ ] Does every button label answer "what does this do?"
- [ ] Do errors say what happened and how to fix it?
- [ ] Do destructive confirms name the object and consequence?
- [ ] Is terminology consistent with one term per concept?
- [ ] Would you read this aloud to a stranger without cringing?
