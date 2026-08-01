---
name: changelog
description: Menulis changelog singkat dan mudah dipahami untuk user non-teknis dalam Bahasa Indonesia. Gunakan saat user minta changelog, release notes, "apa yang baru", ringkasan update, atau ingin menyampaikan perubahan produk ke client, end user, atau stakeholder tanpa jargon.
---

# Changelog (Non-Teknis)

Ubah perubahan kode menjadi **update singkat dan jelas** yang mudah dipahami — tanpa jargon, tanpa detail teknis.

Bahasa: **Bahasa Indonesia**. Gunakan Inggris hanya jika user minta atau audiens jelas non-Indonesia.

**UX writing:** Baca [skills/anti-slop-writing/SKILL.md](../anti-slop-writing/SKILL.md) sebelum menulis dan sebelum finalisasi. Terapkan voice, anti-AI banlist, dan aturan sapaan untuk tiap bullet. **Tidak ada em dash `—` di teks bullet** (ikut anti-slop-writing); pisahkan dengan titik atau koma.

## Prioritas dengan anti-slop-writing

| Surface | Yang menang |
|---------|-------------|
| Voice, banlist, sapaan, loanword | `anti-slop-writing` |
| Struktur changelog (Baru/Peningkatan/Perbaikan, Sorotan, subjudul area) | skill ini |
| Format Perbaikan (sebelum + sesudah) | skill ini |
| Pemisah kalimat di bullet | `anti-slop-writing` (titik/koma, bukan `—`) |

Perbaikan boleh mulai dari behaviour sebelumnya (konteks fix); Baru/Peningkatan tetap front-load manfaat (`Sekarang bisa…`, bukan `Kami telah menambahkan…`).

## Sebelum menulis

1. **Baca** `skills/anti-slop-writing/SKILL.md` — aturan Bahasa Indonesia natural untuk produk (bukan terjemahan mesin / AI slop).
2. **Kenali audiens** — siapa yang baca? (customer, operasional internal, manajer). Default: end user.
3. **Kumpulkan perubahan** — dari input user, git diff, PR, commit, atau scope release. Jika belum jelas, tanya versi/tanggal dan apa yang berubah.
4. **Filter** — skip refactor, bump dependency, CI, dan pekerjaan internal kecuali user minta changelog teknis.

## Aturan penulisan

| Lakukan | Hindari |
|---------|---------|
| Sebut apa yang **bisa user lakukan** atau **apa yang jadi lebih baik** | Sebut file, API, library, atau stack |
| Pakai kata sehari-hari | Pakai "deploy", "refactor", "endpoint", "migration" |
| Satu ide per bullet | Paragraf panjang atau bullet bertingkat |
| Mulai dari manfaat | Mulai dari cara implementasi |
| Spesifik tapi ringkas | Vague ("berbagai perbaikan") |

**Nada:** ramah, langsung, impersonal atau sapaan konsisten ("Sekarang bisa…", "Anda bisa…" — pilih satu, jangan campur).

**Panjang per item:** Baru/Peningkatan: 1 kalimat. Perbaikan: pola `Sebelumnya …. Sekarang …` (dua kalimat pendek, dipisah titik).

**Banyak fitur:** Satu changelog sering punya banyak item — **tetap satu bullet per fitur/perbaikan**, jangan gabung fitur berbeda jadi satu baris. Jangan potong fitur penting hanya demi pendek.

## Banyak fitur dalam satu changelog

Default: release punya **banyak** perubahan. Struktur supaya tetap mudah discan:

### 1. Sorotan (opsional, untuk release besar)

Jika **Baru** punya 3+ item penting, tambah 2–4 bullet di atas section — yang paling berdampak untuk user:

```markdown
**Sorotan**
- [Fitur paling penting 1]
- [Fitur paling penting 2]
```

Sorotan = cuplikan, bukan pengganti daftar lengkap. Semua fitur tetap ada di section di bawah.

### 2. Kelompokkan per area (jika 5+ item dalam satu section)

Pakai subjudul area produk — bukan nama modul teknis:

```markdown
## Baru

### Laporan
- ...
### Pembayaran
- ...

## Perbaikan

### Formulir
- ...
### Notifikasi
- ...
```

Subjudul area: **Laporan**, **Pembayaran**, **Akun**, **Notifikasi**, **Dashboard** — sesuai produk.

### 3. Kapan pakai apa

| Jumlah item (per section) | Struktur |
|---------------------------|----------|
| 1–4 | Flat list (`-` saja) |
| 5–12 | Subjudul area di dalam section |
| 12+ | Sorotan + subjudul area |

### 4. Yang tetap digabung

Gabung hanya **perbaikan kecil sejenis** di area yang sama:

- "Beberapa perbaikan tampilan di halaman pengaturan."
- "Perbaikan kecil pada pesan error saat upload."

**Jangan** gabung fitur baru atau perbaikan yang user perlu tahu secara terpisah.

## Kategori

Pakai hanya section yang ada isinya. Urutan:

