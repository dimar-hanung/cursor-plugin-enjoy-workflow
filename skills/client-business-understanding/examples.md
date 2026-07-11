# Contoh Penggunaan

## Contoh 1: Client minta fitur (input minim)

**Input user:**
> Client bilang: "Kami butuh fitur export Excel di dashboard penjualan."

**Output singkat (cuplikan):**

### Interpretasi
- **Permintaan literal:** tombol export Excel
- **Masalah yang mungkin:** laporan penjualan sulit dibuat/dibagikan ke manajemen
- **⚠️ Kemungkinan solusi, belum masalah terverifikasi**

### Pertanyaan prioritas tinggi
1. Siapa yang memakai laporan penjualan ini, dan untuk keputusan apa?
2. Sekarang laporan dibuat bagaimana — manual dari sistem lain, atau copy-paste?
3. Bisa contoh file Excel yang Anda harapkan (kolom dan periodenya)?
4. Seberapa sering laporan ini dibutuhkan — harian, mingguan, ad-hoc?
5. Apakah yang penting format Excel, atau yang penting datanya cepat sampai ke orang yang tepat?

### Kalimat validasi
> "Jadi kebutuhan utamanya memudahkan tim mendapatkan data penjualan dalam format yang bisa dibagikan — apakah export Excel memang wajib, atau format lain (PDF/email otomatis) juga boleh asal prosesnya lebih cepat?"

---

## Contoh 2: Proses approval (input meeting)

**Input user:**
> Meeting dengan HR: karyawan ajukan cuti lewat email ke atasan, HR input manual ke spreadsheet, sering telat update dan bentrok jatah cuti.

**SIPOC:**

| | |
|---|---|
| Supplier | Karyawan, atasan |
| Input | Form email cuti, keputusan approve/reject |
| Process | Ajukan → approve atasan → HR catat → update jatah |
| Output | Jatah cuti terupdate, arsip cuti |
| Customer | HR, payroll, karyawan |

### Pertanyaan prioritas tinggi
1. Setelah atasan approve, apa yang HR lakukan persisnya di spreadsheet?
2. Bagaimana cara cek jatah cuti hari ini — manual hitung atau ada rumus?
3. Kasus "bentrok jatah" — contoh konkret terakhir kali?
4. Apakah semua jenis cuti (tahunan, sakit, unpaid) aturannya sama?
5. Siapa yang perlu notifikasi saat status cuti berubah?

---

## Contoh 3: Input sangat minim

**Input user:**
> "Client mau sistem inventory."

**3 hipotesis:**

| # | Hipotesis | Pertanyaan pembeda |
|---|-----------|-------------------|
| 1 | Stok sering tidak akurat vs fisik | Seberapa sering stock opname? Selisih tipikal berapa? |
| 2 | Gudang & penjualan pakai tools terpisah | Sistem apa yang dipakai sekarang untuk jual dan stok? |
| 3 | Pertumbuhan SKU — Excel tidak skala | Berapa SKU aktif? Siapa yang update stok harian? |

**Langkah berikutnya:** kirim 4–5 pertanyaan prioritas tinggi sebelum bicara modul inventory.
