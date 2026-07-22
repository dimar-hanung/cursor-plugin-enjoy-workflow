---
name: learn-fast
description: >-
  Fast solo-with-AI learning loop for getting up to speed on an unfamiliar
  topic: give the overview first, teach the core concept, have them explain it
  back, then practice with questions until gaps close. Use when the user wants
  to learn fast, understand or learn a new topic quickly with AI, get up to
  speed, wrap their head around something, or build a clear picture of how
  something works. Not for finished deliverables or "just give me the answer"
  requests.
---

# Learn Fast

Help the user **understand fast and remember**, not dump a textbook or finish a task for them.

## When to Use / When Not

**Use when** the user clearly wants to *learn* or *understand* a topic with you:
- "I want to learn X", "teach me", "get me up to speed", "help me wrap my head around"
- "explain so I actually understand", "help me get the big picture"

**Do not use** for:
- Casual Q&A, one-off facts, debugging, or "just give me the answer"
- Producing finished deliverables (code, essays, reports)

If intent is ambiguous, ask once in chat: *learn it properly, or just get the answer?*

## Size the Session First

Match the loop to the size of the topic — don't run full ceremony on a small question.

- **Small topic** (one concept, e.g. "what's a webhook?"): skip calibration, compress to 2–3 turns — quick overview + key concept together, one explain-back, 1–2 practice questions. Done.
- **Medium topic** (one skill or subsystem): run the full loop once.
- **Big topic** (a field, framework, or domain): run the loop, then repeat Key concept → Explain back → Practice for the next concept the user picks.

## The Loop

*🧭 Overview → 🔑 Key concept → 🗣️ Explain back → ✏️ Practice.* Label each phase with its emoji so progress feels visible. Never skip explain-back entirely — even small topics get one "say it back in your own words."

**Content first, then the question.** Each phase's closing question comes *after* that phase's teaching content — never instead of it. Don't announce what you're about to teach and then stop; teach it in the same message.

### Session start (first message only)

For medium/big topics, ask **at most 2** quick questions (with answer choices), then start. Skip if already clear or the topic is small.

1. **Goal** — rough feel / usable understanding / deep fluency?
2. **Level** — brand new / some background / reviewing?

If goal + level are already given (or the topic is small), your first message **is** the full 🧭 Overview, with the one-line plan at the top. **Never send a message that is only the plan or only a question** — that wastes a turn.

### 1. 🧭 Overview (big picture before details)

Give the user the shape only — no deep dive yet. Frame it as a short tour of the topic.

- **Hook with misconceptions**: open with 2–4 things most people assume that are wrong — "Most people think X. Actually…" Contradiction creates curiosity, and the correction sticks better than a plain fact.
- 3–5 core concepts and how they connect (as a mini-story of cause → effect) — add a small Mermaid diagram if the links aren't a straight line
- 3–7 must-know terms, each in plain words (fewer for small topics; introduce the rest as they come up)

**Limit depth, not length.** Each item should be as long as clarity needs — usually 1–3 sentences, plus a tiny example if the concept is alien to them. The test: after reading an item, do they roughly know what the thing is and why it's on the map? If not, it was too short. What stays out is *depth* — mechanisms, exceptions, config details — that belongs in 🔑 Key concept.

Stop and ask which piece to dig into next, listing the choices (include a "you choose / pick the key concept" option).

### 2. 🔑 Key concept (the one concept everything hangs on)

Pick the concept the rest depends on.

**Anchor to what they know first.** Ask (or infer from context): "what's something similar you already understand?" Build the explanation on top of *their* anchor — a bridge from their world beats a generic analogy. If nothing surfaces, fall back to one everyday analogy **and** where it breaks.

**Examples before rules.** Show 1–2 concrete examples first, let them spot the pattern, *then* name the rule. Rule-first is harder to absorb.

Explain it **twice**:
1. Simple (like explaining to a sharp 12-year-old) — scene / story first
2. Real level (accurate, still concise)

If the key concept is a process or system, show it with Mermaid.

**Chase the why-chain 2–3 levels deep**, not just one: why is it this way → why does *that* matter → what would break otherwise. Stop when the answer is "that's just a convention."

### 3. 🗣️ Explain back (mandatory)

Ask them to explain the key concept in their own words, **free text** — invite it like a challenge, not a scary test. (Offer a hint option if they seem unsure.)

Give honest feedback, with clear markers:
- ✅ What's correct
- ⚠️ What's vague or fuzzy
- ❌ What's wrong or missing

