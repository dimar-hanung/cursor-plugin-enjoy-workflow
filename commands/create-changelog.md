---
name: create-changelog
description: Tulis changelog non-teknis Bahasa Indonesia (release notes / apa yang baru). Struktur tanggal + highlight + nested modul; tipe perubahan inline di bullet; voice via anti-slop-writing.
---

# Changelog (Non-Teknis)

Update singkat untuk user non-teknis. Bahasa: **Indonesia** (Inggris hanya jika diminta).

**Wajib baca** [anti-slop-writing](../skills/anti-slop-writing/SKILL.md) sebelum menulis dan finalisasi (voice, banlist, sapaan). Detail anti-AI ada di skill itu.

- **`anti-slop-writing`** — voice, banlist, sapaan, pemisah kalimat (titik/koma, bukan `—`)
- **Command ini** — struktur, tanggal, highlight domain/modul (filter relevansi), nested list modul, label tipe inline (Baru / Perbaikan / Improvement / Dihapus / Berubah)

## Sebelum menulis

1. Baca `anti-slop-writing` → polish tiap bullet.
2. Kumpulkan perubahan (input, diff, commit, PR). **Tanya tanggal** jika belum jelas.
3. Filter internal: refactor, CI, deps — skip kecuali changelog teknis.
4. Map tiap item → konteks `1.` (dimana / untuk siapa / ketika apa) + fitur di `-` dengan label tipe di depan

## Aturan inti

**Lakukan:**

- Manfaat / behaviour yang user alami
- Kata sehari-hari
- Satu fitur/fix = satu nested bullet
- Spesifik
- Nested list modul (`1.` + `-`) dengan tipe inline

**Hindari:**

- File, API, stack, root cause teknis
- deploy, refactor, endpoint
- Paragraf di nested list, gabung fitur berbeda
- "berbagai perbaikan", filler marketing
- `###` section per tipe · `###` untuk label modul · flat bullet tanpa modul

**Panjang:** Highlight → 1 kalimat, **nama domain/modul saja**. Bullet → 1 kalimat setelah label (atau `Sebelumnya … Sekarang …` jika kontras membantu).

**Nada:** ramah, langsung. Utamakan **Sekarang** untuk manfaat/behaviour baru. Pakai **Sebelumnya** + **Sekarang** saat perbandingan membuat perubahan lebih jelas — tidak hanya untuk Perbaikan.

## Struktur

```markdown
# Changelog

## 🎉 [Hari], [tanggal]

[Highlight: domain/modul yang berubah — supaya user tahu relevan atau tidak.]

1. [Konteks: dimana | untuk siapa | ketika apa]
   - Baru, Sekarang [fitur — apa yang bisa dilakukan]
   - Perbaikan, Sebelumnya …. Sekarang ….
   - Improvement, Sebelumnya …. Sekarang ….
   - Dihapus, Sebelumnya …. Sekarang ….
   - Berubah, Sebelumnya …. Sekarang ….
```

**Level:**

- **`#`** — `Changelog`
- **`##`** — **Tanggal** (`## 🎉 Kamis, 23 Juli 2026`)
- **paragraf setelah `##`** — **Highlight** — domain/modul yang berubah (filter relevansi)
- **`1.`** — **Konteks** — dimana / untuk siapa / ketika apa
- **`-`** — **Tipe + fitur** — label tipe, lalu isi (boleh pakai **Sekarang** / **Sebelumnya**)

**Tipe perubahan (inline di `-`, bukan section):**

- **Baru** — fitur yang sebelumnya belum ada → `Baru, Sekarang [manfaat]` (atau tanpa Sekarang jika sudah jelas)
- **Perbaikan** — bug/perilaku salah → `Perbaikan, Sebelumnya …. Sekarang ….` (kontras wajib)
- **Improvement** — fitur sudah ada, jadi lebih baik → `Improvement, Sebelumnya …. Sekarang ….` — atau `Improvement, Sekarang …` jika cukup
- **Dihapus** — fitur, menu, atau opsi tidak tersedia lagi → `Dihapus, Sebelumnya …. Sekarang ….` — jelaskan apa yang hilang dan alternatifnya
- **Berubah** — aturan, kebijakan, atau alur resmi berubah (bukan bug) → `Berubah, Sebelumnya …. Sekarang ….` — mis. peraturan, syarat, batas waktu

**Pilih label:**

- Fitur baru → **Baru**
- Sesuatu rusak/salah, lalu diperbaiki → **Perbaikan**
- Fitur lama jadi lebih baik → **Improvement**
- Fitur/opsi dihilangkan → **Dihapus**
- Aturan hukum, kebijakan, syarat, atau alur wajib berubah → **Berubah**