1. **Baru** — sesuatu yang sebelumnya user belum bisa lakukan
2. **Peningkatan** — fitur yang sudah ada jadi lebih baik atau lebih cepat
3. **Perbaikan** — apa yang bermasalah **sebelumnya**, dan apa yang **sekarang** benar (format wajib, lihat bawah)

Opsional jika relevan:

- **Perubahan** — perilaku berubah; user mungkin perlu menyesuaikan (jelaskan dampak praktis)
- **Dihapus** — fitur atau opsi tidak tersedia lagi (sebut alternatif)

Jangan pakai: Added, Deprecated, Security, Performance, Internal, Chore, Refactor.

## Format Perbaikan (wajib)

Tiap item di **Perbaikan** harus jelas **sebelum** dan **sesudah** supaya user tahu apa yang diperbaiki.

**Format default** — satu bullet, dua kalimat pendek, **tanpa em dash**:

```markdown
- Sebelumnya macet di layar login. Sekarang langsung ke halaman yang benar.
- Sebelumnya email notifikasi terkirim dua kali. Sekarang cuma satu.
- Sebelumnya upload file besar sering gagal di tengah. Sekarang bisa selesai.
```

| Lakukan | Hindari |
|---------|---------|
| Sebut perilaku yang user **alami** | Sebut root cause teknis (null pointer, race condition) |
| Konkret: "macet di login", "tanggal salah" | Vague: "ada bug", "tidak berfungsi dengan baik" |
| Satu masalah = satu bullet | Campur beberapa bug dalam satu bullet |
| Titik atau koma sebagai pemisah | Em dash `—` di teks bullet (AI tell, lihat anti-slop-writing) |

**Variasi singkat** jika "sebelumnya" sudah implisit:

```markdown
- Tanggal di invoice PDF yang diunduh sekarang sesuai hari yang benar (sebelumnya sering beda satu hari).
```

**Gabungan perbaikan kecil** — boleh tanpa detail sebelum/sesudah per item:

```markdown
- Beberapa perbaikan kecil pada tampilan formulir pengaturan.
```

## Workflow

```
1. Baca anti-slop-writing     → voice, banlist, sapaan (skills/anti-slop-writing/SKILL.md)
2. Catat perubahan mentah      → dari diff, commit, atau catatan user — semua fitur
3. Buang yang internal         → test, CI, deps, cleanup kode
4. Terjemahkan tiap item       → satu bullet per fitur/perbaikan penting
   Perbaikan: sebut behaviour sebelumnya + sekarang
5. Kelompokkan                 → Baru / Peningkatan / Perbaikan
6. Subkelompokkan jika perlu   → area produk (Laporan, Akun, …) bila 5+ item
7. Sorotan (opsional)          → 2–4 item terpenting jika release besar
8. Tambah judul                → versi + tanggal jika ada
9. Polish + cek                → anti-slop-writing audit; tanpa jargon; tanpa em dash di bullet
```

## Template output

```markdown
# [Nama produk] — [Versi atau tanggal]

[Satu kalimat opsional: tema release — hanya jika membantu.]

**Sorotan** *(opsional, release besar)*
- [2–4 item paling penting]

## Baru

### [Area produk] *(jika 5+ item)*
- [Satu fitur = satu bullet]

## Peningkatan
- ...

## Perbaikan

### [Area produk]
- Sebelumnya [behaviour bermasalah]. Sekarang [behaviour benar].
```

Release kecil (1–4 item total): flat list tanpa Sorotan dan tanpa subjudul area.

## Panduan terjemahan

Ubah input teknis ke bahasa user:

| Teknis (input) | Non-teknis (output) |
|----------------|---------------------|
| Added export to CSV endpoint | Data bisa diunduh sebagai spreadsheet |
| Fixed null pointer in payment handler | Sebelumnya pembayaran gagal saat keranjang kosong. Sekarang bisa lanjut. |
| Optimized database queries on dashboard | Dashboard lebih cepat dimuat |
| Implemented OAuth2 with Google | Bisa masuk dengan akun Google |
| Bumped React 18 → 19 | *(skip — internal)* |
| Refactored auth module | *(skip — internal)* |
| Fixed typo in error message | Sebelumnya pesan error membingungkan. Sekarang jelas apa yang harus dilakukan. |
| Added pagination to user list | Daftar panjang lebih mudah dibaca. Gunakan next/previous untuk pindah halaman. |

Perbaikan kecil bisa digabung: **Beberapa perbaikan kecil pada formulir dan pesan error.**

## Hindari pola terjemahan mesin / AI

Ikuti banlist dan contoh di `skills/anti-slop-writing/SKILL.md`. Ringkas untuk changelog:

