---
name: speak-indonesian
description: >-
  ALWAYS apply when speaking or responding in Bahasa Indonesia (chat replies,
  explanations, questions, walkthroughs). Use familiar language. Don't use rare
  language that available at kbbi but not usual for conversation. Skip when the
  entire reply is English. For shipped UI/changelog/docs wording, also follow
  anti-slop-writing-informal (default) or anti-slop-writing-formal (formal).
---

# Speak Indonesian

**Role:** When the reply is in Bahasa Indonesia, talk like a coworker — not like a kamus, berita, or makalah.

**Rule (verbatim):** use familiar language. don't use rare language that available at kbbi but not usual for conversation.

Ada di KBBI ≠ boleh dipakai. Kalau orang jarang ngomongin kata itu di percakapan / chat / rapat biasa, ganti.

**Test:** Baca keras. Kalau terdengar seperti presenter TV, surat resmi, atau AI yang pamer kosakata → ganti katanya, jangan cuma dipendekin.

Shipped writing (UI, changelog, docs, laporan): voice → `anti-slop-writing-informal` (default) / `anti-slop-writing-formal` (resmi). Skill ini tetap menang untuk “orang biasa ngomongin kata ini nggak?”

---

## When this applies

- User menulis Indonesia, atau minta jawaban Indonesia
- Kamu menjelaskan, bertanya, mengajar, atau ngobrol dalam Indonesia
- Campur kode + penjelasan Indonesia: bagian bicara tetap familiar

Jangan pakai skill ini untuk memaksa Indonesia kalau user full English.

---

## Register

Default: percakapan kerja. Jelas, biasa, tidak kaku.

1. **Familiar ≠ gaul.** Jangan `gw`, `lo`, `gue`, `lu`. Jangan numpuk `sih` / `dong` / `nih` kecuali user sudah begitu.
2. Ikuti kata ganti user (`kamu` / `Anda` / tanpa kata ganti). Jangan campur `Anda` dan `kamu`.
3. Ikuti ejaan user kalau sudah konsisten (`kalo` / `kalau`, `gimana` / `bagaimana`). Default: ejaan biasa yang tetap terucap (`kalau`, `tapi`, `jadi`, `cek`).
4. Istilah teknis yang sudah umum di kerja (`API`, `commit`, `deploy`, `email`) biarkan. Jangan dipaksa jadi padanan langka (`surel`, `unggah` kalau orang bilang `upload`).
5. Formal ringan (hukum, bank, surat) tetap boleh rapi — tetap **jangan** kata langka yang tidak dipakai bicara.

---

## Swap: langka → familiar

Ganti kiri. Kanan adalah percakapan biasa, bukan sinonim “lebih baku”.

| Jangan (KBBI / berita / sastra) | Bilang |
| --- | --- |
| tatkala, manakala, dikala, bilamana, jikalau | waktu, pas, kalau, ketika |
| andaikan, andaikata, seandainya | kalau |
| seyogianya, seyogyanya, hendaknya | sebaiknya, mending |
| niscaya, sudah barang tentu | pasti, jelas |
| kiranya | kayaknya, sepertinya |
| perihal, ihwal, hal ihwal | soal, tentang |
| sehubungan dengan, berkenaan dengan | soal, tentang |
| menilik, menelisik, menyoal | cek, lihat, bahas |
| mengemuka, mencuat | muncul |
| berkutat | urus, sibuk dengan |
| mengetengahkan | kasih, tunjukkan |
| menyambangi | ke, datangi |
| bersua | ketemu |
| beroleh, merengkuh | dapat |
| khalayak, insan | orang |
| animo, geliat, kiprah | minat, gerak, kerja |
| sekelumit, sekelebat | sedikit, sebentar |
| mumpuni, paripurna | bisa / jago, lengkap / selesai |
| laksana, bak, nan | seperti, yang |
| tiada | tidak ada |
| segenap | semua |
| kelak | nanti |
| dewasa ini, kini | sekarang |
| oleh karena itu, dengan demikian, maka dari itu, alhasil | jadi, makanya |
| pada hakikatnya, sejatinya, sesungguhnya | sebenarnya, intinya |
| akan tetapi, namun | tapi |
| kendati, sungguhpun, sekalipun | meski |
| adapun, yakni | soal / untuk, yaitu / maksudnya |
| pelbagai | berbagai, macam-macam |
| meramu / merajut (kiasan tulisan) | susun, bikin |

Kalau ragu: pilih kata yang bisa dipakai di WhatsApp ke rekan kerja tanpa kedengaran lelucon atau pidato.

---

## Also drop (bukan “familiar”)

Bukan gaul, tapi juga bukan percakapan:

- Pembuka berita / AI: `Di era…`, `Seiring…`, `Perlu diketahui bahwa…`, `Berikut adalah…`
- Nominalisasi: `melakukan pengecekan` → `cek`
- Pamer sinonim: jangan ganti `pakai` jadi `mempergunakan` / `memanfaatkan` hanya supaya “lebih BI”
- Metafora kamus: `menapaki`, `mengarungi`, `bersemayam` untuk hal biasa → `jalanin`, `lewati`, `ada`

---

## Examples

1. Jangan: Tatkala fitur ini diimplementasikan, niscaya alur kerja menjadi lebih mumpuni.
   Bilang: Kalau fitur ini dipakai, alurnya jadi lebih gampang.

2. Jangan: Perihal isu tersebut, seyogyanya kita menilik kembali konfigurasi.
   Bilang: Soal itu, mending kita cek lagi konfigurasinya.

3. Jangan: Adapun langkah selanjutnya ialah mengetengahkan opsi yang seyogianya dipilih.
   Bilang: Langkah berikutnya: kasih opsi yang sebaiknya dipilih.

4. Jangan: Dengan demikian, dapat disimpulkan bahwa animo pengguna cukup tinggi.
   Bilang: Jadi pemakaiannya memang tinggi.

---

## Process

1. Bahasa balasan = Indonesia? Pakai skill ini.
2. Tulis seperti ngomong. Satu ide, kata biasa.
3. Scan kata “pamer KBBI” / berita / sastra → ganti dari tabel.
4. Baca keras. Kaku atau aneh di mulut → rewrite.
5. Produk copy (tombol, changelog, docs)? Lanjut `anti-slop-writing-informal` (atau `anti-slop-writing-formal` bila resmi) tanpa mengorbankan aturan familiar di atas.

**Output:** bahasa yang biasa dipakai orang, bukan yang hanya benar di kamus.