Bedakan **Berubah** vs **Perbaikan**: **Berubah** = memang sengaja mengikuti aturan/kebijakan baru; **Perbaikan** = ada yang salah lalu dibetulkan. Bedakan **Dihapus** vs **Berubah**: **Dihapus** = tidak ada lagi; **Berubah** = masih ada tapi aturannya beda.

### Sekarang / Sebelumnya (semua tipe)

- **Sekarang** — manfaat, behaviour baru, atau kondisi setelah update
  - Contoh: `Baru, Sekarang bisa bayar cicilan per bulan.` · `Improvement, Sekarang hasil pencarian tampil lebih cepat.`
- **Sebelumnya** — kondisi lama — pasang dengan **Sekarang** untuk kontras
  - Contoh: `Perbaikan, Sebelumnya macet di login. Sekarang langsung ke halaman yang benar.` · `Dihapus, Sebelumnya bisa unduh Excel. Sekarang hanya PDF.` · `Berubah, Sebelumnya batas pengajuan 30 hari. Sekarang mengikuti aturan baru 14 hari.`

- **Baru:** utamakan `Sekarang` (belum ada "sebelumnya" di produk — jarang perlu **Sebelumnya**).
- **Perbaikan:** **Sebelumnya** + **Sekarang** wajib.
- **Improvement:** pakai pasangan **Sebelumnya** + **Sekarang** jika kontras memperjelas; cukup **Sekarang** saja jika sudah jelas.
- **Dihapus:** **Sebelumnya** + **Sekarang** wajib — sebut apa yang hilang dan apa yang user lakukan sekarang (alternatif, jika ada).
- **Berubah:** **Sebelumnya** + **Sekarang** wajib — fokus aturan/kebijakan/alur resmi, bukan bug.

Pisahkan kalimat dengan titik, bukan em dash.

Label tipe: **Baru**, **Perbaikan**, **Improvement** (tidak diterjemahkan), **Dihapus**, **Berubah**. Pisahkan label dan isi dengan koma + spasi: `Baru, …`

Satu `1.` boleh punya beberapa `-` dengan tipe berbeda jika beberapa perubahan di konteks yang sama.

### Tanggal (wajib)

Format: **`## 🎉 [Hari], [d] [Bulan] [yyyy]`** — bahasa Indonesia, emoji tada `🎉` wajib di depan tanggal.

Contoh: `## 🎉 Kamis, 23 Juli 2026`

**Urutan tanggal: terbaru di atas.** Setiap pembaruan = satu blok `##` tanggal. Blok baru selalu **disisipkan paling atas** (langsung di bawah `# Changelog`). Tanggal lama turun ke bawah. Jangan urut kronologis naik (lama → baru).

```markdown
# Changelog

## 🎉 Jumat, 2 Agustus 2026    ← terbaru (paling atas)
…

## 🎉 Kamis, 23 Juli 2026      ← lebih lama
…
```

Satu dokumen bisa banyak tanggal; yang ditulis hari ini selalu di atas.

### Highlight (wajib)

Satu kalimat di bawah tanggal, sebelum nested list. **Sebut domain/modul apa saja yang berubah** — supaya user langsung tahu changelog ini untuk mereka atau boleh dilewati.

**Tujuan:** filter relevansi, bukan ringkasan fitur.

**Rumus:** `Ada perubahan di [modul], [modul], dan [modul].`

- Ambil nama dari label `1.` — singkat, tanpa detail `-`.
- Boleh pakai nama UI yang user kenal (Pembayaran, Sertifikat, Chat Grup).
- Jangan sebut apa yang berubah, manfaat, atau tipe (Baru/Perbaikan).

**Hindari:**

- `…bisa bayar cicilan, email konfirmasi, push notifikasi…` (detail fitur)
- `Pembayaran kampus lebih fleksibel…` (manfaat/tema)

**Lebih baik:**

- `Ada perubahan di pembayaran kampus, chat grup, login, dan pengajuan cuti.`
- `Ada perubahan di sertifikat mahasiswa, impor pembimbing KIT, jadwal ujian, dan pengiriman sertifikat POS.`

**Tes cepat:** dari highlight saja, user tahu **area mana** yang kena — tanpa perlu baca bullet.

## Modul (`1.`) vs fitur (`-`)

Nested list punya **dua lapisan** — jangan campur di satu baris.

- **`1.`** — tanya: **Konteks** (dimana / untuk siapa / ketika apa, pilih yang paling jelas) · isi: pendek, penanda konteks, bukan kalimat fitur
- **`-`** — tanya: **Tipe + apa?** · isi: label tipe + fitur; boleh **Sekarang** / **Sebelumnya** · panjang: 1 kalimat (kontras: sebelum + sesudah)

