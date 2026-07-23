# Forms, Inputs, Validation

Open when building or reviewing any form, from login to multi-step checkout.

## Fields

- **DO** ask the minimum. Every field must be used by the product now. **NEVER** ask what you can infer (country from phone code, city from postal code) or fetch later.
- **DO** single column. **DON'T** place fields side by side except tightly-coupled pairs (first/last name, month/year).
- **DO** label above the input, always visible. **NEVER** placeholder-as-label — it vanishes on focus and kills recall.
- **DO** use placeholder only for format examples ("name@company.com"), helper text below for rules that matter before typing.
- **DO** mark **optional** fields, not required ones (most fields should be required — if not, cut them).
- **DO** group related fields with headings; order easy → hard (name before payment).
- **DO** size inputs to expected content — a postal-code field shouldn't be full width.

## Input behavior

- **DO** match input type to data: `type="email"`, `inputmode="numeric"`, `type="tel"` — right mobile keyboard for each.
- **DO** set `autocomplete` attributes (name, email, address, cc-number); autofill is the fastest form.
- **DO** auto-format as the user types (card number spacing, phone grouping) and accept any paste — strip spaces/dashes yourself.
- **DO** trim whitespace; **DON'T** fail validation on a trailing space.
- **DO** autofocus the first field on dedicated form pages; **DON'T** autofocus inside long content pages.
- **DON'T** use dropdowns for <5 known options (radio/segmented) or for free-text-sized sets (combobox with search).

## Validation

- **DO** validate a field on blur after first interaction; re-validate on keystroke only once it's in error (reward fixing instantly).
- **DO** prevent before validate, validate before submit — catch issues at the earliest step.
- **NEVER** flag untouched fields while the user is still working.
- **DON'T** disable the submit button as validation. **DO** allow submit, then show an error summary at top + inline errors, and move focus to the first error.
- **DO** write errors as what's wrong + how to fix: "Card number is 15 digits — Amex cards start with 34 or 37" (see writing.md for tone).
- **NEVER** clear or reset fields on a failed submit. All input survives errors, back navigation, and accidental refresh where feasible.
- **DO** validate on the server too and map server errors back to fields, not a generic banner.

## Submission

- **DO** show progress on the button itself ("Saving…"), disable during flight, keep the label's verb.
- **DO** make success unmistakable: navigate or confirm what happened ("Invoice sent") — not a silent state change.
- **DO** protect long forms: warn before navigation discards unsaved changes, or autosave drafts.

## Multi-step forms

- **DO** show labeled progress and allow back without loss.
- **DO** persist each completed step server-side or locally.
- **DO** end with a review step for consequential submissions (orders, applications) — editable per section.
