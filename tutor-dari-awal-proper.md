# Dokumentasi Proyek Generator Halaman HTML

## Daftar Isi
1. [Persiapan Lingkungan](#persiapan-lingkungan)
2. [Instalasi](#instalasi)
3. [Struktur Proyek](#struktur-proyek)
4. [Penggunaan](#penggunaan)
5. [Troubleshooting](#troubleshooting)

## Persiapan Lingkungan

### Prasyarat
- Python 3.6 atau lebih baru
- pip (Python package installer)

### Membuat Virtual Environment (Opsional tapi Disarankan)

## Instalasi

1. Clone repositori atau buat folder proyek baru:
   ```bash
   mkdir proyek-template-html
   cd proyek-template-html
   ```

2. Buat file `requirements.txt` dengan isi berikut:
   ```bash
   jinja2
   cloudinary
   spintax
   colorutils
   ```

3. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```

## Struktur Proyek

Pastikan Anda memiliki struktur file sebagai berikut:
```
proyek-template-html/
│
├── generate_pages.py
├── requirements.txt
├── domains.txt
├── brands-slot.txt
├── temp-1.html
├── temp-2.html
├── temp-3.html
└── temp-4.html
```

## Penggunaan

1. Siapkan file input:
   - `domains.txt`: Daftar domain, satu per baris
   - `brands.txt`: Daftar merek, satu per baris

2. Jalankan script:
   ```bash
   python generate_pages.py
   ```

3. Ikuti petunjuk di layar:
   - Masukkan nama folder output
   - Pilih jumlah halaman per domain
   - Pilih opsi template (1-5)
   - Masukkan domain untuk AMP dan nama halaman AMP jika diminta

4. Hasil akan disimpan di folder `html-[nama_folder]`

## Troubleshooting

- **Modul tidak ditemukan**: Pastikan semua dependensi terinstal dengan benar. Jika masih bermasalah, coba instal ulang modul tersebut:
  ```bash
  pip install [nama_modul]
  ```

- **Kesalahan izin file**: Pastikan Anda memiliki hak akses yang cukup untuk membaca/menulis di direktori proyek.

- **Masalah koneksi Cloudinary**: Periksa kredensial Cloudinary Anda dan pastikan koneksi internet stabil.

- **Template tidak ditemukan**: Pastikan file template HTML (`temp-1.html`, `temp-2.html`, dll.) berada di direktori yang benar.

Untuk bantuan lebih lanjut, silakan buka issue di repositori GitHub proyek ini atau hubungi pengembang.