import os
import json
import shutil
import re
import random
import itertools
import spintax
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from colorutils import Color
import xml.etree.ElementTree as ET
from datetime import datetime

# Import the cloudinary.api for managing assets
import cloudinary.api
# Import the cloudinary.uploader for uploading assets
import cloudinary.uploader

cloudinary.config(
    cloud_name="vndal",
    api_key="348255791798544",
    api_secret="Rta3BuDxX1egZO3fA5jrFVRNUh8",
    secure=True
)
def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def create_html_page(template_file, output_file, context):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_file)
    html_output = template.render(context)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_output)

def random_color():
    return '#{:02x}{:02x}{:02x}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def create_sitemap(domain_folder, domain):
    sitemap_root = ET.Element("urlset")
    sitemap_root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    
    url = ET.SubElement(sitemap_root, "url")
    loc = ET.SubElement(url, "loc")
    loc.text = f"https://{domain}/"
    lastmod = ET.SubElement(url, "lastmod")
    lastmod.text = datetime.now().strftime("%Y-%m-%d")
    
    for brand_folder in os.listdir(domain_folder):
        brand_path = os.path.join(domain_folder, brand_folder)
        if os.path.isdir(brand_path):
            url = ET.SubElement(sitemap_root, "url")
            loc = ET.SubElement(url, "loc")
            loc.text = f"https://{domain}/{brand_folder}/"
            lastmod = ET.SubElement(url, "lastmod")
            lastmod.text = datetime.now().strftime("%Y-%m-%d")
    
    sitemap_tree = ET.ElementTree(sitemap_root)
    sitemap_file = os.path.join(domain_folder, "sitemap.xml")
    sitemap_tree.write(sitemap_file, encoding="utf-8", xml_declaration=True)
    print(f"Sitemap dibuat untuk {domain}: {sitemap_file}")

def spintax_brand(brand):
    words = brand.split()
    spintaxed_words = [f"{{{word}|{word.capitalize()}}}" for word in words]
    return " ".join(spintaxed_words)

image_urls = [
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_1.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_2.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_3.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_4.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_5.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_6.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_7.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_8.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_9.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_10.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_11.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_12.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_13.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_14.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238382/vndal_15.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238383/vndal_16.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238383/vndal_17.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238383/vndal_18.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238383/vndal_19.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238383/vndal_20.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238383/vndal_21.jpg",
    "https://res.cloudinary.com/dax42uome/image/upload/t_VNDAL/v1725238383/vndal_22.jpg"
]

colors = [
    "#000000", "#0D1117", "#1A1A1A", "#1E1E1E", "#2C2C2C", "#333333", "#3C3C3C", "#2B2B2B", "#1C2833", "#17202A",
    "#1B2631", "#212F3C", "#2C3E50", "#34495E", "#4A0E4E", "#1A5276", "#117A65", "#7D3C98", "#A93226", "#D35400",
    "#27AE60", "#2980B9", "#8E44AD", "#FF1493", "#00CED1", "#FF4500", "#32CD32", "#4169E1", "#9400D3", "#FF6347",
    "#20B2AA", "#FF69B4", "#1E90FF", "#00FA9A", "#FF8C00", "#00BFFF", "#7B68EE"
]

print('========================================================')
print('''
██╗   ██╗███╗   ██╗██████╗  █████╗ ██╗     
██║   ██║████╗  ██║██╔══██╗██╔══██╗██║     
██║   ██║██╔██╗ ██║██║  ██║███████║██║     
╚██╗ ██╔╝██║╚██╗██║██║  ██║██╔══██║██║     
 ╚████╔╝ ██║ ╚████║██████╔╝██║  ██║███████╗
  ╚═══╝  ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚══════╝
''')
print('VNDAL LP-2.0 Script Berjalan...')
print('========================================================')
inputfoldername = input("\nSilakan masukkan nama folder \nMasukkan nama folder: ").lower()
print('========================================================')

