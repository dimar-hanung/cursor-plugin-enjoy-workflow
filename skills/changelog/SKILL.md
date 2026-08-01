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
| Skill ini | Struktur, nested list modul, format Perbaikan |

## Sebelum menulis

1. Baca `anti-slop-writing` → polish tiap bullet.
2. Kumpulkan perubahan (input, diff, commit, PR). Tanya versi/tanggal jika belum jelas.
3. Filter internal: refactor, CI, deps — skip kecuali changelog teknis.
4. Map tiap item ke **modul/fitur + konteks lokasi** (nama UI, bukan `auth-service`).

## Aturan inti

| Lakukan | Hindari |
|---------|---------|
| Manfaat / behaviour yang user alami | File, API, stack, root cause teknis |
| Kata sehari-hari | deploy, refactor, endpoint |
| Satu fitur/fix = satu nested bullet | Paragraf, gabung fitur berbeda |
| Spesifik | "berbagai perbaikan", filler marketing |
| Nested list modul (`1.` + `-`) | Heading `###` untuk modul, flat bullet tanpa modul |

**Panjang:** Baru/Peningkatan → 1 kalimat. Perbaikan → `Sebelumnya …. Sekarang …` (dua kalimat, titik, **tanpa em dash**).

**Nada:** ramah, langsung. Baru/Peningkatan front-load manfaat (`Sekarang bisa…`). Perbaikan boleh mulai dari behaviour sebelumnya.

## Struktur

```markdown
# [Produk] — [Versi/tanggal]

**Sorotan** *(opsional, 2–4 item)*
- [Modul/konteks]: [item penting]

## Baru | Peningkatan | Perbaikan

1. [Modul/Fitur + konteks]
   - [perubahan]
```

| Level | Isi |
|-------|-----|
| `##` | Baru, Peningkatan, Perbaikan (opsional: Perubahan, Dihapus) |
| `1.` | Label modul/fitur + konteks lokasi |
| `-` | Satu perubahan per bullet |

**Sorotan** *(opsional, 2–4 item jika banyak perubahan):* flat bullet, prefiks modul — `Laporan: bisa diunduh PDF.` Cuplikan saja; daftar lengkap tetap di bawah.

## Label modul & konteks

Nama dari UI/navigasi user. **Ordered nested list** — tidak pakai `###`.

**Fitur sama, beda tempat** → tiap tempat = entri `1.` sendiri, label lengkap:

| Pola | Contoh `1.` |
|------|-------------|
| Area tunggal | `Laporan`, `Akun` |
| Fitur di modul | `Pembayaran di Fasilitas A` |
| Fitur pada konteks | `Notifikasi pada Chat Grup` |
| Fitur pada sub-fitur | `Notifikasi pada Pembayaran di Fasilitas A` |

`di` = modul/lokasi · `pada` = konteks di dalamnya.

| Lakukan | Hindari |
|---------|---------|
| Satu konteks = satu `1.` label lengkap | Satu `1. Notifikasi` untuk semua tempat |
| Label `1.` = lokasi; bullet = perubahan | Ulang konteks panjang di bullet |

Gabung hanya perbaikan kecil sejenis dalam satu nested bullet di modul yang sama.

## Format Perbaikan (wajib)

Tiap item: behaviour **sebelumnya** + **sekarang**.

```markdown
1. Masuk
   - Sebelumnya macet di layar login. Sekarang langsung ke halaman yang benar.
```

Variasi singkat: `…sekarang benar (sebelumnya sering beda satu hari).`

## Workflow

1. Baca anti-slop-writing → 2. Catat semua perubahan → 3. Map modul + konteks → 4. Buang internal → 5. Terjemahkan (hasil, bukan implementasi) → 6. Kelompokkan Baru/Peningkatan/Perbaikan → 7. Nested list `1.` + `-` → 8. Sorotan opsional → 9. Judul + polish (aloud test, no em dash)

## Contoh

```markdown
# Acme App — Maret 2026

## Baru
1. Pengaturan
   - Mode gelap bisa diaktifkan dari sini.

## Perbaikan
1. Masuk
   - Sebelumnya tetap di layar login. Sekarang langsung ke halaman yang benar.
```

**Fitur sama, beda konteks:**

```markdown
# Campus App — v2.1

## Baru
1. Pembayaran di Fasilitas A
   - Bisa bayar cicilan per bulan.
2. Notifikasi pada Chat Grup
   - Push saat ada pesan baru di grup.
3. Notifikasi pada Pembayaran di Fasilitas A
   - Email konfirmasi setelah pembayaran berhasil.

## Perbaikan
1. Notifikasi pada Chat Grup
   - Sebelumnya push telat beberapa menit. Sekarang langsung setelah pesan masuk.
```

## Cek sebelum kirim

- [ ] anti-slop-writing diterapkan (baca aloud)
- [ ] Nested list `1.` + `-`; tidak ada `###` untuk modul
- [ ] Label `1.` = modul + konteks jika fitur sama beda tempat
- [ ] Modul wajib di setiap item
- [ ] Perbaikan: sebelumnya + sekarang; tanpa em dash
- [ ] Satu bullet per fitur/fix penting; tanpa jargon/commit mentah

## Rules

**MUST:** anti-slop-writing · Indonesia · hasil bukan implementasi · nested list modul · label konteks lengkap jika fitur sama beda tempat · satu bullet per item · Perbaikan sebelum+sesudah · nama UI bukan internal.

**NEVER:** `###` modul · flat bullet tanpa modul · gabung konteks under label generik · em dash di bullet · jargon/path/tiket · filler · paste commit mentah.

## References

- [anti-slop-writing](../anti-slop-writing/SKILL.md) — voice, banlist, polish
