---
name: anti-slop-writing-informal
description: >-
  Default skill for writing or refining Bahasa Indonesia so it sounds
  personal, relaxed, and genuinely human — not AI-generated, not forced gaul.
  Use for UI microcopy, changelogs, reports, docs, personal blogs, essays,
  social captions, community posts, consumer brand voice, and any piece in
  the kamu/aku register. Only switch to anti-slop-writing-formal when a
  formal or semi-formal register is required (gov, bank, legal, academic,
  corporate client).
---

# Anti-Slop Writing — Informal (Bahasa Indonesia)

**Role:** Write or refine casual Bahasa Indonesia that sounds like one specific person talking — santai, konkret, tidak kaku — without drowning it in slang or AI cheerfulness.

**Default untuk semua tulisan Indonesia di plugin ini** — formal hanya saat konteks menuntut.

**Surfaces this skill covers**

1. **UI microcopy** (buttons, errors, empty, labels) — light casual; mechanics + glossary: `anti-slop-writing-formal` §UI microcopy
2. **Changelog / release notes** — light casual, benefit-first; structure: `/create-changelog`
3. **Report / docs / analysis** — casual register; full prose rules: [prose.md](../anti-slop-writing-formal/references/prose.md)
4. **Personal blog / essay / journal** — storytelling, opinion, catatan perjalanan
5. **Social caption / thread** — Instagram, X, LinkedIn santai
6. **Community post** — Discord, Telegram, forum, grup WA
7. **Casual consumer brand voice** — playful empty states, onboarding santai

Formal/semi-formal required (gov, bank, legal, academic, corporate client, laporan resmi) → `anti-slop-writing-formal`. Spoken chat replies → `ux-craft` [writing.md](../ux-craft/references/writing.md) § Bahasa Indonesia (familiar words; no rare KBBI).

**Test:** Read aloud. Sounds like a brochure, a press release, or ChatGPT trying to be relatable → rewrite.

---

## Shared rules (still apply)

1. **Specific beats praise** — facts, moments, numbers; not `seru banget` / `keren` / `berkesan` kosong.
2. **Verbs beat nouns** — `bikin`, `pakai`, `kirim`; not `melakukan pembuatan`.
3. **Zero em/en dash** (`—` `–`) — use `.` `,` or hyphen `-` for ranges.
4. **No template contrast** — drop `tidak hanya… tetapi juga…`.
5. **No translationese** — rewrite English scaffolds (`Secara harfiah…` for "literally", `Aku penasaran apakah…`).
6. **One term per concept** — no synonym cycling to sound varied.
7. **No chat artifacts** — `Semoga membantu!`, `Tentu saja!`, `Sebagai AI…`.
8. **Pronouns stay clean** — default `aku` / `kamu` / omit. `gw` / `lo` only if the user already writes that way or asks for it.

---

## Register (pick once per piece)

Default per surface: product (UI, changelog, brand) → **light casual**; personal (blog, caption, community) → **informal personal**.

1. **Light casual**
   1. Use for: consumer product voice, friendly empty states, brand santai
   2. Pronouns: omit / `kamu`
   3. Particles: at most one softener per string; **never on buttons**
2. **Informal personal**
   1. Use for: blog, caption, community post
   2. Pronouns: `aku` / `kamu` consistent — or omit
   3. Particles OK in prose (`sih`, `kok`, `kan`, `deh`, `dong`) where a person would actually say them

Never mix `kamu` and `Anda` in one piece. Never mix `aku` and `saya`.

---

## Informal slop tells (cut these)

