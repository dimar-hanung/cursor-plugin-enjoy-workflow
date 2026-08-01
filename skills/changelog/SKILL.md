---
name: changelog
description: Menulis changelog singkat dan mudah dipahami untuk user non-teknis dalam Bahasa Indonesia. Gunakan saat user minta changelog, release notes, "apa yang baru", ringkasan update, atau ingin menyampaikan perubahan produk ke client, end user, atau stakeholder tanpa jargon.
---

# Changelog (Non-Teknis)

Update singkat untuk user non-teknis. Bahasa: **Indonesia** (Inggris hanya jika diminta).

**Wajib baca** [anti-slop-writing](../anti-slop-writing/SKILL.md) sebelum menulis dan finalisasi (voice, banlist, sapaan). Detail anti-AI ada di skill itu.

| Yang menang | Surface |
|-------------|---------|
| `anti-slop-writing` | Voice, banlist, sapaan, pemisah kalimat (titik/koma, bukan `—`) |
| Skill ini | Struktur, tanggal, highlight, section `###`, nested list modul, format Perbaikan |

## Sebelum menulis

1. Baca `anti-slop-writing` → polish tiap bullet.
2. Kumpulkan perubahan (input, diff, commit, PR). **Tanya tanggal** jika belum jelas.
3. Filter internal: refactor, CI, deps — skip kecuali changelog teknis.
4. Map tiap item → konteks `1.` (dimana / untuk siapa / ketika apa) + fitur di `-`

## Aturan inti

| Lakukan | Hindari |
|---------|---------|
| Manfaat / behaviour yang user alami | File, API, stack, root cause teknis |
| Kata sehari-hari | deploy, refactor, endpoint |
| Satu fitur/fix = satu nested bullet | Paragraf di nested list, gabung fitur berbeda |
| Spesifik | "berbagai perbaikan", filler marketing |
| Nested list modul (`1.` + `-`) | `###` untuk label modul, flat bullet tanpa modul |

**Panjang:** Highlight → 1–2 kalimat. Baru/Improvement → 1 kalimat. Perbaikan → `Sebelumnya …. Sekarang …` (titik, tanpa em dash).

**Nada:** ramah, langsung. Baru/Improvement front-load manfaat. Perbaikan boleh mulai dari behaviour sebelumnya.

## Struktur

```markdown
# Changelog

## 🎉 [Hari], [tanggal]

[Highlight: 1–2 kalimat ringkas tema pembaruan.]

### Baru
1. [Konteks: dimana | untuk siapa | ketika apa]
   - [Fitur — apa yang bisa dilakukan]

### Perbaikan
1. [Konteks: dimana | untuk siapa | ketika apa — area bermasalah]
   - Sebelumnya …. Sekarang ….

### Improvement
1. [Konteks: dimana | untuk siapa | ketika apa]
   - [Fitur — apa yang jadi lebih baik]
```

| Level | Isi |
|-------|-----|
| `#` | `Changelog` |
| `##` | **Tanggal** (`## 🎉 Kamis, 23 Juli 2026`) |
| `###` | Section: **Baru**, **Perbaikan**, **Improvement** |
| `1.` | **Konteks** — dimana / untuk siapa / ketika apa |
| `-` | **Fitur** — satu kemampuan atau perubahan; manfaat untuk user |

**Section (heading 3, urutan):** pakai hanya yang ada isinya.

1. **Baru** — fitur yang sebelumnya belum ada
2. **Perbaikan** — bug/perilaku salah; format sebelum + sesudah (wajib)
3. **Improvement** — fitur yang sudah ada jadi lebih baik atau lebih cepat

Nama section tetap **Baru**, **Perbaikan**, **Improvement** (Improvement tidak diterjemahkan).

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

Paragraf pendek di bawah tanggal, sebelum section `###`. 1–2 kalimat, fitur konkret, selaras detail di bawah.

```markdown
Pembaruan hari ini menambah pelacakan status sertifikat, impor data pembimbing KIT, unduh jadwal ujian PDF, serta pengiriman sertifikat lewat POS dalam satu transaksi.
```

