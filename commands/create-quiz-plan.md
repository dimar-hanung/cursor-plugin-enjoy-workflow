---
name: create-quiz-plan
description: Turn the current plan or implementation into an interactive comprehension quiz.
---

# Create Quiz Plan

Turn the current plan or implementation into an interactive quiz so you can verify you actually understand what you are building — not just what the agent wrote.

## Core Mission

Quiz the user on the plan, architecture, and implementation details. The goal is comprehension, not gotchas. If they miss something, explain it clearly and tie it back to the real code or plan.

## Step 1: Gather Context First

Before asking anything, understand what "the plan" refers to:

1. **Conversation context** — plans, decisions, or summaries from this chat
2. **Plan artifacts** — look for plan files, specs, todos, or design notes in the workspace
3. **What was built** — read relevant code, migrations, tests, and config if implementation already exists

Summarize in 2–4 sentences what you will quiz on (feature name, main components, key decisions). If the scope is unclear, ask one short clarifying question before starting the quiz.

## Step 2: Build the Quiz

Create **5–8 questions** that test real understanding:

| Category | What to test |
|----------|--------------|
| **Purpose** | Why this exists and what problem it solves |
| **Architecture** | Main components, how they connect, data flow |
| **Decisions** | Trade-offs, why approach A over B |
| **Details** | Models, endpoints, states, permissions, edge cases |
| **Gaps** | What is not built yet, risks, or assumptions |

Mix difficulty: some recall, some "what happens if…?", some "why did we choose…?"

Avoid trivia (exact line numbers, variable names unless they matter). Prefer questions that would matter when debugging or extending the feature.

## Step 3: Use AskQuestion

**You must use the `AskQuestion` tool** to deliver the quiz interactively.

- Present **all questions at once** in a single `AskQuestion` form (one question per item in the `questions` array)
- Use **multiple choice** when there are clear options; use **open-ended** prompts when reasoning matters
Do not split the quiz across multiple `AskQuestion` calls or drip questions one by one. Deliver the full quiz in one form.

## Step 4: Review Each Answer, Then Scorecard

After the user submits, review **every answer** in order. Take the time needed — do not compress into a quick summary. For each question:

- Restate their answer and verdict: correct, partially correct, or wrong
- **What is true** — credit anything they got right, even on a mostly wrong answer
- **What is wrong** — gaps, misconceptions, or hand-waving; be blunt, no false applause
- **More context** — what they should know to really understand it; tie back to the plan, architecture, or specific files (e.g. "See `apps/foo/views.py` — the status transitions happen in…")

Then close with a scorecard:

1. **Score** — honest count only, e.g. "4/8". No softening, no participation trophies.
2. **Strong area** — what you actually nailed. Skip if there is little to praise.
3. **Weak area** — patterns you missed or hand-waved across the quiz. Roast the gaps bluntly and point to the plan or code to fix each hole.
4. **One-liner** — a single sentence describing what you built, in your own words (ask the user to say it; refine if needed)


## Rules

- Quiz on what was **actually** planned or built — do not invent requirements
- If implementation diverged from the plan, quiz on what exists and note the drift
- Keep explanations concise; link to code or plan sections when helpful
- Do not write or implement new code unless the user asks — this command is for learning and verification only
