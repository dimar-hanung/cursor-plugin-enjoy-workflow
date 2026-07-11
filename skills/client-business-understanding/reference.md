# Referensi: Framework & Bank Pertanyaan

## SIPOC — template cepat

| Elemen | Isi | Pertanyaan bantu |
|--------|-----|------------------|
| **S**upplier | Siapa sumber input? | Dari siapa data/bahan ini datang? |
| **I**nput | Apa yang masuk? | Dokumen, data, atau keputusan apa yang dibutuhkan? |
| **P**rocess | Langkah utama (5–7) | Urutkan langkah dari awal sampai selesai |
| **O**utput | Hasil akhir | Apa deliverable-nya? Format? |
| **C**ustomer | Penerima hasil | Siapa yang pakai hasil ini? Untuk apa? |

## 5 Whys — contoh pola

```
Permintaan: "Butuh export Excel"
→ Kenapa? Laporan harian susah dibuat
→ Kenapa? Data di 3 sistem terpisah
→ Kenapa? Tidak ada integrasi
→ Kebutuhan mungkin: agregasi data / dashboard, bukan tombol export
```

Stop saat sampai **masalah bisnis** (bukan gejala teknis).

## JTBD — format

> Ketika **[situasi]**, saya ingin **[motivasi/aksi]**, supaya **[hasil yang diinginkan]**.

## MoSCoW — kriteria singkat

| Level | Arti |
|-------|------|
| Must | Tanpa ini proses gagal / tidak bisa go-live |
| Should | Penting, bisa ditunda 1 fase |
| Could | Nice to have |
| Won't | Di luar scope sekarang — catat untuk nanti |

---

## Bank pertanyaan per tema

### Konteks & tujuan bisnis

- Apa tujuan utama proyek ini untuk bisnis Anda?
- Siapa yang paling terdampak jika proses ini tidak berjalan baik?
- Apakah ada target waktu atau deadline bisnis (bukan deadline teknis)?
- Metrik apa yang dipakai untuk bilang "ini sudah berhasil"?

### Proses saat ini (as-is)

- Bisa jelaskan langkah demi langkah dari awal sampai selesai?
- Siapa saja yang terlibat di setiap langkah?
- Alat/sistem apa yang dipakai sekarang (termasuk Excel, WhatsApp, kertas)?
- Berapa lama proses ini biasanya? Di bagian mana paling lama?
- Ceritakan kejadian terakhir kali proses ini bermasalah — apa yang terjadi?

### Masalah & prioritas

- Apa 1–3 hal yang paling mengganggu hari ini?
- Kalau hanya satu hal yang bisa diperbaiki dulu, yang mana?
- Apakah masalahnya frekuensi (sering) atau dampak (jarang tapi besar)?
- Sudah pernah coba solusi lain? Kenapa tidak cocok?

### Hasil yang diharapkan (to-be)

- Setelah selesai, seperti apa keseharian tim Anda?
- Siapa yang akan memakai hasil ini setiap hari?
- Apa yang **tidak boleh** berubah dari cara kerja sekarang?
- Contoh output ideal — ada dokumen/screenshot/contoh data?

### Aturan, approval, edge case

- Siapa yang boleh approve / reject?
- Apa yang terjadi jika data salah atau tidak lengkap?
- Apakah ada aturan regulasi, audit, atau kebijakan internal?
- Volume: berapa transaksi/kasus per hari atau bulan?
- Apakah ada musim ramai atau puncak beban tertentu?

### Integrasi & data

- Sistem apa saja yang harus terhubung?
- Data master ada di mana? Siapa pemilik data?
- Apakah data harus real-time atau boleh batch harian?

### Scope & constraint

- Apa yang **sengaja tidak** masuk scope fase ini?
- Ada budget, timeline, atau kebatasan teknologi yang sudah pasti?
- Siapa decision maker final kalau ada perdebatan requirement?

---

## Kalimat validasi — pola

Gunakan setelah analisis:

> "Jadi pemahaman saya: [ringkasan proses]. Masalah utamanya [X]. Yang Anda harapkan adalah [Y]. Apakah ini sudah sesuai, atau ada yang perlu dikoreksi?"

> "Saya tangkap prioritas pertama adalah [A], baru [B]. Benar begitu urutannya?"

---

## Diagram alur teks (alternatif BPMN ringkas)

```
[Trigger] → [Langkah 1: Peran A] → {Keputusan?}
                ├ Ya → [Langkah 2]
                └ Tidak → [Langkah alternatif] → [Selesai]
```

Gunakan ketika ada cabang keputusan atau beberapa peran.