## Modul (`1.`) vs fitur (`-`)

Nested list punya **dua lapisan** — jangan campur di satu baris.

| Lapisan | Tanya | Isi | Panjang |
|---------|-------|-----|---------|
| **`1.`** | **Konteks** — dimana / untuk siapa / ketika apa (pilih yang paling jelas) | Pendek — penanda konteks, bukan kalimat fitur |
| **`-`** | **Apa?** | Satu fitur; manfaat untuk user | 1 kalimat (Perbaikan: sebelum + sesudah) |

**`1.` = konteks (lokasi, audiens, atau momen)** · **`-` = fitur** (apa yang bisa dilakukan).

| Hindari di `1.` | Hindari di `-` |
|-----------------|----------------|
| Kalimat panjang, behaviour penuh | Nama area saja tanpa manfaat |
| `1. Fitur impor data` (aksi di label) | `- Pembimbing` (konteks di bullet) |

Satu `1.` boleh punya **beberapa `-`** jika beberapa fitur di konteks yang sama.

### Format label `1.` — dimana, untuk siapa, ketika apa

Pilih **satu penanda** (atau gabung ringkas) supaya user tahu **konteks fitur** — mana yang beda dari entri lain.

| Penanda | Pakai jika… | Pola | Contoh `1.` |
|---------|-------------|------|-------------|
| **Dimana** | Lokasi/halaman/modul penting | `[Area] di/pada [lokasi]` | `Pembayaran di Fasilitas A`, `Jadwal Ujian pada Dashboard` |
| **Untuk siapa** | Beda role/audiens | `[Fitur/area] untuk [siapa]` | `Sertifikat untuk Mahasiswa`, `Laporan untuk Dosen` |
| **Ketika apa** | Momen/trigger yang membedakan | `[Fitur] ketika/saat [kondisi]` | `Notifikasi ketika Pembayaran Berhasil`, `Email saat Transaksi POS Selesai` |

**Gabung** jika perlu (jangan panjang): `Notifikasi pada Pembayaran di Fasilitas A` (dimana + sub-konteks).

**`-` (fitur):** fokus **apa yang bisa dilakukan** — tidak ulang penanda `1.` kalau sudah jelas.

```markdown
1. Sertifikat untuk Mahasiswa          ← untuk siapa
   - Status sertifikat bisa dilacak dari dashboard.

1. Pembayaran di Fasilitas A           ← dimana
   - Bisa bayar cicilan per bulan.

1. Notifikasi ketika Pembayaran POS    ← ketika apa
   - Email konfirmasi terkirim otomatis setelah bayar.
```

`di` / `pada` = lokasi · `untuk` = audiens · `ketika` / `saat` = momen/trigger.

## Format Perbaikan (wajib)

Di section `### Perbaikan`: **`1.` = label modul/area** bermasalah · **`-` = sebelum + sesudah**.

```markdown
### Perbaikan
1. Masuk ke akun
   - Sebelumnya macet di layar login. Sekarang langsung ke halaman yang benar.
```

`1. Masuk ke akun` = area login (nama di UI/navigasi, bukan label generik).

## Format Improvement (wajib)

Di section `### Improvement`: fitur **sudah ada** yang jadi lebih baik (lebih cepat, lebih jelas, lebih mudah) — **bukan** fitur baru.

| Bagian | Isi |
|--------|-----|
| `1.` | Konteks: dimana / untuk siapa / ketika apa (sama aturan label Baru) |
| `-` | Apa yang **membaik** — spesifik, bukan "lebih baik" saja |

```markdown
### Improvement
1. Pencarian pada Dashboard untuk Admin
   - Hasil pencarian tampil lebih cepat saat cari nama peserta.
```