**`1.` = konteks (lokasi, audiens, atau momen)** · **`-` = tipe + fitur** (Baru / Perbaikan / Improvement / Dihapus / Berubah, lalu apa yang berubah).

**Hindari di `1.`:**

- Kalimat panjang, behaviour penuh
- `1. Fitur impor data` (aksi di label)

**Hindari di `-`:**

- Nama area saja tanpa manfaat
- `- Pembimbing` (konteks di bullet)

Satu `1.` boleh punya **beberapa `-`** jika beberapa fitur di konteks yang sama.

### Format label `1.` — dimana, untuk siapa, ketika apa

Pilih **satu penanda** (atau gabung ringkas) supaya user tahu **konteks fitur** — mana yang beda dari entri lain.

- **Dimana** — lokasi/halaman/modul penting · pola: `[Area] di/pada [lokasi]` · contoh: `Pembayaran di Fasilitas A`, `Jadwal Ujian pada Dashboard`
- **Untuk siapa** — beda role/audiens · pola: `[Fitur/area] untuk [siapa]` · contoh: `Sertifikat untuk Mahasiswa`, `Laporan untuk Dosen`
- **Ketika apa** — momen/trigger yang membedakan · pola: `[Fitur] ketika/saat [kondisi]` · contoh: `Notifikasi ketika Pembayaran Berhasil`, `Email saat Transaksi POS Selesai`

**Gabung** jika perlu (jangan panjang): `Notifikasi pada Pembayaran di Fasilitas A` (dimana + sub-konteks).

**`-` (fitur):** fokus **apa yang bisa dilakukan** — tidak ulang penanda `1.` kalau sudah jelas.

```markdown
1. Sertifikat untuk Mahasiswa          ← untuk siapa
   - Baru, Sekarang status sertifikat bisa dilacak dari dashboard.

1. Pembayaran di Fasilitas A           ← dimana
   - Baru, Sekarang bisa bayar cicilan per bulan.

1. Notifikasi ketika Pembayaran POS    ← ketika apa
   - Baru, Sekarang email konfirmasi terkirim otomatis setelah bayar.
```

`di` / `pada` = lokasi · `untuk` = audiens · `ketika` / `saat` = momen/trigger.

## Format per tipe

### Perbaikan

**`-` = `Perbaikan,` + Sebelumnya + Sekarang** — kontras wajib.

```markdown
1. Masuk ke akun
   - Perbaikan, Sebelumnya macet di layar login. Sekarang langsung ke halaman yang benar.
```

### Improvement

Fitur **sudah ada** yang jadi lebih baik — **bukan** fitur baru.

- **`1.`** — konteks: dimana / untuk siapa / ketika apa
- **`-`** — `Improvement, Sebelumnya …. Sekarang ….` — atau `Improvement, Sekarang …` jika kontras sudah jelas

```markdown
1. Pencarian pada Dashboard untuk Admin
   - Improvement, Sebelumnya hasil pencarian lambat. Sekarang tampil lebih cepat saat cari nama peserta.
```

**Lakukan:**

- Kontras **Sebelumnya** + **Sekarang** saat membantu
- Sebut **apa** yang membaik (kecepatan, kejelasan, alur)
- Bedakan dari **Baru** (belum ada) vs **Improvement** (sudah ada, ditingkatkan)

**Hindari:**

- Vague: "pengalaman lebih baik", "UI diperbaiki"
- Masukkan fitur baru dengan label Baru
- Improvement tanpa detail konkret

### Dihapus

Fitur, menu, tombol, atau opsi **tidak tersedia lagi**.

```markdown
1. Unduh Laporan pada Dashboard
   - Dihapus, Sebelumnya laporan bisa diunduh sebagai Excel. Sekarang hanya tersedia format PDF.
```

Sebut alternatif jika ada. Jangan pakai **Perbaikan** untuk sesuatu yang sengaja dihilangkan.

### Berubah

Aturan, kebijakan, syarat, batas waktu, atau alur resmi **berubah** — bukan bug, bukan peningkatan UX.

```markdown
1. Pengajuan Cuti untuk Karyawan
   - Berubah, Sebelumnya pengajuan cuti bisa diajukan hingga 30 hari sebelumnya. Sekarang mengikuti kebijakan baru maksimal 14 hari sebelum tanggal cuti.

1. Verifikasi Identitas pada Pendaftaran
   - Berubah, Sebelumnya cukup upload KTP. Sekarang wajib verifikasi wajah sesuai ketentuan terbaru.
```

Pakai **Berubah** untuk perubahan hukum, regulasi, kebijakan institusi, atau syarat bisnis. Pakai **Perbaikan** hanya jika sistem sebelumnya salah menjalankan aturan yang sudah benar.

## Workflow

