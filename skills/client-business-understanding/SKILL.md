---
name: client-business-understanding
description: Membantu mengurai maksud client, memetakan proses bisnis, dan menyusun pertanyaan klarifikasi. Gunakan saat user kesulitan memahami kebutuhan client, proses bisnis, requirement tidak jelas, hasil meeting dengan client, atau meminta bantuan menyusun pertanyaan ke client.
---

# Memahami Proses Bisnis Client

Bantu user **mengerti apa yang client maksud** — bukan langsung loncat ke solusi teknis.

Bahasa respons: **Indonesia**, kecuali user minta Inggris. Nada: jelas, praktis, tidak akademis berlebihan.

## Workflow

Ikuti urutan ini setiap kali skill dipakai:

```
1. Terima input     → catatan meeting, chat client, brief, atau cerita user
2. Pisahkan lapisan → permintaan / masalah / asumsi / yang belum jelas
3. Pilih framework  → sesuai kompleksitas (lihat bawah)
4. Susun output     → pakai template wajib
5. Buat pertanyaan  → prioritas tinggi dulu, siap kirim ke client
```

Jangan asumsikan detail yang tidak disebutkan. Tandai eksplisit: **Diketahui** vs **Asumsi** vs **Belum jelas**.

## Pilih framework

| Situasi | Framework | Output singkat |
|---------|-----------|----------------|
| Proses baru / belum jelas scope | SIPOC | Supplier, Input, Process, Output, Customer |
| Client minta fitur spesifik | 5 Whys + JTBD | Akar masalah + kalimat "Ketika… saya ingin… supaya…" |
| Alur kerja banyak cabang/approval | BPMN ringkas | Langkah berurutan + keputusan + peran |
| Banyak stakeholder / sistem | Context diagram | Sistem, aktor luar, data masuk/keluar |
| Scope melebar / "semua penting" | MoSCoW | Must / Should / Could / Won't (sementara) |

Default untuk input pendek: **5 Whys → SIPOC → pertanyaan klarifikasi**.

Detail framework dan bank pertanyaan: [reference.md](reference.md).  
Contoh lengkap: [examples.md](examples.md).

## Deteksi red flag

Jika client bilang hal seperti ini, **curigai solusi prematur** — gali masalah dulu:

- "Tinggal tambah tombol / fitur X"
- "Sama kayak aplikasi Y"
- "Harusnya sistem otomatis"
- "Semua departemen butuh ini"

Tandai di output: **⚠️ Kemungkinan solusi, belum masalah terverifikasi.**

## Template output wajib

Selalu gunakan struktur ini:

```markdown
## Ringkasan
[2–3 kalimat: apa yang client katakan vs apa yang kemungkinan mereka butuhkan]

## Yang sudah jelas
- [Fakta dari input user — tanpa interpretasi berlebihan]

## Yang belum jelas
- [Gap spesifik — ini dasar pertanyaan ke client]

## Pemetaan proses
[SIPOC / alur langkah / diagram teks — pilih yang paling membantu]

## Interpretasi kebutuhan
**Permintaan literal:** [apa yang mereka minta]
**Masalah yang mungkin:** [hipotesis — tandai sebagai hipotesis]
**Dampak jika salah paham:** [1–2 kalimat risiko]

## Pertanyaan ke client
### Prioritas tinggi (tanyakan dulu)
1. [Pertanyaan terbuka, bahasa client-friendly]
...

### Prioritas menengah
1. ...

### Opsional (jika waktu memungkinkan)
1. ...

## Kalimat validasi (baca balik ke client)
"[Ringkasan dalam bahasa client untuk konfirmasi — minta mereka koreksi jika salah]"

## Langkah berikutnya untuk kamu
1. [Aksi konkret — misalnya: kirim pertanyaan prioritas tinggi, minta contoh dokumen, dll.]
```

## Aturan menyusun pertanyaan

1. **Satu pertanyaan = satu topik** — jangan gabung 3 hal dalam satu kalimat.
2. **Pertanyaan terbuka dulu** ("Ceritakan…", "Bagaimana…") baru tertutup ("Apakah…").
3. **Minta contoh konkret** — "Contoh terakhir kali proses ini gagal/ribet?"
4. **Hindari jargon IT** kecuali client teknis.
5. **Maksimal 5–7 pertanyaan prioritas tinggi** per putaran — jangan overwhelm client.
6. Kelompokkan pertanyaan per tema: **konteks → proses saat ini → masalah → hasil yang diharapkan → batasan**.

## Saat input sangat minim

Jika user hanya memberi 1–2 kalimat:

1. Buat **3 hipotesis** kemungkinan maksud client (berbeda satu sama lain).
2. Untuk tiap hipotesis, tulis **2 pertanyaan** yang membedakan hipotesis tersebut.
3. Jangan pura-pura yakin — katakan apa yang masih perlu diverifikasi.

## Saat user bawa dokumen panjang

1. Ekstrak dulu: aktor, proses, pain point, constraint, deadline.
2. Baru peta SIPOC atau alur.
3. Pertanyaan fokus pada **kontradiksi** dan **bagian yang tidak disebut** (siapa approve? edge case? volume data?).

## Yang tidak dilakukan skill ini

- Tidak langsung desain database, API, atau arsitektur kecuali user minta setelah kebutuhan jelas.
- Tidak mengarang requirement yang tidak ada dasarnya di input.
- Tidak mengganti keputusan bisnis user — hanya memperjelas opsi dan risiko salah paham.
