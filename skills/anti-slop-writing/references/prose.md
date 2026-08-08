# General prose (reports, docs, analyses)

Use when writing or refining longer Bahasa Indonesia: reports, technical docs narrative, canvas-markdown analyses, research summaries, meeting notes turned into prose — not button-length UI.

Adapted from [adenaufal/anti-slop-writing](https://github.com/adenaufal/anti-slop-writing) Indonesian v3 (structure + BI rules). Still obey shared banlist and **zero em/en dashes**.

## Before writing

1. Lock **register** (formal ringan / semi-formal / light casual) — default semi-formal.
2. Lock **audience** (client, internal eng, public).
3. Lead with the **finding or decision**, not a time-frame opener.

## Do

- **Specific facts** — names, dates, numbers, what changed for whom.
- **Burstiness** — mix short (3–7 words) and longer sentences; never 3+ sentences in a row with nearly the same length.
- **Vary openers** — if many sentences start with the same pattern (`Hal ini…`, `Selain itu…`, `Ini…`), rewrite.
- **Break four-part DNA** — AI loves claim → expand → contrast → resolve. Open on the complication, end on a hard fact, or put the conclusion first at least twice per piece.
- **One-sentence paragraphs** OK for emphasis; avoid metronome 3–4 sentence blocks every time.
- **Repeat the right word** for clarity — don’t cycle synonyms (elegant variation).
- Light discourse particles in semi-formal (`kan`, `nah`) if they sound natural — never force slang; never `gw`, `lo`, `gue`, `lu`

## Don’t

- Section titled only **Kesimpulan** that restates the body (BI-1). If you conclude, say something new.
- Open with **Di era modern… / Seiring perkembangan zaman… / Dalam konteks X yang semakin Y…** (BI-2).
- End with vague **tantangan dan peluang / prospek masa depan** optimism.
- Stack **bold headers + colon** on every bullet for essays (`**SEO:** …`). Prefer prose; simple lists without bold labels when needed.
- Mechanical **bold on every term**.
- **Anda**-lock in casual pieces — match the register (BI-9).
- Fake burstiness by alternating punchy / long on a rigid seesaw — vary irregularly.

## Changelog vs full report

1. **Unit**
   1. Changelog: bullet, one idea
   2. Report / analysis: paragraphs + optional short lists
2. **Lead**
   1. Changelog: user benefit
   2. Report / analysis: finding / verdict
3. **Structure owner**
   1. Changelog: `/create-changelog` (`commands/create-changelog.md`)
   2. Report / analysis: this file + ask
4. **Voice**
   1. Both: this skill

## Quick self-check (30 seconds)

- [ ] Any `—` or `–`? → remove
- [ ] Any `tidak hanya… tetapi juga` / `merupakan salah satu` / `dapat dilihat bahwa` / empty `memastikan`? → rewrite
- [ ] Symmetric hook (`Banyak orang mengira… Kenyataannya…`)? → cut
- [ ] First sentence of each paragraph: mostly the same shape? → vary
- [ ] Colon-heavy `**Label:**` stacks? → prose or simple list
- [ ] Could a competitor name replace yours and the praise still work? → replace praise with facts
- [ ] Read aloud — memo / ChatGPT? → cut fillers, add one concrete detail

## Cite upstream lite checklist

Condensed source: [indonesian/SKILL-lite.md](https://github.com/adenaufal/anti-slop-writing/blob/main/indonesian/SKILL-lite.md) — adapt; do not paste long-form detector tactics into UI.