1. anti-slop-writing → 2. Catat perubahan → 3. Map modul + konteks → 4. Buang internal → 5. Terjemahkan → 6. Pilih label (Baru / Perbaikan / Improvement / Dihapus / Berubah) per item → 7. Nested list dengan tipe inline → 8. Tanggal + highlight domain (dari label `1.`) → 9. **Sisipkan blok tanggal di atas** (terbaru paling atas) → 10. Polish

## Contoh

**Satu tanggal (pembaruan hari ini):**

```markdown
# Changelog

## 🎉 Jumat, 2 Agustus 2026

Ada perubahan di pembayaran kampus, chat grup, login, pencarian admin, unduh laporan, dan pengajuan cuti.

1. Pembayaran di Fasilitas A
   - Baru, Sekarang bisa bayar cicilan per bulan.
   - Baru, Sekarang email konfirmasi terkirim setelah pembayaran berhasil.
2. Notifikasi pada Chat Grup
   - Baru, Sekarang push terkirim saat ada pesan baru di grup.
3. Masuk ke akun
   - Perbaikan, Sebelumnya tetap di layar login. Sekarang langsung ke halaman yang benar.
4. Pencarian pada Dashboard untuk Admin
   - Improvement, Sebelumnya hasil pencarian lambat. Sekarang tampil lebih cepat saat cari nama peserta.
5. Unduh Laporan pada Dashboard
   - Dihapus, Sebelumnya laporan bisa diunduh sebagai Excel. Sekarang hanya tersedia format PDF.
6. Pengajuan Cuti untuk Karyawan
   - Berubah, Sebelumnya pengajuan cuti bisa diajukan hingga 30 hari sebelumnya. Sekarang mengikuti kebijakan baru maksimal 14 hari sebelum tanggal cuti.
```

**Beberapa tanggal (terbaru di atas):**

```markdown
# Changelog

## 🎉 Jumat, 2 Agustus 2026

Ada perubahan di pembayaran kampus dan chat grup.

1. Pembayaran di Fasilitas A
   - Baru, Sekarang bisa bayar cicilan per bulan.
2. Notifikasi pada Chat Grup
   - Baru, Sekarang push terkirim saat ada pesan baru di grup.

## 🎉 Kamis, 23 Juli 2026

Ada perubahan di sertifikat mahasiswa, impor pembimbing KIT, jadwal ujian, dan pengiriman sertifikat POS.

1. Sertifikat untuk Mahasiswa
   - Baru, Sekarang status sertifikat bisa dilacak dari dashboard.
2. Impor Data Pembimbing KIT pada Menu Admin
   - Baru, Sekarang data pembimbing bisa diimpor dari spreadsheet.
3. Unduh Jadwal Ujian pada Halaman Ujian
   - Baru, Sekarang jadwal ujian bisa diunduh sebagai PDF.
4. Pengiriman Sertifikat ketika Bayar di POS
   - Baru, Sekarang sertifikat bisa dikirim lewat POS dalam satu transaksi.
```

## Cek sebelum kirim

- [ ] anti-slop-writing (baca aloud)
- [ ] Tanggal `## 🎉 Hari, d Bulan yyyy` + highlight domain/modul (filter relevansi)
- [ ] **Terbaru di atas** (blok tanggal baru paling atas)
- [ ] Tanpa section `###` per tipe (Baru, Perbaikan, dll.)
- [ ] Modul = nested `1.` + `-` dengan label tipe inline
- [ ] `1.` punya konteks (dimana / untuk siapa / ketika apa)
- [ ] Pakai **Sekarang** / **Sebelumnya** sesuai tipe (Perbaikan / Dihapus / Berubah: pasangan wajib; Baru/Improvement: utamakan Sekarang)
- [ ] **Dihapus** = fitur hilang · **Berubah** = aturan/kebijakan/alur resmi beda (bukan bug)
- [ ] Tanpa em dash

## Rules

**MUST:** anti-slop-writing · Indonesia · tanggal `## 🎉 …` + highlight domain/modul · **terbaru di atas** · nested list · label tipe inline · **Sekarang** untuk manfaat baru · **Sebelumnya**+**Sekarang** wajib di Perbaikan, Dihapus, Berubah · label `1.` pakai dimana/untuk siapa/ketika apa · nama UI bukan internal.

**NEVER:** section `###` per tipe · `###` untuk label modul · flat bullet tanpa modul · bullet tanpa label tipe · **Berubah** untuk bug · **Dihapus** untuk peningkatan UX · highlight berisi detail fitur atau manfaat · em dash · jargon/commit mentah · filler · urut tanggal lama di atas.

## References

- [anti-slop-writing](../skills/anti-slop-writing/SKILL.md) — voice, banlist, polish