| Lakukan | Hindari |
|---------|---------|
| `1. Pencarian pada Dashboard` + `- Hasil … lebih cepat` | `1. Pencarian` (tanpa dimana/untuk siapa) |
| Sebut **apa** yang membaik (kecepatan, kejelasan, alur) | Vague: "pengalaman lebih baik", "UI diperbaiki" |
| Bedakan dari **Baru** (belum ada) vs **Improvement** (sudah ada, ditingkatkan) | Masukkan fitur baru ke Improvement |

## Workflow

1. anti-slop-writing → 2. Catat perubahan → 3. Map modul + konteks → 4. Buang internal → 5. Terjemahkan → 6. Kelompokkan Baru/Perbaikan/Improvement → 7. Nested list → 8. Tanggal + highlight → 9. **Sisipkan blok tanggal di atas** (terbaru paling atas) → 10. Polish

## Contoh

**Satu tanggal (pembaruan hari ini):**

```markdown
# Changelog

## 🎉 Jumat, 2 Agustus 2026

Update menambah cicilan di Fasilitas A, notifikasi chat grup, dan email konfirmasi pembayaran di fasilitas yang sama.

### Baru
1. Pembayaran di Fasilitas A
   - Bisa bayar cicilan per bulan.
2. Notifikasi pada Chat Grup
   - Push saat ada pesan baru di grup.
3. Notifikasi ketika Pembayaran di Fasilitas A
   - Email konfirmasi terkirim setelah pembayaran berhasil.

### Perbaikan
1. Masuk ke akun
   - Sebelumnya tetap di layar login. Sekarang langsung ke halaman yang benar.

### Improvement
1. Pencarian pada Dashboard untuk Admin
   - Hasil pencarian tampil lebih cepat saat cari nama peserta.
```

**Beberapa tanggal (terbaru di atas):**

```markdown
# Changelog

## 🎉 Jumat, 2 Agustus 2026

Update menambah cicilan di Fasilitas A dan notifikasi chat grup.

### Baru
1. Pembayaran di Fasilitas A
   - Bisa bayar cicilan per bulan.
2. Notifikasi pada Chat Grup
   - Push saat ada pesan baru di grup.

## 🎉 Kamis, 23 Juli 2026

Pembaruan hari itu menambah pelacakan status sertifikat, impor data pembimbing KIT, unduh jadwal ujian PDF, serta pengiriman sertifikat lewat POS dalam satu transaksi.

### Baru
1. Sertifikat untuk Mahasiswa
   - Status sertifikat bisa dilacak dari dashboard.
2. Impor Data Pembimbing KIT pada Menu Admin
   - Data pembimbing bisa diimpor dari spreadsheet.
3. Unduh Jadwal Ujian pada Halaman Ujian
   - Jadwal ujian bisa diunduh sebagai PDF.
4. Pengiriman Sertifikat ketika Bayar di POS
   - Sertifikat bisa dikirim lewat POS dalam satu transaksi.
```

## Cek sebelum kirim

- [ ] anti-slop-writing (baca aloud)
- [ ] Tanggal `## 🎉 Hari, d Bulan yyyy` + highlight
- [ ] **Terbaru di atas** (blok tanggal baru paling atas)
- [ ] Section `### Baru` / `### Perbaikan` / `### Improvement` (h3)
- [ ] Modul = nested `1.` + `-`, bukan `###`
- [ ] `1.` punya konteks (dimana / untuk siapa / ketika apa) · `-` = fitur
- [ ] Perbaikan: sebelumnya + sekarang; Improvement: konteks jelas + apa yang membaik; tanpa em dash

## Rules

**MUST:** anti-slop-writing · Indonesia · tanggal `## 🎉 …` + highlight · **terbaru di atas** · section `###` · nested list · label `1.` pakai dimana/untuk siapa/ketika apa · Perbaikan sebelum+sesudah · nama UI bukan internal.

**NEVER:** `###` untuk label modul · flat bullet tanpa modul · highlight vague · em dash · jargon/commit mentah · filler · urut tanggal lama di atas.

## References

- [anti-slop-writing](../anti-slop-writing/SKILL.md) — voice, banlist, polish