while True:
    try:
        pages_per_domain = int(input("Berapa halaman yang ingin Anda buat per domain? "))
        if pages_per_domain > 0:
            break
        else:
            print("Mohon masukkan angka positif.")
    except ValueError:
        print("Mohon masukkan angka yang valid.")

print('========================================================')

template_choice = input("\nPilih opsi template:\n1. Acak\n2. Template 1\n3. Template 2\n4. Template 3\n5. Template 4\nMasukkan pilihan Anda (1-5): ")
if template_choice == '1':
    template_files = ['temp-1.html', 'temp-2.html', 'temp-3.html', 'temp-4.html']
else:
    template_index = int(template_choice) - 2
    template_files = [f'temp-{template_index + 1}.html']

print('========================================================')

file_root_normal = f'html-{inputfoldername}/'
create_folder_if_not_exists(file_root_normal)

with open('domains.txt', 'r') as f:
    domains = [line.strip() for line in f]

with open('brands-slot.txt', 'r', encoding='utf-8') as f:
    original_brands = [line.strip() for line in f]
    spintaxed_brands = [spintax_brand(brand) for brand in original_brands]

if len(spintaxed_brands) < pages_per_domain:
    spintaxed_brands = (spintaxed_brands * ((pages_per_domain // len(spintaxed_brands)) + 1))[:pages_per_domain]
else:
    spintaxed_brands = spintaxed_brands[:pages_per_domain]

print(f"Jumlah domain: {len(domains)}")
print(f"Jumlah brand yang akan digunakan: {len(spintaxed_brands)}")

for domain in domains:
    domain_folder = os.path.join(file_root_normal, domain)
    create_folder_if_not_exists(domain_folder)

amp_domain = input("Masukkan domain untuk AMP (contoh: amphost.id): ")
amp_page_name = input("Masukkan nama halaman untuk file HTML AMP (contoh: mrmouse): ")
print('========================================================')

buttonUrl = input("Masukkan URL untuk tombol (contoh: https://domain.com/foldermu): ")
print('========================================================')

css_template = """
<style>
.header-announcement-bar-wrapper {
    background: {{ header_color }};
}
.products.collection-content-wrapper.product-layout-side-by-side {
    background-color: {{ products_color }};
}
footer .content-wrapper {
    background: {{ footer_color }};
}
</style>
"""

for template_name in ['temp-1.html', 'temp-2.html', 'temp-3.html', 'temp-4.html']:
    with open(template_name, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '{{ css }}' in content:
        content = content.replace('{{ css }}', css_template)
    else:
        content = content.replace('</head>', css_template + '</head>')
    
    with open(template_name, 'w', encoding='utf-8') as file:
        file.write(content)

total_files_created = 0
amp_counter = 1

for domain in domains:
    domain_folder = os.path.join(file_root_normal, domain)
    domain_files_created = 0
    
    for spintaxed_brand in spintaxed_brands:
        if domain_files_created >= pages_per_domain:
            break
        
        brandName = spintax.spin(spintaxed_brand)
        brandSlug = brandName.replace(" ", "-").lower()
        brand_normalized = brandName.replace("-", " ")
        folder_path = os.path.join(domain_folder, brandSlug)
        create_folder_if_not_exists(folder_path)
        
        output_file = os.path.join(folder_path, "index.html")
        
        if os.path.exists(output_file):
            print(f"File sudah ada: {output_file}")
            continue

        canonicalUrl = f'https://{domain}/{brandSlug}/'
        link = f'https://{domain}/{brandSlug}/'
        amphtml = f'https://{amp_domain}/{amp_page_name}-{amp_counter}/'
        
        title_options = [
            "{{Selamat datang|Sambut|Bergabunglah|Temukan Keseruan}} di {brand_normalized}: {{Petualangan|Pengalaman|Perjalanan|Sensasi}} Slot {{Mewah|Eksklusif|Berkelas|Premium}} Menanti Anda!",
            "{brand_normalized}: {{Rasakan|Alami|Nikmati|Jelajahi}} Sensasi {{Kemewahan|Keistimewaan|Keunggulan|Kelas Atas}} dan {{Keberuntungan|Nasib Baik|Peruntungan|Kesempatan Emas}} dalam Satu {{Pengalaman|Petualangan|Momen|Kesempatan}}",
            "{{Destinasi Utama|Tujuan Favorit|Pilihan Terbaik|Surga Slot}} Slot Online 2024: {brand_normalized} {{Hadir|Muncul|Tampil|Siap Melayani}} untuk Anda",
            "{brand_normalized} - {{Tempat|Lokasi|Situs|Arena}} {{Terbaik|Teratas|Paling Unggul|Paling Menjanjikan}} untuk {{Pencari Keberuntungan|Pemburu Jackpot|Penggemar Slot|Pejuang Kemenangan}} di 2024",
            "{{Jelajahi|Temukan|Rasakan|Nikmati}} Dunia Slot {{Mewah|Eksklusif|Berkelas|Terkemuka}} {brand_normalized} - {{Pengalaman|Sensasi|Keseruan|Petualangan}} Tak Terlupakan Menanti!",
            "{brand_normalized}: {{Wujudkan|Raih|Capai|Gapai}} Impian Anda dalam {{Petualangan|Pengalaman|Perjalanan|Eksplorasi}} Slot Online {{Terbaik|Teratas|Paling Unggul|Paling Menguntungkan}}",
            "{{Bersiaplah|Siap-siap|Persiapkan Diri}} untuk {{Memasuki|Menjelajahi|Mengalami}} Dunia {brand_normalized}: Slot {{Mewah|Eksklusif|Berkelas|Terbaik}} Menanti Anda!",
            "{brand_normalized} - {{Pintu Gerbang|Jalan Masuk|Akses}} Menuju {{Kekayaan|Kemewahan|Keberuntungan|Kesuksesan}} di Dunia Slot Online",
            "{{Temukan|Jelajahi|Rasakan}} Keajaiban Slot di {brand_normalized}: {{Pengalaman|Petualangan|Sensasi}} {{Tak Tertandingi|Luar Biasa|Menakjubkan}}",
            "{brand_normalized}: {{Tempat|Arena|Lokasi}} di mana {{Impian|Harapan|Keinginan}} Bertemu {{Keberuntungan|Kesempatan|Peluang}} dalam Dunia Slot",
            "{{Bergabunglah|Ikuti|Jadilah Bagian}} dari Revolusi Slot Online bersama {brand_normalized} - {{Pengalaman|Sensasi|Keseruan}} Bermain Tanpa Batas",
            "{brand_normalized}: {{Pusat|Surga|Oasis}} {{Kegembiraan|Kesenangan|Hiburan}} Slot Online yang {{Tak Tertandingi|Luar Biasa|Menakjubkan}}",
            "{{Rasakan|Alami|Nikmati}} {{Sensasi|Getaran|Keseruan}} Kemenangan di {brand_normalized} - {{Tempat|Arena|Lokasi}} Slot Online {{Terpercaya|Andal|Terbaik}}",
            "{brand_normalized} - {{Membuka|Menghadirkan|Mempersembahkan}} {{Pintu|Jalan|Akses}} Menuju {{Kekayaan|Kemewahan|Kesuksesan}} di Dunia Slot Online",
            "{{Temukan|Jelajahi|Eksplorasi}} {{Keajaiban|Keunikan|Keistimewaan}} Slot di {brand_normalized}: {{Pengalaman|Petualangan|Sensasi}} yang {{Tak Terlupakan|Mengesankan|Memukau}}",
            "{{Bergabunglah|Ikuti|Jadilah Bagian}} dengan {brand_normalized}: {{Destinasi|Tujuan|Tempat}} Utama untuk {{Petualangan|Pengalaman|Perjalanan}} Slot Online {{Terbaik|Teratas|Paling Unggul}}",
            "{brand_normalized} - {{Wujudkan|Raih|Capai}} Impian Anda dalam Dunia Slot Online yang {{Mempesona|Menakjubkan|Memukau}}",
            "{{Nikmati|Rasakan|Alami}} {{Keseruan|Kegembiraan|Kesenangan}} Tanpa Batas di {brand_normalized} - {{Surga|Oasis|Tempat Ideal}} Slot Online",
            "{{Temukan|Jelajahi|Eksplorasi}} {{Keajaiban|Keunikan|Pesona}} Slot Online di {brand_normalized} - {{Pengalaman|Petualangan|Sensasi}} yang {{Tak Tertandingi|Luar Biasa|Menakjubkan}}",
            "{brand_normalized}: {{Pintu Gerbang|Jalan Masuk|Akses}} Menuju {{Kemenangan|Kesuksesan|Keberuntungan}} di Dunia Slot Online"
        ]
        title_template = random.choice(title_options).format(brand_normalized=brand_normalized)
        title = spintax.spin(title_template)
        
        description_options = [
        "{{Selamat datang|Sambut|Bergabunglah|Temukan keseruan}} di dunia {brand_normalized}, tempat di mana {{petualangan|pengalaman|perjalanan|sensasi}} slot {{mewah|eksklusif|berkelas|premium}} menanti Anda! Apakah Anda siap untuk {{merasakan|mengalami|menikmati|menjelajahi}} sensasi {{kemewahan|keistimewaan|keunggulan|kelas atas}} dan {{keberuntungan|nasib baik|peruntungan|kesempatan emas}} dalam satu {{pengalaman|petualangan|momen|kesempatan}} yang tak terlupakan? {brand_normalized} {{hadir|muncul|tampil|siap melayani}} sebagai {{destinasi utama|tujuan favorit|pilihan terbaik|surga slot}} bagi para {{pencari keberuntungan|pemburu jackpot|penggemar slot|pejuang kemenangan}} yang {{menginginkan|mendambakan|mencari|mengejar}} {{pengalaman|sensasi|keseruan|petualangan}} bermain slot online {{terbaik|teratas|paling unggul|paling menguntungkan}} di tahun 2024.",
            "Bersiaplah untuk {{memasuki|menjelajahi|mengalami|menyelami}} dunia {brand_normalized} yang {{menakjubkan|memukau|mengagumkan|luar biasa}}! Kami menawarkan {{koleksi|rangkaian|pilihan|varian}} permainan slot yang {{luar biasa|istimewa|unik|terbaik}}, dirancang khusus untuk memenuhi selera para pemain yang {{menghargai|mencari|mendambakan|menginginkan}} {{kualitas|keunggulan|keistimewaan|pengalaman terbaik}} dan {{kemewahan|kecanggihan|keunikan|inovasi}}. Dengan {{grafis memukau|visual menawan|tampilan mempesona|desain mengagumkan}}, {{efek suara yang memanjakan telinga|audio berkualitas tinggi|suara yang realistis|atmosfer yang imersif}}, dan {{fitur bonus yang menggiurkan|hadiah melimpah|kejutan menarik|peluang kemenangan besar}}, setiap putaran di {brand_normalized} adalah sebuah {{petualangan mewah|pengalaman eksklusif|momen istimewa|kesempatan emas}} yang menjanjikan {{keseruan|kegembiraan|kepuasan|kenikmatan}} tiada tara.",
            "{brand_normalized} {{mengundang|mengajak|menyambut|mempersilakan}} Anda untuk {{merasakan|mengalami|menikmati|menjelajahi}} sensasi {{bermain slot|berjudi online|mengadu peruntungan|meraih kemenangan}} yang {{tak tertandingi|luar biasa|istimewa|unik}}. Kami {{menyediakan|menawarkan|menghadirkan|mempersembahkan}} {{platform|situs|arena|tempat}} bermain yang {{aman|terpercaya|handal|profesional}}, didukung oleh {{teknologi terkini|inovasi terbaru|sistem canggih|fitur modern}} untuk {{memastikan|menjamin|memberikan|menghadirkan}} {{pengalaman bermain|kenyamanan|keamanan|kepuasan}} yang {{optimal|maksimal|terbaik|luar biasa}} bagi setiap pemain. {{Bergabunglah|Daftarlah|Mulailah|Ikuti}} bersama kami dan {{temukan|rasakan|nikmati|alami}} sendiri {{keseruan|kegembiraan|keunikan|keistimewaan}} bermain di {brand_normalized}!"
        ]
        description_template = random.choice(description_options).format(brand_normalized=brand_normalized)
        description = spintax.spin(description_template)
        
        description2_template = """
        <p style="text-align: justify;">{{Selamat datang|Sambut|Bergabunglah|Temukan keseruan}} di dunia {brand_normalized}, tempat di mana {{petualangan|pengalaman|perjalanan|sensasi}} slot {{mewah|eksklusif|berkelas|premium}} menanti Anda! Apakah Anda siap untuk {{merasakan|mengalami|menikmati|menjelajahi}} sensasi {{kemewahan|keistimewaan|keunggulan|kelas atas}} dan {{keberuntungan|nasib baik|peruntungan|kesempatan emas}} dalam satu {{pengalaman|petualangan|momen|kesempatan}} yang tak terlupakan? {brand_normalized} {{hadir|muncul|tampil|siap melayani}} sebagai {{destinasi utama|tujuan favorit|pilihan terbaik|surga slot}} bagi para {{pencari keberuntungan|pemburu jackpot|penggemar slot|pejuang kemenangan}} yang {{menginginkan|mendambakan|mencari|mengejar}} {{pengalaman|sensasi|keseruan|petualangan}} bermain slot online {{terbaik|teratas|paling unggul|paling menguntungkan}} di tahun 2024.</p>

        <p style="text-align: justify;">{brand_normalized} {{menawarkan|menghadirkan|mempersembahkan|memperkenalkan}} {{koleksi|rangkaian|pilihan|varian}} permainan slot yang {{luar biasa|istimewa|unik|terbaik}}, dirancang khusus untuk memenuhi selera para pemain yang {{menghargai|mencari|mendambakan|menginginkan}} {{kualitas|keunggulan|keistimewaan|pengalaman terbaik}} dan {{kemewahan|kecanggihan|keunikan|inovasi}}. Dengan {{grafis memukau|visual menawan|tampilan mempesona|desain mengagumkan}}, {{efek suara yang memanjakan telinga|audio berkualitas tinggi|suara yang realistis|atmosfer yang imersif}}, dan {{fitur bonus yang menggiurkan|hadiah melimpah|kejutan menarik|peluang kemenangan besar}}, setiap putaran di {brand_normalized} adalah sebuah {{petualangan mewah|pengalaman eksklusif|momen istimewa|kesempatan emas}} yang menjanjikan {{keseruan|kegembiraan|kepuasan|kenikmatan}} tiada tara.</p>

        <p style="text-align: justify;">Kami {{bangga|senang|gembira}} {{mempersembahkan|menghadirkan|menawarkan}} jackpot {{berlimpah|besar|fantastis}} yang menanti untuk {{dimenangkan|diraih|dicapai}}. Dengan {{tingkat kemenangan yang tinggi|peluang menang yang besar|kesempatan sukses yang melimpah}} dan {{peluang jackpot yang menggiurkan|kesempatan meraih hadiah besar|kemungkinan memenangkan hadiah utama}}, {brand_normalized} adalah tempat di mana {{impian|harapan|angan-angan}} Anda tentang {{kekayaan|kemakmuran|kesuksesan finansial}} bisa menjadi {{kenyataan|realita|nyata}}. {{Bergabunglah|Daftarlah|Ikuti}} sekarang dan {{rasakan|alami|nikmati}} sendiri sensasi menjadi bagian dari {{komunitas elit|kelompok eksklusif|lingkaran terpilih}} pemain slot yang {{beruntung|sukses|berjaya}}. {brand_normalized} - di mana setiap putaran adalah {{kesempatan|peluang|momen}} untuk {{meraih|mendapatkan|mewujudkan}} kemewahan!</p>
        """
        
        description2 = spintax.spin(description2_template.format(brand_normalized=brand_normalized))

        ratingValue = random.randint(76, 97)
        ratingCount = random.randint(2153, 291721)
        imageUrl = random.choice(image_urls)
        
        base_color = random.choice(colors)
        base_rgb = Color(hex=base_color).rgb
        lighter_rgb = tuple(min(255, int(c * 1.3)) for c in base_rgb)
        lighter_color = '#{:02x}{:02x}{:02x}'.format(*lighter_rgb)

        context = {
            'brand_slug': brandSlug,
            'brand_name': brandName,
            'canonicalUrl': canonicalUrl,
            'link': link,
            'buttonUrl': buttonUrl,
            'title': title,
            'description': description,
            'description2': description2,
            'ratingValue': ratingValue,
            'ratingCount': ratingCount,
            'image_url': imageUrl,
            'base_color': base_color,
            'lighter_color': lighter_color,
            'header_color': random_color(),
            'products_color': random_color(),
            'footer_color': random_color(),
            'amphtml': amphtml  
        }
        
        if template_choice == '1':
            template_file = random.choice(template_files)
        else:
            template_file = template_files[0]
        
        create_html_page(template_file, output_file, context)
        print(f'HTML untuk {brandName} telah dibuat: {output_file}')
        total_files_created += 1
        domain_files_created += 1

    print(f"Telah diproses {domain_files_created} halaman untuk domain {domain}")
    
    # Increment AMP counter untuk domain berikutnya
    amp_counter += 1

# Buat sitemap untuk setiap domain setelah semua brand diproses
for domain in domains:
    domain_folder = os.path.join(file_root_normal, domain)
    create_sitemap(domain_folder, domain)
    print(f"Sitemap telah dibuat untuk {domain}")

print(f"Total file yang dibuat: {total_files_created}")
print(f"Jumlah brand yang diproses: {len(spintaxed_brands)}")
print(f"Jumlah domain: {len(domains)}")
print("Pembuatan HTML dan sitemap selesai.")

# Verifikasi
for domain in domains:
    domain_folder = os.path.join(file_root_normal, domain)
    file_count = sum([len(files) for r, d, files in os.walk(domain_folder)])
    print(f"Jumlah file di {domain}: {file_count}")
# Tambahkan fitur untuk membuat file verifikasi Google
def create_google_verification_file(domain_folder):
    verification_content = "google-site-verification: googleb1a563b9a3ac6428.html"
    verification_file = os.path.join(domain_folder, "googleb1a563b9a3ac6428.html")
    
    with open(verification_file, 'w') as f:
        f.write(verification_content)
    
    print(f"File verifikasi Google telah dibuat: {verification_file}")

# Buat file verifikasi Google untuk setiap domain
for domain in domains:
    domain_folder = os.path.join(file_root_normal, domain)
    create_google_verification_file(domain_folder)

# Tambahkan fitur untuk membuat file HTML verifikasi Google
def create_google_verification_html(domain_folder):
    verification_content = "google-site-verification: google82c0985e435124d4.html"
    verification_file = os.path.join(domain_folder, "google82c0985e435124d4.html")
    
    with open(verification_file, 'w') as f:
        f.write(f"<html><head><meta name=\"google-site-verification\" content=\"{verification_content}\"></head><body>{verification_content}</body></html>")
    
    print(f"File HTML verifikasi Google telah dibuat: {verification_file}")

# Buat file HTML verifikasi Google untuk setiap domain
for domain in domains:
    domain_folder = os.path.join(file_root_normal, domain)
    create_google_verification_html(domain_folder)


print("Proses Selesai ~")