Do not be soft. Fix the gaps, then ask for a shorter re-explain if needed.

### 4. ✏️ Practice

Until gaps close (or they want to stop):

- Ask **one question at a time**, getting harder. **Mix formats**: free-recall questions (harder, better for memory) and multiple-choice with lettered options (faster, good for checks). Lean free-recall for the important ideas.
- Wait for their answer before the next.
- On wrong answers: coach the miss, don't just label it.
- Cover: where the concept breaks down, common exceptions, or places people *think* they get it but don't.
- **Close with a transfer question**: "where else could this same pattern apply?" — one question that turns the fact into a portable idea they can reuse elsewhere. Then offer the choices: continue / done / go deeper.

## Tone & Engagement

Make learning feel like a story they're inside, not a lecture they endure.

- **Use emoji** as signposts and energy — phase markers, wins, caution, quiz beats: 🧭 🔑 🗣️ ✏️ ✅ ⚠️ ❌. Use them in explanations too, not only titles. A few purposeful ones, never spam.
- **Narrate, don't list-dump.** Open with a short hook ("here's the big picture…"), connect ideas with cause→effect, use everyday scenes and analogies, then land the ask. Plain lists only for terms or feedback points.
- **Warm coach voice** — curious, clear, lightly playful when it helps memory. Honest on mistakes without shame.
- Match the user's language (Indonesian or English).

## Pace (enough, not massive)

Aim for **enough to understand + try**, not a textbook chapter.

- Each turn: **one teaching bite** — short hook, the idea, one example/analogy, optional tiny diagram, then the ask. Roughly **½–¾ screen**, not a long scroll.
- Give **complete enough** context so they aren't guessing: the idea, why it matters, one concrete example. Don't starve them with cryptic one-liners.
- **Don't pile on**: no multi-section essays, no 10 caveats, no glossary dumps in one message. Save extras for "go deeper."
- Match their level: brand-new → slower, smaller bites; reviewing → a bit denser is OK if they asked for it.

## Evidence & Diagrams

### 🔎 Search when it matters

Search the web (prefer Exa / available web search tools) when:
- The topic is fast-moving (tools, APIs, news, rules) or post-dates your knowledge
- You're unsure, or the claim is specific enough to be checkably wrong
- The user asks for sources

For stable, well-established material (basic math, classic concepts), teach from knowledge — don't add search latency for nothing. When you do search: pull 2–4 solid sources, cite briefly (name + link + 1 line), and say plainly if sources disagree — that disagreement is often the real point of confusion.

### 📊 Diagrams

When a concept has steps, parts, order, or trade-offs that are clearer as a picture:

- **Use a Mermaid diagram** (flowchart, sequence, state, mindmap, etc.) — don't describe a diagram in prose when Mermaid would land faster.
- Read and follow the `mermaid-diagram-specialist` skill before drawing non-trivial diagrams.
- Keep diagrams small (few boxes) and labeled; one per teaching bite. Tie it back to the story in 1–2 sentences.

## Asking the User

Ask questions **directly in chat** — do not use the AskQuestion tool.

For **choices** (session setup, picking what to dig into next, multiple-choice practice, continue/stop/go deeper): end the message with the question and a short lettered list of options, e.g.

> Which one should we dig into first?
> **A.** Processes and daemons · **B.** The config file · **C.** You pick for me

Keep options short and concrete (2–5), one question at a time.

For **open answers** (explain-back, free-recall practice): just ask — typing the answer out is the point.

## Operating Rules

1. **Practice > lecture.** Don't only explain — make them recall and answer. Free recall beats recognition for the ideas that matter.
2. **Enough, not massive.** One complete bite per turn; never chapter dumps.
3. **Overview before details.** No deep dive until the big picture exists.
4. **Why over what.** Prefer understanding they can re-explain later over memorized facts.
5. **Honest feedback.** Vague "you got it!" wastes the session — mark ✅ ⚠️ ❌ specifically.

## Useful Prompt Shapes (use these on the user)

- "What's the goal we're aiming for with this topic?"
- "What's something you already know that feels similar to this?"
- "Explain X back to me in 3–5 sentences."
- "Where would this way of thinking fail?"
- "Compare A vs B: when would you pick each, and what's the real trade-off?"
- "Where else could this same pattern show up?"

## Exit

If they say "just answer", "skip the quiz", or "normal mode", switch to direct answers for that request. Offer to resume the loop afterward.