1. **AI cheerfulness** — `Yuk, simak!`, `Penasaran? Baca terus!`, `Selengkapnya di sini!`, `Jangan sampai ketinggalan!`
2. **Fake relatability hooks** — `Siapa nih yang…`, `Anak [X] pasti relate!`, `Kamu tim mana?`
3. **YouTube-script artifacts in text** — `Halo guys, balik lagi di…`, `Oke jadi kali ini kita akan…`
4. **Forced gaul stacking** — `banget`, `literally`, `vibes`, `healing` in every sentence; one loanword per sentence max, and only words people actually say
5. **Particle stuffing** — `sih` / `dong` / `nih` closing every sentence; particles season a sentence, they don't carry it
6. **Calque interjections** — `Secara harfiah…`, `Sejujurnya,` opening every paragraph, `Pada akhir hari` (for "at the end of the day")
7. **Bureaucratic bleed** — `Sekian dari saya`, `semoga bermanfaat`, `demikian` in a casual piece → just end, or end on a concrete note
8. **Emoji / exclamation padding** — `!!!`, emoji every line; one per caption is usually plenty
9. **Template listicle openers** — `Berikut 5 alasan mengapa…` → start with the thing itself
10. **Hedge clusters** — `menurut aku sih sebenarnya mungkin…` → pick a stance
11. **News/AI openers** — `Di era…`, `Seiring…`, `Perlu diketahui bahwa…`, `Berikut adalah…` (swap table: `ux-craft` [writing.md](../ux-craft/references/writing.md) § Bahasa Indonesia)

---

## Rhythm (prose)

- Mix short and long sentences irregularly — 3–7 word punches between longer ones; no metronome.
- Vary openers; not every paragraph starts `Aku…` / `Jadi…`.
- One-sentence paragraph OK for emphasis.
- Repeat the right word; don't cycle synonyms.
- Break the AI essay shape (claim → expand → contrast → resolve) — start mid-story, end on a hard fact.

---

## Examples

1. Bad: Yuk, simak 5 tips produktivitas yang akan mengubah hidupmu! → Good: Lima hal ini bikin aku beres kerjaan sebelum maghrib. Nomor tiga paling susah.
2. Bad: Siapa nih yang suka begadang? Ternyata begadang tidak hanya buruk untuk kesehatan, tetapi juga… → Good: Aku begadang tiap malam selama setahun. Badan yang bayar.
3. Bad: Secara harfiah semua orang pakai aplikasi ini sekarang! → Good: Di kantor, semua pindah ke aplikasi ini dalam seminggu.
4. Bad: Sekian catatan perjalanan saya, semoga bermanfaat! → Good: Besoknya kami balik lagi. Kali ini bawa payung.
5. Bad (casual UI): Ups! Sepertinya ada yang salah nih~ → Good: Tidak bisa disimpan. Coba lagi.
6. Bad: Kopi pagi ini sangat estetik dan memberikan vibes yang positif banget → Good: Kopi pagi ini pahit. Mejanya menghadap jalan. Cukup.

---

## Process

1. **Surface** — blog / caption / community / casual UI.
2. **Voice** — lock pronouns (`aku`/`kamu` or omit); match the user's own samples if given.
3. **Draft** — write like telling a friend; front-load the interesting thing.
4. **Anti-slop pass** — shared rules + informal tells above.
5. **Familiar words** — no rare KBBI; if unsure, search how Indonesians actually say it (not KBBI). See [writing.md](../ux-craft/references/writing.md) § Bahasa Indonesia.
6. **Read aloud** — if you wouldn't say it to a friend without cringing, rewrite.

**Output:** Indonesian text only (written or refined), keep formatting/placeholders/line breaks, unless the user asks for a comparison or rationale.

---

## Post-pass checklist

1. Em/en dash count = **0**
2. No `Yuk simak` / fake hooks / `semoga bermanfaat` closers
3. Particles: seasoning, not stuffing; **zero** on buttons
4. Pronouns consistent (`aku`/`kamu`; no `Anda` drift, no `saya` drift)
5. Slang: only words people actually say; max one per sentence
6. Read aloud — brochure or ChatGPT-relatable? → rewrite

---

## References

- [anti-slop-writing-formal](../anti-slop-writing-formal/SKILL.md) — formal register when required + canonical banlist, UI mechanics, prose rules
- [writing.md](../ux-craft/references/writing.md) — familiar Indonesian words (chat + ID copy); swap table
- [adenaufal/anti-slop-writing](https://github.com/adenaufal/anti-slop-writing) — upstream ID v3
