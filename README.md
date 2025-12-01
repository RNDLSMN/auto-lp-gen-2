# auto-lp-gen-2

Auto Generate Landing Page - Generator otomatis untuk membuat halaman landing page menggunakan template HTML dan konfigurasi dinamis.

## Fitur

- Generate landing page otomatis dari template HTML
- Support multiple brands dan domains
- Integrasi dengan Cloudinary untuk manajemen gambar
- Generate sitemap XML otomatis
- Template dinamis dengan Jinja2
- Spintax support untuk variasi konten

## Persyaratan

- Python 3.6 atau lebih baru
- pip (Python package installer)

## Instalasi

1. Clone repository:
```bash
git clone https://github.com/RNDLSMN/auto-lp-gen-2.git
cd auto-lp-gen-2
```

2. Buat virtual environment (disarankan):
```bash
python3 -m venv venv
source venv/bin/activate  # Untuk macOS/Linux
# atau
venv\Scripts\activate  # Untuk Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Struktur Proyek

```
auto-lp-gen-2/
├── vndal-lp.py              # Script utama generator
├── requirements.txt         # Dependencies Python
├── brands-slot.txt          # Konfigurasi brands untuk slot
├── brands.txt               # Daftar brands
├── domains.txt              # Daftar domains
├── sitemap-cg.txt           # Template sitemap
├── temp-1.html             # Template HTML 1
├── temp-2.html             # Template HTML 2
├── temp-3.html             # Template HTML 3
├── temp-4.html             # Template HTML 4
└── tutor-dari-awal-proper.md  # Dokumentasi lengkap
```

## Penggunaan

1. Konfigurasi file:
   - Edit `brands-slot.txt` untuk mengatur brands
   - Edit `domains.txt` untuk mengatur domains
   - Edit template HTML (`temp-1.html` hingga `temp-4.html`) sesuai kebutuhan

2. Jalankan script:
```bash
python vndal-lp.py
```

3. Output akan di-generate di folder sesuai dengan domain dan brand yang dikonfigurasi.

## Dependencies

- `jinja2` - Template engine untuk HTML
- `cloudinary` - Manajemen gambar dan assets
- `spintax` - Support untuk spintax syntax
- `colorutils` - Utility untuk manipulasi warna

## Dokumentasi

Untuk dokumentasi lengkap, lihat file `tutor-dari-awal-proper.md`.

## Lisensi

Proyek ini adalah private project.
