---
name: anti-slop-writing
description: >-
  Write or refine Bahasa Indonesia so it sounds human — not AI, machine-
  translated, or bureaucratic. Use for product UI microcopy, changelogs,
  reports, docs, analyses, emails, EN→ID localization, or when running
  /refine-ux-writing. Canonical for natural Indonesian product and general
  writing in this plugin.
---

# Anti-Slop Writing (Bahasa Indonesia)

**Role:** Write or refine Bahasa Indonesia that a real person would say or send — warm enough for the surface, specific, short where space is tight — while keeping established tech terms when forced translation would confuse readers.

**Surfaces this skill covers**

1. **UI microcopy** (buttons, errors, empty, labels)
   1. Register: semi-formal conversational; often omit pronouns
   2. Notes: short; see UX mechanics below + `ux-craft` English laws
2. **Changelog / release notes**
   1. Register: semi-formal; benefit-first
   2. Notes: structure owned by `changelog` skill; **voice** here
3. **Report / analysis / canvas-markdown / docs prose**
   1. Register: semi-formal (or formal ringan if gov/legal)
   2. Notes: full prose rules in [references/prose.md](references/prose.md)
4. **Client / Notion / email brief**
   1. Register: match audience
   2. Notes: same banlist; less slang than personal blog

**Canonical for Indonesian wording** on these surfaces. English UX laws: `skills/ux-craft/references/writing.md` (intent applies; ID wording conflicts → **this skill wins**).

**Test:** Read aloud. Sounds like a memo, landing page, or ChatGPT → rewrite.

