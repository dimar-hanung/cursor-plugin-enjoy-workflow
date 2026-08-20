# UX Writing & Microcopy

Open this file when writing or reviewing buttons, labels, errors, confirmations, empty states, banners, toasts, or any user-facing copy — and when the reply itself is in Bahasa Indonesia (chat, explanations, walkthroughs).

## Language

**UX copy is always Bahasa Indonesia** unless the user explicitly asks for English (or the product is already English-only). Do not ship English UI strings by default. Do not mix EN and ID on the same screen.

Chat replies still follow the user: Indonesia if they write/ask Indonesia; English if the entire thread is English. Chat is not UX copy.

| Surface | Language | Canonical source |
|----------|----------|------------------|
| **UI / microcopy** (buttons, errors, empty, confirms, toasts) | **Bahasa Indonesia** (default) | **This file** + `anti-slop-writing-informal` (voice); `anti-slop-writing-formal` when formal |
| **Changelog / docs / reports** | Bahasa Indonesia | Voice: anti-slop (informal default); structure: `/create-changelog` for changelogs |
| **Chat / explanations** | Match the user | This file § Bahasa Indonesia when the reply is ID |
| English UI | Only if user asks, or product already EN | Laws here as **intent**; English strings then OK |

Familiar-word wins: if a person would not say it in chat or a standup, do not ship it. For ID voice conflicts (empty-state phrasing, apology, particles), anti-slop wins — informal by default, formal when formal.

## Contents

- Buttons
- Errors
- Confirmations & success
- Empty states
- Terminology & tone
- Dates & numbers
- Toasts
- Quick checklist
- Bahasa Indonesia (familiar words)

## 1. Buttons

The button alone must answer "klik ini ngapain?"

- Verb + object: `Simpan perubahan`, `Hapus file`, `Kirim invoice`.
- Sentence case everywhere (buttons, titles, labels) — not Title Case Every Word or ALL CAPS.
- Keep the verb during progress: `Menyimpan…` not `Loading…`.
- Consequential actions name the object on the button — not `Ya`, `Tidak`, or bare `OK`.
- Prefer a specific verb over bare `Kirim` or `Lanjutkan` when one exists.

## 2. Errors

Calm, specific, blameless. The user should know what happened and how to fix it.

- Three parts when useful: what happened + why + how to fix.
- Never blame the user — `Tidak ada akun dengan email itu,` not `Email yang kamu masukkan salah.`
- No `Oops!` or `Terjadi kesalahan` alone.
- Raw codes or jargon never stand alone; if a code helps support, append it quietly after the human sentence.
- Put the fix in the message when known (`File harus di bawah 10 MB. Yang ini 14 MB`).
- No exclamation marks, `silakan`, or `maaf` padding. State it plainly.

## 3. Confirmations & success

At the moment of commitment or completion, copy must remove ambiguity about what is about to happen or what just happened.

- Name object + consequence: `Hapus 'Laporan Q3'? Tidak bisa dibatalkan.` Buttons: `Hapus laporan` / `Batal` — not `Yakin?` with Ya/Tidak.
- State scope with numbers: `Ini mengeluarkan 3 anggota dari proyek.`
- Success messages name what happened: `Invoice #204 terkirim ke acme.com` — plus the next action when useful (`Lihat invoice`).

## 4. Empty states

Two jobs: what this space is + how to fill it, with the CTA right there.

- Example: `Belum ada API key. Buat key untuk mulai request.` + [Buat API key]
- Distinguish first-use, no-results, and error — not a lone illustration with `Tidak ada apa-apa!` (see states.md). Prefer `Belum ada…` over scolding `Tidak ada…`.

## 5. Terminology & tone

Consistent language builds trust; inconsistent language forces the user to translate your product into their mental model on every screen.

- One term per concept, everywhere — pick `proyek` or `workspace`, never both for the same thing. Keep a terms list for the product.
- The user's nouns, not internal names (`Download laporan`, not `Export SSRS artifact`).
- Never `card` / `kartu` for a UI tile — kanban, dashboard, card view. Name the object (`Tambah tugas`, not `Tambah kartu`; `Belum ada tugas`, not `Belum ada kartu`) or omit. Keep `kartu` only for payment/ID.
- Front-load the key word: `Hapus akun` not `Klik di sini jika kamu ingin menghapus akun`.
- No marketing adverbs in product UI: `Effortlessly`, `Seamlessly`, `Supercharge`, `Unlock`, `jelajahi`, `tingkatkan pengalaman`. Plain verbs; say what happens.
- Tone scales with stakes — casual for routine, neutral for transactional, formal for irreversible/legal.
- Write copy you would read aloud to a stranger. Then run § Bahasa Indonesia.

## 6. Dates & numbers

How you display time and quantity signals whether the product respects the user's context or was built for one locale and one precision level.

