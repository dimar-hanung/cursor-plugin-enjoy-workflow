---
name: anti-slop-writing-formal
description: >-
  Write or refine formal and semi-formal Bahasa Indonesia so it sounds human,
  clear, and specific — not AI-generated, machine-translated, or bureaucratic.
  Use ONLY when a formal or semi-formal register is required (gov, bank,
  legal, academic, corporate client, laporan resmi) or the user asks for
  formal. Holds the canonical banlist, UI mechanics, and prose rules for all
  registers. Default register in this plugin is informal →
  anti-slop-writing-informal.
---

# Anti-Slop Writing — Formal & Semi-Formal (Bahasa Indonesia)

**Role:** Write or refine Bahasa Indonesia that a real person would send in a professional context — warm enough for the surface, specific, short where space is tight — while keeping established tech terms when forced translation would confuse readers.

**Surfaces this skill covers**

1. **UI microcopy** (buttons, errors, empty, labels)
   1. Register: semi-formal conversational; often omit pronouns
   2. Notes: short; see UX mechanics below + `ux-craft` writing.md (always ID unless user asks EN)
2. **Changelog / release notes**
   1. Register: semi-formal; benefit-first
   2. Notes: structure owned by `/create-changelog` command; **voice** here
3. **Report / analysis / canvas-markdown / docs prose**
   1. Register: semi-formal (or formal ringan if gov/legal)
   2. Notes: full prose rules in [references/prose.md](references/prose.md)
4. **Client / Notion / email brief**
   1. Register: match audience
   2. Notes: same banlist; less slang than personal blog

**Bukan default.** Semua tulisan Indonesia default ke `anti-slop-writing-informal`; buka skill ini hanya saat register formal / semi-formal diperlukan. Skill ini memegang canonical banlist, UI mechanics, dan prose rules yang dipakai semua register. UX writing: `skills/ux-craft/references/writing.md` — always Bahasa Indonesia unless the user asks for English (intent applies; ID voice conflicts → the anti-slop-writing skills win). Chat / spoken replies → `writing.md` § Bahasa Indonesia (familiar words; no rare KBBI). That section still wins on “would a person actually say this word?”

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
9. **No street pronouns** — never `gw`, `lo`, `gue`, `lu`; use omit / `Anda` / `kamu` by register.

---

## Register (pick once per piece)

1. **Formal ringan**
   1. Use for: gov, bank, legal, academic report
   2. Pronouns: `Anda` / impersonal
   3. Particles (`sih`, `dong`, `nih`): none
2. **Semi-formal**
   1. Use for: SaaS UI, changelog, most reports, docs
   2. Pronouns: omit / `kamu` sparingly / `Anda` if brand
   3. Particles: rare; prose may use lightly

Default register plugin ini informal — casual dan personal (light casual consumer voice, aku/kamu blog, social captions) → `anti-slop-writing-informal`.

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
- Never `card` / `kartu` for a UI tile (kanban, dashboard, card view). Name the object (`tugas`, `item`, `catatan`…) or omit. Keep `kartu` only for payment/ID (`kartu kredit`, `nomor kartu`). Flag it if the source uses either.
- Preserve `{{placeholders}}` exactly

Button/error laws in `writing.md` apply as **intent**; UX copy stays Bahasa Indonesia unless the user asks for English.

---

## 2. Voice — changelog & release notes

- Benefit first: `Sekarang bisa…` not `Kami telah menambahkan…` — berlaku untuk **Baru**, **Improvement**, dan bagian "sesudah" di **Perbaikan**
- One idea per bullet; plain words; no stack/jargon
- Section structure → `/create-changelog` (`commands/create-changelog.md`); voice/banlist/dashes → **this skill**
- **Sebelumnya** + **Sekarang** untuk kontras — wajib di Perbaikan, Dihapus, Berubah; boleh di Improvement; Baru utamakan **Sekarang** saja

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
17. UI tile `card` / `kartu` / `tampilan kartu` → name the object or omit; keep `kartu` only for payment/ID

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
6. `Belum ada kartu` / `Tambah kartu` / `Card view` (UI tile)
   1. Prefer: `Belum ada tugas` / `Buat tugas` / `Daftar` or `Grid` — never `card` or `kartu` for the tile