**Upstream:** Adapted from [adenaufal/anti-slop-writing](https://github.com/adenaufal/anti-slop-writing) Indonesian v3. Open when the quick lists below are not enough:

- Vocab → [references/banlist.md](references/banlist.md)
- Structure / BI tells → [references/patterns.md](references/patterns.md)
- Longer prose (report, docs, analysis) → [references/prose.md](references/prose.md)

---

## Shared rules (every surface)

1. **Specific beats praise** — facts, actions, numbers; not `sangat penting` / `inovatif` / `komprehensif` kosong.
2. **Verbs beat nouns** — `simpan` / `bayar` / `kirim`, not `melakukan penyimpanan` / `pelaksanaan pembayaran`.
3. **Zero em/en dash** (`—` `–`) in Indonesian — use `.` `,` or hyphen `-` for ranges.
4. **No template contrast** — drop `tidak hanya… tetapi juga…`.
5. **No cadence uniformity** — avoid three equal chips / three same-length bullets by default; vary length.
6. **No translationese** — rewrite English scaffolds (`Apakah Anda dapat…`, `Kami telah menambahkan…`).
7. **One term per concept** — no synonym cycling (`proyek` / `workspace` / `ruang kerja` for the same thing).
8. **No chat artifacts** — `Semoga membantu!`, `Baik, berikut adalah…`, `Sebagai AI…`.
9. **No street pronouns** — never `gw`, `lo`, `gue`, `lu`; use omit / `kamu` / `Anda` / `aku` by register.

---

## Register (pick once per piece)

1. **Formal ringan**
   1. Use for: gov, bank, legal, academic report
   2. Pronouns: `Anda` / impersonal
   3. Particles (`sih`, `dong`, `nih`): none
2. **Semi-formal** (default)
   1. Use for: SaaS UI, changelog, most reports, docs
   2. Pronouns: omit / `kamu` sparingly / `Anda` if brand
   3. Particles: rare; prose may use lightly
3. **Light casual**
   1. Use for: consumer social product, friendly empty
   2. Pronouns: omit / `kamu`
   3. Particles: at most one softener
4. **Informal blog**
   1. Use for: only if user asks
   2. Pronouns: `aku` / `kamu` consistently — never `gw`, `lo`, `gue`, `lu`
   3. Particles: OK in prose — **never** on buttons

Never mix `Anda` and `kamu` in the same flow or document section.

---

## 1. Voice — UI microcopy

Default: like helping a neighbor, not filing a surat resmi.

1. Short everyday words (`butuh`, `pilih`, `simpan`, `coba lagi`) — not `mohon` / `dalam rangka`
2. Imperative, active (`Simpan perubahan`) — not “Anda perlu…”
3. Implied subject when clear (`Simpan perubahan?`)
4. Tone scales with stakes (casual routine → neutral money/legal) — no jokes on pay/delete/legal
5. Particles almost never on buttons/labels; bank/gov/legal: none

Align with Microsoft voice adapted for ID: warm, crisp, ready to help. Gov products → InaDigital formal ringan ([INA Digital](https://design.inadigital.go.id/foundation/writing/)).

### UI mechanics

- Indonesian often +15–20% length — cut words, don’t shrink font
- Sentence case for messages; buttons ~2–3 words, verb (+ object); progress keeps verb (`Menyimpan…`)
- Numbers: `1.000` / `5,25` (ID locale); `&` → `dan` unless code/name
- Errors: what happened + how to fix; no blame; no `Oops!`
- Empty: what it is + how to fill + CTA; prefer `Belum ada…` over scolding `Tidak ada…`
- Keep loanwords users know (`email`, `API`, `upload`); don’t invent `surel` / `tembolok`
- Preserve `{placeholders}` exactly

English button/error laws still apply as **intent** via `writing.md`.

---

## 2. Voice — changelog & release notes

- Benefit first: `Sekarang bisa…` not `Kami telah menambahkan…`
- One idea per bullet; plain words; no stack/jargon
- Section structure → `skills/changelog`; voice/banlist/dashes → **this skill**
- Perbaikan: before/after clear without em dashes

---

## 3. Voice — reports, docs, analyses

- Lead with the conclusion or the concrete finding, not `Di era modern…`
- Prefer verbs and specifics over bureaucratic nominalisasi
- Vary sentence length and openers (burstiness) — see [prose.md](references/prose.md)
- Never add a compulsory `## Kesimpulan` that only restates
- Break “four-part sentence DNA” (claim → expand → contrast → resolve) at least twice in a long piece
- Particles OK lightly in semi-formal prose; match tier; don’t force slang

---

## Quick banlist (all surfaces)

1. Journey fluff: `Jelajahi…`, `Mulai perjalanan…`, `Tingkatkan pengalaman…` → name the action
2. Marketing adverbs / calques: seamless, unlock, supercharge, `secara signifikan` kosong
3. `Oops!` / `Mohon maaf atas ketidaknyamanan` → fix path (sorry only if data loss / stuck)
4. `Apakah Anda yakin…` + Ya/Tidak → object + consequence on the control
5. `Terjadi kesalahan` alone → cause + next step
6. `Silakan` / `Mohon` stacked → omit or one invite max
7. `melakukan [noun]`, `dalam rangka`, `dalam upaya`, `guna meningkatkan` → plain verb + `untuk`
8. `tidak hanya… tetapi juga…` → one claim
9. Em/en dash → `.` `,` or `-`
10. Three equal parallel items → 1–2 uneven claims
11. `merupakan salah satu…`, `sangat krusial`, `memfasilitasi`, `mengoptimalkan`, `berperan penting` → concrete outcome
12. `Di era modern…`, `Perlu diketahui…`, `Sebagai kesimpulan…`, `Dapat dilihat bahwa…` → start with the fact
13. Hook `Banyak orang mengira X. Kenyataannya Y.` → lead with finding or action
14. Prompt-keyword spam → say once, then plain language
15. Relative `di mana` calque → rewrite as direct sentences
16. Chat closers: `Semoga membantu!`, `Tentu saja!`

More → [banlist.md](references/banlist.md) · [patterns.md](references/patterns.md)

### Translationese

1. `Apakah Anda dapat…`
   1. Prefer: `Bisa…` / imperative
2. `Kami telah menambahkan…`
   1. Prefer: `Sekarang bisa…`
3. `Format surel tidak valid`
   1. Prefer: `Format email salah`
4. `Kredensial otentikasi`
   1. Prefer: `Email dan kata sandi`
5. `Anda harus memasukkan data yang valid`
   1. Prefer: `Masukkan data yang benar`

---

## Quick glossary (UI)

Simpan · Batal · Hapus · Ubah/Edit · Pengaturan (not Setelan) · Akun (not rekening) · Masuk · Daftar · Cari · Lanjutkan · Kirim · Kesalahan/Error

---

## Examples

**UI**

1. Bad: Unggah gagal. Mohon coba lagi. → Good: Upload gagal. Coba lagi.
2. Bad: Apakah Anda ingin menyimpan perubahan Anda? → Good: Simpan perubahan?
3. Bad: Jelajahi fitur kami untuk meningkatkan pengalaman Anda → Good: Lihat fitur
4. Bad: Fitur ini merupakan salah satu inovasi penting yang memfasilitasi optimalisasi kerja Anda → Good: Simpan filter. Dipakai lagi nanti.

**Changelog**

5. Bad: Kami telah menambahkan kemampuan untuk mengekspor laporan — Good: Sekarang bisa ekspor laporan ke PDF.
6. Bad: Berbagai perbaikan performa dan pengalaman pengguna — Good: Halaman daftar pelanggan dimuat lebih cepat.

**Report / prose**

7. Bad: Di era digital ini, dapat disimpulkan bahwa transformasi digital memainkan peran krusial… → Good: Tahun lalu 87% tiket masuk lewat aplikasi. Antrean loket turun setengahnya.
8. Bad: …yang menyoroti pentingnya kolaborasi antar pemangku kepentingan. → Good: Tim sales dan finance pakai satu nomor invoice. Dispute turun.

Error frames: `Tidak bisa [aksi]` / `Gagal [aksi]` + next step.

---

## Process

1. **Surface** — UI / changelog / report-docs / other.
2. **Register** — lock pronouns and formality.
3. **Keep vs translate** — mark EN terms readers already know.
4. **Draft** — write or refine; front-load the key word or finding.
5. **Anti-slop pass** — shared rules + quick banlist; open references if still stiff.
6. **Length** — fit the surface (UI tight; prose can breathe but stay concrete); `{vars}` exact; **zero** em/en dashes.
7. **Read aloud** — awkward spoken = wrong written.
8. **Consistency** — same term across the piece / neighboring screens.

**Output:** Indonesian text only (written or refined), keep formatting/placeholders/line breaks, unless the user asks for a comparison or rationale.

---

## Post-pass checklist (all surfaces)

1. Em/en dash count = **0**
2. No `Di era` / `Seiring` / `Dalam konteks… yang semakin` openers
3. No `merupakan salah satu` / `tidak hanya… tetapi juga` / `berperan … dalam membentuk` / empty `memastikan`
4. `yang` chains ≤2 per sentence (prose); UI strings: prefer zero nested relatives
5. Pronoun register matches surface (`Anda` vs omit vs `kamu` — never mixed)
6. Length fits surface (UI tight; prose concrete)
7. Placeholders `{…}` unchanged
8. Read aloud — memo / ChatGPT / landing page? → rewrite

---

## References

### Local

- [banlist.md](references/banlist.md) — expanded vocab (all surfaces)
- [patterns.md](references/patterns.md) — structural / BI tells (UI + prose)
- [prose.md](references/prose.md) — reports, docs, analyses, longer Indonesian

### External

- [adenaufal/anti-slop-writing](https://github.com/adenaufal/anti-slop-writing) — upstream ID v3
- [INA Digital — Penulisan](https://design.inadigital.go.id/foundation/writing/)
- [Special Skill — Prinsip UX Writing](https://specialskill.id/article/2025/03/08/panduan-lengkap-ux-writing-dari-prinsip-dasar-hingga-proses-penulisan/)
- [Microsoft voice](https://learn.microsoft.com/en-us/style-guide/brand-voice-above-all-simple-human) · [Windows writing](https://learn.microsoft.com/en-us/windows/apps/design/style/writing-style) · [ID localization](https://aka.ms/indonesian-styleguide)
- [human-writing ID](https://github.com/syahiidkamil/Software-Engineer-AI-Agent-Atlas/blob/main/.claude/skills/human-writing/languages/id.md)
