# Structural patterns (UI + prose)

Adapted from [adenaufal/anti-slop-writing](https://github.com/adenaufal/anti-slop-writing) `indonesian/references/structural-patterns.md` + BI rules (v3).

Open when text still feels “template” after a banlist pass. For long reports/docs also open [prose.md](prose.md).

## Kill on every surface

### 1. Em / en dash

Zero `—` or `–` in Indonesian. Use `.` `,` or hyphen `-` for ranges (`10-15`, `2020 sampai 2025`).

### 2. Negative parallelism

`Tidak hanya X, tetapi juga Y` / `Bukan sekadar X, melainkan Y` → one clear claim.

### 3. Rule of three / cadence uniformity

Three equal marketing chips, three parallel benefits, three identical-length bullets = AI tell. Prefer 1–2 specific claims; vary length. In prose, also vary sentence openers (not every line starts with the same pattern).

### 4. Nominalization overload

`Pelaksanaan penyimpanan dilakukan` → `Simpan`. Prefer verbs over noun piles in UI and reports.

### 5. Importance inflation

`merupakan salah satu … terpenting` → evidence, number, or user action.

### 6. False ranges

`Dari pemula hingga ahli` as fluff → cut, or a real scale with a midpoint.

### 7. Participial / tack-on analysis

`…, yang menyoroti pentingnya…` / `…, menggarisbawahi…` → delete or a second short sentence with a fact.

### 8. Challenges pivot

`Di sisi lain terdapat tantangan… Namun dengan upaya yang tepat…` → one concrete problem (+ number) or omit.

### 9. Hook dua klausa (BI-11)

`Banyak orang mengira X. Kenyataannya Y.` → start with finding, benefit, or action.

### 10. Prompt-keyword repetition (BI-12)

Repeating the feature name / slogan every line → say once, then plain language.

### 11. Elegant variation

Cycling synonyms for one concept → one term everywhere.

### 12. Translationese / `di mana` relative

English scaffold or `program di mana peserta…` → direct Indonesian sentences.

### 13. Epistemic padding

`Dapat dilihat bahwa…` / `Perlu dipahami bahwa…` → state the finding.

### 14. Translationese lint (TR — all surfaces)

1. Over-`oleh` passive (`Keputusan dibuat oleh tim`)
   1. Fix: active / pro-drop — `Tim yang buat keputusan`
2. `yang` chains (>2 relatives in one sentence)
   1. Fix: split or restructure
3. Relative `di mana`
   1. Fix: direct clause
4. Over-`adalah`
   1. Fix: drop when Indonesian is clear without it
5. Repeated subject `Anda` / `Kami` every clause
   1. Fix: drop when clear

### 15. Colon density (prose)

Claude-era tell: many `Label: explanation` stacks. In reports, prefer periods or short sentences. In UI labels, a single colon is fine.

## Surface notes

1. **UI**
   1. Particles almost never on buttons; no street slang — never `gw`, `lo`, `gue`, `lu`
   2. Exactly 3 wizard steps is OK when the product needs 3 steps — ban is *equal-length marketing chips*, not real step counts
2. **Changelog**
   1. Benefit-first bullets; structure from `/create-changelog` command
3. **Report / docs**
   1. Apply [prose.md](prose.md): burstiness, no compulsory Kesimpulan, break four-part DNA

## Out of scope for UI microcopy (use in prose only)

Do **not** inject these into buttons, errors, or labels:

- Essay burstiness games, four-part DNA breaking, rhetorical questions mid-string
- Discourse particles / idioms / interjections (`Duh`, `Waduh`, peribahasa)
- Register drift “for authenticity”
- Compulsory anti-detector stylometry tactics

Those belong in [prose.md](prose.md) when writing reports.