- Locale-aware dates and numbers (ID: `1.000` / `5,25`); never raw ISO in body copy.
- Relative time for recent activity (`2 jam lalu`) with absolute on hover; absolute (`12 Mar 2026`) for records, invoices, logs.
- Consistent precision per context; round display values, keep exact on hover/export.

## 7. Toasts

Toasts are ephemeral — useful for lightweight confirmation, dangerous for anything the user must act on or remember.

- Lead with the event: `Export selesai. report.csv siap` + action (`Download`).
- Do not notify what the user is already looking at.
- Errors that need action stay inline — toasts vanish (see states.md).

## 8. Quick checklist

Read every new or changed string aloud before shipping — awkward spoken copy is almost always wrong written copy.

- [ ] Copy is Bahasa Indonesia (unless the user asked for English)?
- [ ] Does every button label answer "klik ini ngapain?"
- [ ] Do errors say what happened and how to fix it?
- [ ] Do destructive confirms name the object and consequence?
- [ ] Is terminology consistent with one term per concept?
- [ ] No `card` / `kartu` for UI tiles — object named, or omitted?
- [ ] Would you read this aloud to a coworker without cringing?
- [ ] Every word is something a coworker would actually say (see § Bahasa Indonesia)?

## 9. Bahasa Indonesia

**Role:** Talk like a coworker — not like a kamus, berita, or makalah.

**Rule (verbatim):** use familiar language. don't use rare language that available at kbbi but not usual for conversation.

Ada di KBBI ≠ boleh dipakai. Kalau orang jarang ngomongin kata itu di percakapan / chat / rapat biasa, ganti.

**Test:** Baca keras. Kalau terdengar seperti presenter TV, surat resmi, atau AI yang pamer kosakata → ganti katanya, jangan cuma dipendekin.

**Kalau ragu, cari di internet dulu** — bagaimana orang Indonesia biasa bilang di chat, UI produk (Gojek, Tokopedia, Google, Microsoft), atau percakapan kerja. Jangan cek KBBI dulu. Ada di kamus tapi tidak muncul di percakapan = jangan dipakai.

Shipped writing (UI, changelog, docs, laporan): always Indonesia + voice → `anti-slop-writing-informal` (default) / `anti-slop-writing-formal` (resmi). Section ini tetap menang untuk “orang biasa ngomongin kata ini nggak?”

### When this applies

- **UX copy:** always. Tombol, error, empty state, toast, label, changelog, docs produk.
- User menulis Indonesia, atau minta jawaban Indonesia
- Kamu menjelaskan, bertanya, mengajar, atau ngobrol dalam Indonesia
- Campur kode + penjelasan Indonesia: bagian bicara tetap familiar

Jangan pakai section ini untuk memaksa Indonesia di **chat** kalau user full English. UX copy tetap Indonesia kecuali user minta English.

### Register

Default: percakapan kerja. Jelas, biasa, tidak kaku.

1. **Familiar ≠ gaul.** Jangan `gw`, `lo`, `gue`, `lu`. Jangan numpuk `sih` / `dong` / `nih` kecuali user sudah begitu.
2. Ikuti kata ganti user (`kamu` / `Anda` / tanpa kata ganti). Jangan campur `Anda` dan `kamu`. Default UI: omit / `kamu`.
3. Ikuti ejaan user kalau sudah konsisten (`kalo` / `kalau`, `gimana` / `bagaimana`). Default: ejaan biasa yang tetap terucap (`kalau`, `tapi`, `jadi`, `cek`).
4. Istilah teknis yang sudah umum di kerja (`API`, `commit`, `deploy`, `email`) biarkan. Jangan dipaksa jadi padanan langka (`surel`, `unggah` kalau orang bilang `upload`). Familiar mengalahkan padanan resmi.
5. Formal ringan (hukum, bank, surat) tetap boleh rapi — tetap **jangan** kata langka yang tidak dipakai bicara.

### Swap: langka → familiar

