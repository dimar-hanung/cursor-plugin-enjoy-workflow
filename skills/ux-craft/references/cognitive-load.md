# Cognitive Load & Simplicity

Open this file when designing or reviewing: forms, settings pages, onboarding, dense screens, decision points, default values, anything where the user has to read, choose, or remember.

## Contents

- What "simple" actually means
- Decisions are more taxing than reading
- Hard questions are product work
- Progressive disclosure
- Defaults handle the 80% case
- Chunk long inputs
- Recognition over recall
- Consistency: same control for same idea
- The cost of choices
- Visual hierarchy
- Read order = decision order
- Animation is information
- Respect attention
- Anti-patterns
- Quick checklist

## 1. What "simple" actually means

"Simple" does not mean "few features." It means "few decisions per moment." A product with a thousand features can feel simple if it never asks the user to think about more than one at a time. A product with five features can feel overwhelming if all five are visible at once.

Cognitive load is the mental effort required to operate the interface. Three kinds:

- **Intrinsic** — load inherent to the task (filing taxes is hard; do not blame yourself for that).
- **Extraneous** — load added by the interface (where to click, what this label means, why the button is greyed out).
- **Germane** — load that builds the user's understanding (good onboarding adds germane load on purpose).

The job is to push extraneous load toward zero. Intrinsic load is the user's problem; extraneous load is yours.

## 2. Decisions are more taxing than reading

A common mistake: cutting words to "make it simpler" while leaving the number of choices intact. Cutting one option helps the user more than cutting one sentence.

- Count the choices on each screen. Three or fewer per visible region is the working ceiling.
- A long sentence is one decision (read or skip). A list of seven options is seven decisions.
- Group related options so the user makes a coarse decision first, then a fine one.
- Cut choices before cutting copy — removing two options helps more than removing two sentences.

Hard questions create hidden choices. If the user has to calculate, compare, remember an external fact, or infer what you mean, the interface has handed them product work. Turn one hard question into several easy ones, offer a recommendation, prefill known data, or retrieve the missing information.

Useful test: can a reasonable user answer this within a few seconds without leaving the screen? If not, the problem is not copy length. The question is too hard.

## 3. Hard questions are product work

When a screen feels dense but the copy is already short, the underlying rule is probably too hard. Simplify the policy before adding another tooltip or wizard step. Another screen will not fix a confusing eligibility rule or a product decision the user should not have to make.

- Show only what the user needs for the *current* decision.
- Split hard questions into several easy ones.
- Recommend safe defaults and retrieve known data instead of asking what you can infer.

## 4. Progressive disclosure

Hide complexity in time and space. Show only what is needed *to make the current decision*; reveal the rest when it becomes relevant.

Patterns:

- **Expandable sections** — for optional or advanced settings the majority will ignore.
- **Step-by-step flows** — for tasks with conditional branches (next step depends on previous answer).
- **Contextual reveal** — show the field only when the toggle that requires it is on.
- **Defaults + "Advanced"** — pick sensible defaults; let power users open Advanced to tune.

What progressive disclosure is not: hiding important information behind a click. If the user *needs* the information to decide, hiding it is malpractice. Hide only what the user can safely defer. Required steps must not live behind non-obvious affordances — icon-only controls, hover-only menus, gestures without hints.

## 5. Defaults handle the 80% case

Whatever is pre-selected, pre-filled, or pre-checked is the decision you are making *for* the majority of users.

- Choose defaults the way you would choose a recommendation for a friend.
- Defaults must be *common*, *safe*, and *reversible* — in that order.
- If safety conflicts with commonness (e.g., notifications), prefer safe and let the user opt in.
- Never default to the option that benefits you over the user. That is a dark pattern.
- Defaults for the 80% case; settings for the 20%. The obvious behavior should not require configuration.

A good default is invisible. A bad default surfaces every time the user finishes a task and goes "wait, what was checked?"

## 6. Chunk long inputs

Forms with more than 5 fields should be broken into steps unless the fields are tightly related.

- Each step should be answerable in under 30 seconds.
- Show progress (3 of 5) so the user can pace themselves.
- Allow back-and-forth without losing data.
- Save draft state automatically; do not require explicit "Save draft."

Single long form is appropriate when fields are interdependent (the user needs to see all of them to answer accurately). Stepped form is appropriate when fields are independent. A form with roughly seven or fewer independent fields does not need steps for appearance alone.

## 7. Recognition over recall

Show options instead of asking users to remember and type them. The user's working memory is small (about 4 chunks) and unreliable.

- Autocomplete instead of free text where the set is bounded.
- Recently-used lists for items the user picks repeatedly.
- Previews instead of names where visual identity matters more than text identity (files, photos, projects).
- Inline help text — the rules of the field next to the field, not in a separate help page.