| Hindari | Pakai |
|---------|-------|
| "Apakah Anda dapat…" (pembuka kaku) | "Bisa…" / "Sekarang bisa…" |
| "Kami telah menambahkan fitur…" | Langsung ke manfaat: "Bisa unduh laporan sebagai PDF." |
| "Berbagai perbaikan bug dan peningkatan" | Sebut konkret atau gabung per kategori |
| "Mohon maaf atas ketidaknyamanan" | Langsung sebut apa yang diperbaiki |
| "melakukan pembayaran", "melakukan penyimpanan" | "bayar", "simpan" |
| Marketing fluff (`Jelajahi…`, `Mulai perjalanan…`) | Nama aksi konkret |
| Em dash `—` di bullet | Titik atau koma (`Sebelumnya …. Sekarang …`) |

## Contoh

### Contoh 1 — Release kecil

**Input:** Fixed login redirect bug, added dark mode toggle, improved search speed.

**Output:**

```markdown
# Acme App — Maret 2026

## Baru
- Mode gelap bisa diaktifkan dari Pengaturan.

## Peningkatan
- Hasil pencarian tampil lebih cepat.

## Perbaikan
- Sebelumnya setelah masuk tetap di layar login. Sekarang langsung ke halaman yang benar.
```

### Contoh 2 — Dari commit (filter internal)

**Input commit:**
- `feat: add Stripe webhook for refunds`
- `fix: invoice PDF date timezone`
- `chore: upgrade eslint`

**Output:**

```markdown
# Billing — v2.4

## Peningkatan
- Status refund di akun lebih sering update dengan benar.

## Perbaikan
- Tanggal di invoice PDF yang diunduh sekarang sesuai hari yang benar (sebelumnya sering beda satu hari).
```

(commit `eslint` dibuang; webhook dijelaskan dari sisi user.)

### Contoh 3 — Release banyak fitur

**Input:** Export PDF laporan, filter tanggal di dashboard, login Google, notifikasi push, perbaikan upload file besar, perbaikan typo label, perbaikan crash saat logout, perbaikan email duplikat.

**Output:**

```markdown
# Acme App — v3.0 — Agustus 2026

Update besar: laporan, dashboard, dan masuk akun.

**Sorotan**
- Laporan bisa diunduh sebagai PDF.
- Bisa masuk dengan akun Google.
- Notifikasi push untuk update penting.

## Baru

### Laporan
- Laporan bisa diunduh sebagai PDF.

### Dashboard
- Filter tanggal di dashboard untuk lihat data per periode.

### Akun
- Bisa masuk dengan akun Google.
- Notifikasi push untuk update penting.

## Perbaikan

### Upload
- Sebelumnya upload file besar sering gagal di tengah. Sekarang bisa selesai.

### Akun
- Sebelumnya aplikasi error saat keluar. Sekarang keluar lancar.
- Sebelumnya email notifikasi terkirim dua kali. Sekarang cuma satu.

### Tampilan
- Label di beberapa formulir sekarang lebih jelas (sebelumnya membingungkan).
```

### Contoh 4 — Release minimal

**Input:** Added Google sign-in.

**Output:**

```markdown
# Acme App — 2 Agustus 2026

- Bisa masuk dengan akun Google.
```

## Cek sebelum kirim

- [ ] Sudah baca dan terapkan `skills/anti-slop-writing/SKILL.md` (baca kalimat aloud — tidak seperti memo / AI)
- [ ] Setiap fitur/perbaikan penting punya bullet sendiri — tidak digabung sembarangan
- [ ] Tanpa istilah teknis yang tidak dijelaskan
- [ ] Item **Perbaikan** punya behaviour sebelumnya + sekarang (format `Sebelumnya …. Sekarang …`, tanpa em dash)
- [ ] Struktur jelas (Sorotan / subjudul area jika banyak item)
- [ ] Tidak ada duplikat antar section
- [ ] Versi atau tanggal ada jika user sudah beri

## Rules

- **MUST** baca `skills/anti-slop-writing/SKILL.md` sebelum menulis dan sebelum mengirim changelog.
- **MUST** tulis untuk pembaca non-teknis kecuali user minta changelog developer.
- **MUST** Bahasa Indonesia sebagai default.
- **MUST** jelaskan hasil, bukan implementasi.
- **MUST** satu bullet per fitur atau perbaikan penting — jangan hilangkan item hanya demi pendek.
- **MUST** kelompokkan per area produk jika satu section punya 5+ item.
- **MUST** tiap item Perbaikan sebut behaviour **sebelumnya** dan **sekarang** (dua kalimat, dipisah titik).
- **MUST** tiap bullet singkat. Perbaikan: dua kalimat pendek; Baru/Peningkatan: satu kalimat.
- **NEVER** pakai em dash `—` di teks bullet (ikut banlist anti-slop-writing).
- **NEVER** paste commit message mentah jika berisi jargon.
- **NEVER** sertakan path file, nama class, atau ID tiket kecuali user minta.
- **NEVER** isi dengan filler ("kami sangat antusias", "berbagai perbaikan bug dan peningkatan").

## References

- [anti-slop-writing](../anti-slop-writing/SKILL.md) — voice, anti-AI banlist, sapaan, dan polish Bahasa Indonesia untuk tiap bullet changelog
- [/refine-ux-writing](../../commands/refine-ux-writing.md) — command trigger ke skill di atas
