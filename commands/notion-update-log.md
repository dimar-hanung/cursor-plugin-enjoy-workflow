---
name: notion-update-log
description: Update Notion Note (### Pertanyaan, ### Pelajaran umum) lalu Log. Eksperimen wajib Hasil; Pelajaran diawali Ternyata. Bahasa Indonesia, anti-slop. Notion MCP.
---

# Notion Update Log

Update log kerja di Notion. Bahasa: **Indonesia**. Ringkas, mudah discan — bukan paragraf teknis.

**Wajib baca** [anti-slop-writing-informal](../skills/anti-slop-writing-informal/SKILL.md). Voice di situ; struktur di command ini. Konteks resmi → `anti-slop-writing-formal`.

| Yang menang | Surface |
|-------------|---------|
| `anti-slop-writing-informal` | Voice default, titik/koma (bukan `—`); banlist lengkap di `anti-slop-writing-formal` |
| Command ini | `## 📝 Note` lalu `## ⚔️ Log` + label tipe |

## Alur

1. Ambil URL Notion → `notion-fetch`.
2. Kumpulkan kerja (chat/diff/commit). **Tanya tanggal** jika belum jelas.
3. Update `## 📝 Note` jika perlu + tulis entri `## ⚔️ Log`.
4. Polish anti-slop → `notion-update-page` (Note di tempatnya; log baru paling atas di dalam Log).
5. Laporkan singkat: tanggal + pertanyaan/pelajaran + jumlah item.

## Struktur halaman (urut)

1. **`## 📝 Note`** — di atas
   - **`### Pertanyaan`** — terbuka / terjawab
   - **`### Pelajaran`** — insight umum / business rule (**Ternyata** wajib)
2. **`## ⚔️ Log`** — di bawah Note · progress harian (New → Old)

### `## 📝 Note` → `### Pertanyaan`

```markdown
## 📝 Note

### Pertanyaan

- [ ] Apakah semua partner pakai Partner Service ID yang sama?
- [x] Format signature notifikasi sudah sesuai spesifikasi BRI?
   Jawaban: Ya, setelah konfirmasi Zoom tim BRI memakai format tanda tangan dengan timestamp UTC.

### Pelajaran
…
```

- Baru → `- [ ]` di **paling atas**. Terjawab → `- [x]` + indent `Jawaban: …`. Jangan hapus yang terjawab.
- Tidak ada perubahan → jangan ubah section.

### `## 📝 Note` → `### Pelajaran`

Insight **umum** dari kerja — bukan label Log (Investigasi, Perbaikan, Blocker, dll).

Bisa tentang proses teknis, **aturan bisnis / business rule**, sejarah keputusan partner, cara kerja yang ternyata berbeda dari asumsi, pola yang berguna, atau apa saja yang layak diingat. **Setiap `-` selalu diawali `Ternyata,`.**

```markdown
### Pelajaran

- Ternyata, BP3IP dulunya menggunakan BRIVA, bukan SNAP BI.
- Ternyata, semua partner pakai satu Partner Service ID, bukan ID berbeda per partner.
- Ternyata, body request harus compact satu baris di Signature Service dan Client Simulator supaya tanda tangan cocok.
```

Opsional: kelompokkan dengan `1.` konteks jika banyak pelajaran di area yang sama.

```markdown
1. Pembayaran
   - Ternyata, BP3IP dulunya menggunakan BRIVA, bukan SNAP BI.
2. Signature
   - Ternyata, ASPI hash body versi ringkas. Body berformat membuat tanda tangan gagal.
```

| Level | Isi |
|-------|-----|
| `-` | `Ternyata, [insight].` — teknis atau bisnis |
| `1.` | opsional — konteks area jika perlu dikelompokkan |

Pelajaran baru di **paling atas**. Jangan hapus yang lama. Tidak ada insight baru → jangan ubah section.

### `## ⚔️ Log`

Di **bawah** `## 📝 Note`. Entri baru **langsung di bawah** heading `## ⚔️ Log` (New → Old).

```markdown
## ⚔️ Log

### Rabu, 9 Agustus 2026

1. Pembayaran BRI
   - Investigasi, Sebelumnya asumsi error dari signature. Sekarang fokus cek Partner Service ID.
   - Eksperimen, Sekarang uji skenario bayar VA. Hasil: Ada clue, ID harus sama untuk semua partner.
   - Keputusan, Sekarang setuju pakai satu Service ID.
   - Baru, Sekarang laporan VA bisa diuji sampai skenario bayar.
2. Notifikasi pembayaran
   - Eksperimen, Sekarang uji notifikasi di simulator. Hasil: Berhasil, tanda tangan dan token lolos.
   - Perbaikan, Sebelumnya notifikasi ditolak. Sekarang alur sudah lolos uji.
3. OAuth BRI
   - Eksperimen, Sekarang coba direct sandbox. Hasil: Buntu, masih ditolak tanpa petunjuk jelas.
   - Blocker, Sebelumnya lanjut uji mandiri. Sekarang menunggu jawaban BRI.
```

| Level | Isi |
|-------|-----|
| `###` | `### [Hari], [d] [Bulan] [yyyy]` — plain, tanpa emoji. Jam opsional di akhir |
| `1.` | Konteks (dimana / untuk siapa / ketika apa) |
| `-` | Label tipe + isi |

Buat section jika belum ada. Jangan tulis log di luar `## ⚔️ Log`. Jangan pindahkan Log di atas Note.
## Label tipe

### Log saja (`## ⚔️ Log`)

**Progress:** Eksperimen · Investigasi · Temuan · Koordinasi · Blocker · Keputusan  
**Hasil:** Baru · Perbaikan · Improvement · Dihapus · Berubah

| Label | Format |
|-------|--------|
| **Eksperimen** | `Eksperimen, … Hasil: Buntu \| Ada clue \| Berhasil, …` (**hasil wajib**) |
| **Investigasi / Blocker** | `…, Sebelumnya …. Sekarang ….` |
| **Temuan / Koordinasi / Keputusan / Baru** | `…, Sekarang …` |
| **Perbaikan / Dihapus / Berubah** | `…, Sebelumnya …. Sekarang ….` |
| **Improvement** | kontras atau `Sekarang …` |

### Pelajaran saja (`### Pelajaran`)

Insight umum — teknis **atau** business rule. Bukan kategori Log.

```text
- Ternyata, [insight].
```

Contoh bisnis: `Ternyata, BP3IP dulunya menggunakan BRIVA, bukan SNAP BI.`

Titik untuk pisah kalimat. Tanpa em dash. Tanpa label Progress/Hasil.

## Aturan isi

| Lakukan | Hindari |
|---------|---------|
| Ringkas, bahasa sehari-hari | Dump debug, wall of text |
| Satu perubahan = satu `-` | Label generik (`Update`, `Fix`) |
| Terjemahkan jargon ke dampak | Env, secret, path, kode HTTP mentah |

## Notion MCP

1. `notion-fetch` → pastikan `## 📝 Note` lalu `## ⚔️ Log` (buat jika perlu; **Note di atas, Log di bawah**).
2. Update `### Pertanyaan` / `### Pelajaran` tanpa menghapus history.
3. Sisipkan log baru paling atas di `## ⚔️ Log`.
4. Jangan rewrite seluruh halaman kecuali diminta.

## Cek sebelum kirim

- [ ] anti-slop · ringkas · tanpa em dash
- [ ] Log: tanggal `### Hari, d Bulan yyyy`, New→Old, `1.` + `-` label tipe
- [ ] **Eksperimen** punya Hasil · **Pelajaran** punya **Ternyata,**
- [ ] Note di-update hanya jika ada perubahan

## Rules

**MUST:** Notion MCP · Indonesia · anti-slop · Note di atas · Log di bawah · label tipe hanya di Log · Pelajaran diawali **Ternyata,** · Eksperimen→Hasil · New→Old · ringkas.

**NEVER:** label Log di Pelajaran · Pelajaran tanpa Ternyata · Log di atas Note · dump teknis · hapus history · rewrite halaman tanpa diminta · em dash · bullet Log tanpa label.

## References

- [anti-slop-writing-informal](../skills/anti-slop-writing-informal/SKILL.md)


USER REQUEST:
