# Indonesian banlist (formal & semi-formal surfaces)

Adapted from [adenaufal/anti-slop-writing](https://github.com/adenaufal/anti-slop-writing) `indonesian/references/vocabulary-banlist.md` (v3). Prefer **plain verbs + facts** over synonym swaps.

Use for UI, changelog, reports, docs, and professional Indonesian. Cut anything that does not carry new information. Casual/personal register → `anti-slop-writing-informal`.

## Significance puffers — drop or prove

1. `sangat penting` / `krusial` / `signifikan` / `relevan`
   1. Prefer: say why it matters in one short clause, or cut
2. `fundamental` / `mendasar` (pujian samar)
   1. Prefer: name the concrete foundation
3. `luar biasa` / `mendalam` / `berarti` (pujian samar)
   1. Prefer: name the concrete result

## Analytical verbs AI overuses

1. `menyoroti` / `menggarisbawahi`
   1. Prefer: tunjukkan fakta / hapus meta
2. `memfasilitasi`
   1. Prefer: bantu / memungkinkan
3. `mengoptimalkan`
   1. Prefer: perbaiki [apa]
4. `mengimplementasikan`
   1. Prefer: terapkan / jalankan
5. `berkontribusi pada` / `berperan dalam`
   1. Prefer: verb konkret + hasil
6. `berperan … dalam membentuk` (trigram 2026)
   1. Prefer: hapus; sebut apa yang benar-benar dilakukan
7. `mengedepankan` / `mewujudkan` / `merealisasikan`
   1. Prefer: buat / utamakan / simpan
8. `memanfaatkan` (kalau hanya “pakai”)
   1. Prefer: pakai / gunakan
9. `menyelami` (padanan “delve”)
   1. Prefer: langsung ke isi
10. `memastikan` (padding “ensuring”, 2026)
    1. Prefer: tindakan konkret — enkripsi / validasi / simpan

## Formal connectives — prefer plain

1. `selain itu`
   1. Prefer: juga / kalimat baru
2. `di sisi lain`
   1. Prefer: tapi / namun (sekali saja)
3. `lebih lanjut` / `dengan demikian` / `oleh karena itu`
   1. Prefer: jadi / karena itu / potong
4. `tak kalah penting` / `menariknya`
   1. Prefer: langsung ke fakta
5. `sehubungan dengan` / `berkaitan dengan` / `dalam hal ini`
   1. Prefer: spesifik atau potong
6. `dalam rangka` / `dalam upaya` / `guna meningkatkan`
   1. Prefer: untuk + verb
7. `meskipun demikian` / `namun perlu diingat bahwa`
   1. Prefer: tapi / potong

Heavy connectives are worse in UI; in reports, use sparingly and never as empty pivots.

## Puffery & buzzwords (ID)

Never as vague praise:

`komprehensif`, `holistik`, `inovatif`, `dinamis`, `inklusif`, `berbagai macam`, `beragam` (tanpa daftar), `terkini` (tanpa tanggal), `transformasi digital`, `ekosistem` (figuratif), `paradigma`, `optimalisasi`, `sinergi`, `lanskap` (kalke), `kompleksitas` / `dinamika` (tanpa jelaskan apa), `berkelanjutan` (buzzword kosong)

## Copula avoidance

1. `merupakan`
   1. Prefer: adalah / susun ulang
2. `berperan sebagai` / `berfungsi sebagai`
   1. Prefer: adalah / dipakai untuk
3. `menjadi salah satu… yang paling…`
   1. Prefer: angka / perbandingan konkret
4. `memiliki peran penting`
   1. Prefer: sebut peran spesifik

## Epistemic padding (reports especially)

1. `dapat dilihat bahwa` / `dapat dipahami bahwa`
   1. Prefer: langsung ke angka atau fakta
2. `perlu dipahami bahwa` / `perlu diketahui bahwa`
   1. Prefer: potong; nyatakan isinya
3. `hal ini menunjukkan betapa pentingnya`
   1. Prefer: nyatakan faktanya

## Opening / closing crutches

Never:

- Di era modern ini… / Seiring perkembangan zaman…
- Dalam konteks [X] yang semakin [Y]…
- Perlu diketahui bahwa / Penting untuk diingat
- Sebagai kesimpulan / Dapat disimpulkan bahwa / Dengan demikian, dapat disimpulkan
- Pada akhirnya… (kecuali urutan langkah sungguhan)
- Tantangan dan peluang / Prospek masa depan (formula kosong)
- Semoga membantu! / Tentu saja! / Baik, berikut adalah…
- Apakah ada yang ingin Anda tanyakan?
- Sebagai AI, saya…

## Formula pairs — never together

- tantangan dan peluang
- di satu sisi… di sisi lain…
- kelebihan dan kekurangan (pasangan kosong)
- tidak hanya… tetapi juga…

## Symmetric hooks (BI-11) — never as openers

- Banyak orang mengira X. Kenyataannya Y.
- Lupakan X. Fokus ke Y.
- Ini bukan soal X. Ini soal Y. / Bukan soal X. Ini soal Y.

## Hedging / 2026 closers (reports especially)

Cut clusters and empty closers:

- pada intinya / pada dasarnya / secara fundamental / perlu dicatat
- nuansa / bernuansa (pujian samar)
- Meskipun…, secara umum, dalam banyak kasus, perlu dicatat bahwa… (hedge stack)
- satu hal yang pasti / satu hal yang jelas / intinya adalah
- ketegangan inheren / ini memunculkan pertanyaan penting tentang

## EN calques (2025–2026)

Cut or rewrite: ensuring / memastikan yang…, plays a role in / berperan dalam membentuk, seamless, unlock, supercharge, highlighting / menyoroti (meta), empty intensifiers: secara signifikan / secara efektif / semakin (tanpa angka).

Also: `mampu untuk X` → verb langsung; sentence-start `sebaliknya` → `tapi` or restructure; overused `alih-alih` → rewrite the comparison.

## Collaborative chat artifacts

Never in UI, changelog, or shipped reports: Semoga membantu!, Tentu saja!, Baik berikut adalah…, Jangan ragu untuk bertanya, Sebagai AI…

## UI chrome — never as the user’s noun

1. `card` / `kartu` / `tampilan kartu` for a UI tile (kanban, dashboard widget, card view)
   1. Prefer: name the object (`tugas`, `item`, `catatan`, `tiket`…) or omit (`Tambah`, `Belum ada apa-apa di sini`)
   2. View toggle: `Daftar` / `Grid` (or icon-only) — not `Tampilan kartu`
   3. Keep `kartu` only for payment/ID: `kartu kredit`, `nomor kartu`, `kartu debit`
   4. Do not keep English `card` in Indonesian UI as a substitute — both are weird for a tile

## Replacement rule

Do not synonym-hunt. Restructure:

- AI: “Festival ini merupakan salah satu momen penting yang tidak hanya menampilkan kekayaan budaya, tetapi juga memperkuat kohesi sosial.”
- Human: “Festival ini jalan sejak 1987. Warga bikin lapak sendiri. Keju kambing habis sebelum siang.”