---

## Quick glossary (UI)

Simpan · Batal · Hapus · Ubah/Edit · Pengaturan (not Setelan) · Akun (not rekening) · Masuk · Daftar · Cari · Lanjutkan · Kirim · Kesalahan/Error · Kartu (payment/ID only — never for UI tiles; name the object)

---

## Examples

**UI**

1. Bad: Unggah gagal. Mohon coba lagi. → Good: Upload gagal. Coba lagi.
2. Bad: Apakah Anda ingin menyimpan perubahan Anda? → Good: Simpan perubahan?
3. Bad: Jelajahi fitur kami untuk meningkatkan pengalaman Anda → Good: Lihat fitur
4. Bad: Fitur ini merupakan salah satu inovasi penting yang memfasilitasi optimalisasi kerja Anda → Good: Simpan filter. Dipakai lagi nanti.
5. Bad: Belum ada kartu. Tambah kartu untuk memulai. → Good: Belum ada tugas. Buat tugas pertama.

**Changelog**

6. Bad: Kami telah menambahkan kemampuan untuk mengekspor laporan — Good: Sekarang bisa ekspor laporan ke PDF.
7. Bad: Berbagai perbaikan performa dan pengalaman pengguna — Good: Halaman daftar pelanggan dimuat lebih cepat.

**Report / prose**

8. Bad: Di era digital ini, dapat disimpulkan bahwa transformasi digital memainkan peran krusial… → Good: Tahun lalu 87% tiket masuk lewat aplikasi. Antrean loket turun setengahnya.
9. Bad: …yang menyoroti pentingnya kolaborasi antar pemangku kepentingan. → Good: Tim sales dan finance pakai satu nomor invoice. Dispute turun.

Error frames: `Tidak bisa [aksi]` / `Gagal [aksi]` + next step.

---

## Process

1. **Surface** — UI / changelog / report-docs / other.
2. **Register** — lock pronouns and formality (formal ringan / semi-formal).
3. **Keep vs translate** — mark EN terms readers already know.
4. **Draft** — write or refine; front-load the key word or finding.
5. **Anti-slop pass** — shared rules + quick banlist; open references if still stiff.
6. **Length** — fit the surface (UI tight; prose can breathe but stay concrete); `{{vars}}` exact; **zero** em/en dashes.
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
9. No `card` / `kartu` for UI tiles (name the object or omit)

---

## References

### Local

- [banlist.md](references/banlist.md) — expanded vocab (all formal surfaces)
- [patterns.md](references/patterns.md) — structural / BI tells (UI + prose)
- [prose.md](references/prose.md) — reports, docs, analyses, longer Indonesian
- [anti-slop-writing-informal](../anti-slop-writing-informal/SKILL.md) — casual / personal register (blog, caption, aku/kamu)
- [writing.md](../ux-craft/references/writing.md) — UX writing (always ID unless user asks EN) + familiar words (§ Bahasa Indonesia)

### External

- [adenaufal/anti-slop-writing](https://github.com/adenaufal/anti-slop-writing) — upstream ID v3
- [INA Digital — Penulisan](https://design.inadigital.go.id/foundation/writing/)
- [Special Skill — Prinsip UX Writing](https://specialskill.id/article/2025/03/08/panduan-lengkap-ux-writing-dari-prinsip-dasar-hingga-proses-penulisan/)
- [Microsoft voice](https://learn.microsoft.com/en-us/style-guide/brand-voice-above-all-simple-human) · [Windows writing](https://learn.microsoft.com/en-us/windows/apps/design/style/writing-style) · [ID localization](https://aka.ms/indonesian-styleguide)
- [human-writing ID](https://github.com/syahiidkamil/Software-Engineer-AI-Agent-Atlas/blob/main/.claude/skills/human-writing/languages/id.md)