Ganti kiri. Kanan adalah percakapan biasa, bukan sinonim “lebih baku”. KBBI dan bahasa berita bukan acuan familiar ([KBBI vs percakapan](https://newsroom.co.id/memutus-jarak-antara-bahasa-yang-hidup-di-jalanan-dan-bahasa-yang-hidup-di-kbbi/), [kata arkais](https://www.cnnindonesia.com/edukasi/20250206172014-569-1195430/memahami-apa-itu-kata-arkais-dan-contohnya)). Padanan resmi kalah dari kata yang orang sudah pakai ([W3C: Email, bukan Surel](https://github.com/w3c/wai-translations/blob/main/glossaries/Bahasa%20Indonesia.md)). UI: kata pendek yang sudah dikenal ([Seragam](https://seragam.belajar.id/inklusivitas)).

**Arkais / sastra** (jarang di percakapan sekarang)

| Jangan | Bilang |
| --- | --- |
| tatkala, manakala, dikala, apakala, bilamana, jikalau | waktu, pas, kalau, ketika |
| niscaya, sudah barang tentu | pasti, jelas |
| hendaklah, bahwasanya, tiadalah, jua | harus / mending, (hapus), tidak, juga |
| beroleh | dapat |
| syahdan, alkisah, hatta | (hapus) / lalu |
| andaikan, andaikata, seandainya | kalau |
| seyogianya, seyogyanya, hendaknya | sebaiknya, mending |
| laksana, bak, nan | seperti, yang |
| tiada | tidak ada |

**Berita / surat resmi**

| Jangan | Bilang |
| --- | --- |
| perihal, ihwal, hal ihwal | soal, tentang |
| sehubungan dengan, berkenaan dengan, dalam rangka | soal, tentang, untuk |
| menilik, menelisik, menyoal | cek, lihat, bahas |
| mengemuka, mencuat, berkutat, mengetengahkan | muncul, urus, kasih |
| khalayak, insan, animo, geliat, kiprah | orang, minat, gerak, kerja |
| mumpuni, paripurna, segenap, pelbagai | bisa / jago, lengkap, semua, berbagai |
| dewasa ini, kini, kelak | sekarang, nanti |
| oleh karena itu, dengan demikian, maka dari itu, alhasil | jadi, makanya |
| pada hakikatnya, sejatinya, sesungguhnya | sebenarnya, intinya |
| akan tetapi, namun, kendati, sungguhpun | tapi, meski |
| adapun, yakni | soal / untuk, yaitu |
| meramu / merajut (kiasan tulisan) | susun, bikin |

**Padanan paksa / UI kaku**

| Jangan | Bilang |
| --- | --- |
| surel, posel | email |
| unggah / unduh (kalau orang bilang upload/download) | upload / download |
| tetikus, kibor, pranala | mouse, keyboard, link |
| daring / luring (kecuali produk gov sudah pakai) | online / offline |
| gawai | HP / perangkat |
| waring wera wanua | web |
| modifikasi | ubah / edit |
| rasakan, alami (ajakan UI) | coba, mulai |
| singkirkan | tutup, batal, sembunyikan |

Kalau ragu: pilih kata yang bisa dipakai di WhatsApp ke rekan kerja tanpa kedengaran lelucon atau pidato. Masih ragu → cari di internet, bukan KBBI.

### Also drop (bukan “familiar”)

Bukan gaul, tapi juga bukan percakapan:

- Pembuka berita / AI: `Di era…`, `Seiring…`, `Perlu diketahui bahwa…`, `Berikut adalah…`
- Nominalisasi: `melakukan pengecekan` → `cek`
- Pamer sinonim: jangan ganti `pakai` jadi `mempergunakan` / `memanfaatkan` hanya supaya “lebih BI”
- Metafora kamus: `menapaki`, `mengarungi`, `bersemayam` untuk hal biasa → `jalanin`, `lewati`, `ada`

### Examples

1. Jangan: Tatkala fitur ini diimplementasikan, niscaya alur kerja menjadi lebih mumpuni.
   Bilang: Kalau fitur ini dipakai, alurnya jadi lebih gampang.

2. Jangan: Perihal isu tersebut, seyogyanya kita menilik kembali konfigurasi.
   Bilang: Soal itu, mending kita cek lagi konfigurasinya.

3. Jangan: Adapun langkah selanjutnya ialah mengetengahkan opsi yang seyogianya dipilih.
   Bilang: Langkah berikutnya: kasih opsi yang sebaiknya dipilih.

4. Jangan: Dengan demikian, dapat disimpulkan bahwa animo pengguna cukup tinggi.
   Bilang: Jadi pemakaiannya memang tinggi.

5. Jangan: Masukkan surel, lalu unggah berkas. Tetikus tidak terdeteksi.
   Bilang: Isi email, lalu upload file. Mouse tidak terdeteksi.

### Process

1. UX copy? Bahasa Indonesia, kecuali user minta English. Chat? Ikuti bahasa user.
2. Tulis seperti ngomong. Satu ide, kata biasa.
3. Scan kata “pamer KBBI” / berita / sastra / padanan paksa → ganti dari tabel.
4. Ragu suatu kata familiar? **Cari di internet** (copy produk ID, chat, cara orang bilang) — jangan buka KBBI dulu.
5. Baca keras. Kaku atau aneh di mulut → rewrite.
6. Produk copy (tombol, changelog, docs)? Lanjut `anti-slop-writing-informal` (atau `anti-slop-writing-formal` bila resmi) tanpa mengorbankan aturan familiar di atas. Chat / penjelasan: berhenti di sini — jangan pakai output-only rules anti-slop.

**Output:** bahasa yang biasa dipakai orang, bukan yang hanya benar di kamus.