The user should not have to remember anything between screens. Carry context forward.

## 8. Consistency: same control for same idea

Reuse one control for one concept across the product. A user who learns "Save" once should never have to relearn it.

- "Save" always saves. Never sometimes-submits.
- A trash icon always deletes. Never sometimes-archives.
- A primary button is always the action that progresses the flow. Never sometimes-cancels.

Consistency is more important than being clever. A novel pattern that requires re-learning is worse than a familiar pattern that is slightly less elegant.

## 9. The cost of choices

Hick's law: decision time grows with the number of options. But the bigger cost is not time — it is the user *deferring* the decision entirely.

- Recommend a default option visually (highlight, "Recommended" badge).
- Order options by frequency of use, not alphabetically, not by feature parity.
- For long lists (10+), provide filter or category, not pagination.
- For very long lists (50+), provide search as the primary entry, with browse as fallback.

If three options is the right number, do not show four to "give users choice." Choice is a tax.

## 10. Visual hierarchy

Cognitive load is partly a typography problem. If everything looks equally important, the user must read everything to find the important thing.

- One dominant element per visible region. Eye lands on it first.
- Three levels of weight is the working maximum: primary, secondary, tertiary.
- Whitespace is a control, not a void. Use it to group related items and separate unrelated ones.
- Color carries meaning. Use it sparingly — if everything is colored, nothing is.
- One container + hairline separators (`divide-y`, `border-b`) beat nested cards or boxes for grouping related items — nested chrome adds noise without hierarchy.

If you remove color, weight, and size variations, can the user still tell what matters? If not, hierarchy is failing.

## 11. Read order = decision order

Users read in a Z or F pattern in most languages. The order you place things is the order they are considered. Use this:

- Top-left: who/what this screen is about (anchor).
- Top-right: account or context controls (peripheral but findable).
- Middle: primary content and primary action.
- Bottom: secondary actions, footer info.

In Korean, Japanese, and Chinese contexts, scanning patterns are similar but with adjustments for character density. Test with real readers before assuming the same layout works.

## 12. Animation is information

Used right, motion reduces cognitive load by making transitions legible: where did this come from, where did it go.

- Animate to show cause and effect. The clicked button morphs into the panel it opens.
- Keep durations short: 150–250ms for most transitions, 300–400ms for entrances.
- Never animate on every render. Repeated motion becomes noise.
- Provide a "reduce motion" path for vestibular sensitivity. Use `prefers-reduced-motion`.

If a transition does not help the user understand state change, it does not earn its frames.

## 13. Respect attention

Every modal, toast, badge, sound, and vibration withdraws from a finite budget.

- Modals only when the decision blocks the next step — not for marketing, not for low-stakes confirm.
- Low-stakes actions should not interrupt the user's current task.

## 14. The "back of the napkin" test

A trustworthy heuristic: can you sketch this screen on the back of a napkin and have a colleague understand what it does? If the screen is so dense that the napkin sketch loses meaning, the screen is too dense.

Reduce until the napkin works.

## 15. Anti-patterns

These show up often when a screen was designed feature-by-feature instead of decision-by-decision. Each one adds extraneous load without adding capability.

- **Settings sprawl.** A "General" tab with 30 options is not configurable, it is unfindable. Group, hide, default.
- **Filter panels that always show every filter.** Reveal filters by category; let the user expand only what is relevant.
- **Tooltips as a substitute for labels.** A button that needs a tooltip to be understood is a button with the wrong label.
- **Forms that validate every field on first focus.** Validation should happen on blur or on submit, not as the user is typing the first character.
- **"Smart" defaults that change based on context the user cannot see.** Defaults must be predictable. If the system picks differently in different states, the user cannot form a mental model.
- **More than one "primary" call to action.** If you have two primaries, you have two products fighting for the screen.
- **One hard question.** A single field that asks the user to calculate, remember, compare, or infer too much is not simpler than a guided sequence.
- **Nested cards or boxes.** Group related items in one frame with separators, not boxes inside boxes.

## 16. Quick checklist

Run through this list on any screen that feels busy, slow to decide, or frequently abandoned mid-task.

When reviewing for cognitive load:

- [ ] Can the user describe what this screen is for in one sentence?
- [ ] Is the primary decision obvious within 3 seconds of seeing the screen?
- [ ] Can every question be answered within a few seconds without external memory or calculation?
- [ ] Are choices ≤ 3 per visible region (excluding lists with search/filter)?
- [ ] Are defaults common, safe, and reversible?
- [ ] Is hierarchy visible without reading?
- [ ] Does the screen carry context forward — no re-typing, no re-remembering?
- [ ] Is anything visible that the user does not need *right now*?
