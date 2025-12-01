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
import sys

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

def handle_exit():
    print('\n\033[93m🛑 Proses dibatalkan oleh pengguna 🛑\033[0m')
    print('\033[94m👋 Terima kasih telah menggunakan VNDAL LP-2.0 Script! 👋\033[0m')
    sys.exit(0)

image_urls = [
    "https://kristalmillan.com/image/1000120270.jpg",
    "https://kristalmillan.com/image/1000120271.jpg",
    "https://kristalmillan.com/image/1000120272.jpg",
    "https://kristalmillan.com/image/1000120273.jpg",
    "https://kristalmillan.com/image/1000120278.jpg",
    "https://kristalmillan.com/image/1000120279.jpg",
    "https://kristalmillan.com/image/1000120280.jpg",
    "https://kristalmillan.com/image/1000120281.jpg",
    "https://kristalmillan.com/image/1000120286.jpg",
    "https://kristalmillan.com/image/1000120287.jpg",
    "https://kristalmillan.com/image/1000120288.jpg",
    "https://kristalmillan.com/image/1000120289.jpg",
    "https://kristalmillan.com/image/1000120294.jpg",
    "https://kristalmillan.com/image/1000120295.jpg",
    "https://kristalmillan.com/image/1000120296.jpg",
    "https://kristalmillan.com/image/1000120297.jpg",
    "https://kristalmillan.com/image/1000120305.jpg",
    "https://kristalmillan.com/image/1000120306.jpg",
    "https://kristalmillan.com/image/1000120307.jpg",
    "https://kristalmillan.com/image/1000120308.jpg",
    "https://kristalmillan.com/image/1000120263.jpg",
    "https://kristalmillan.com/image/1000120253.jpg",
    "https://kristalmillan.com/image/1000120254.jpg",
    "https://kristalmillan.com/image/1000120255.jpg",
    "https://kristalmillan.com/image/1000120260.jpg",
    "https://kristalmillan.com/image/1000120261.jpg",
    "https://kristalmillan.com/image/1000120262.jpg",
    "https://kristalmillan.com/image/1000120235.jpg",
    "https://kristalmillan.com/image/1000120241.jpg",
    "https://kristalmillan.com/image/1000120242.jpg",
    "https://kristalmillan.com/image/1000120243.jpg",
    "https://kristalmillan.com/image/1000120247.jpg",
    "https://kristalmillan.com/image/1000120252.jpg",
    "https://kristalmillan.com/image/1000120225.jpg",
    "https://kristalmillan.com/image/1000120226.jpg",
    "https://kristalmillan.com/image/1000120227.jpg",
    "https://kristalmillan.com/image/1000120232.jpg",
    "https://kristalmillan.com/image/1000120233.jpg",
    "https://kristalmillan.com/image/1000120234.jpg",
    "https://kristalmillan.com/image/1000120224.jpg",
    "https://kristalmillan.com/image/1000119566.jpg",
    "https://kristalmillan.com/image/1000119570.jpg",
    "https://kristalmillan.com/image/1000119571.jpg",
    "https://kristalmillan.com/image/1000119549.jpg",
    "https://kristalmillan.com/image/1000119550.jpg",
    "https://kristalmillan.com/image/1000119553.jpg",
    "https://kristalmillan.com/image/1000119555.jpg",
    "https://kristalmillan.com/image/1000119558.jpg",
    "https://kristalmillan.com/image/1000119561.jpg",
    "https://kristalmillan.com/image/1000119565.jpg",
    "https://kristalmillan.com/image/1000119534.jpg",
    "https://kristalmillan.com/image/1000119541.jpg",
    "https://kristalmillan.com/image/1000119542.jpg",
    "https://kristalmillan.com/image/1000119543.jpg",
    "https://kristalmillan.com/image/1000119545.jpg",
    "https://kristalmillan.com/image/1000119546.jpg",
    "https://kristalmillan.com/image/1000119547.jpg",
    "https://kristalmillan.com/image/1000119529.jpg",
    "https://kristalmillan.com/image/1000119530.jpg",
    "https://kristalmillan.com/image/1000119533.jpg"
]

colors = [
    "#000000", "#0D1117", "#1A1A1A", "#1E1E1E", "#2C2C2C", "#333333", "#3C3C3C", "#2B2B2B", "#1C2833", "#17202A",
    "#1B2631", "#212F3C", "#2C3E50", "#34495E", "#4A0E4E", "#1A5276", "#117A65", "#7D3C98", "#A93226", "#D35400",
    "#27AE60", "#2980B9", "#8E44AD", "#FF1493", "#00CED1", "#FF4500", "#32CD32", "#4169E1", "#9400D3", "#FF6347",
    "#20B2AA", "#FF69B4", "#1E90FF", "#00FA9A", "#FF8C00", "#00BFFF", "#7B68EE"
]

try:
    print('🌟========================================================🌟')
    print('''
    \033[91m██╗   ██╗\033[92m███╗   ██╗\033[93m██████╗ \033[94m █████╗ \033[95m██╗     
    \033[91m██║   ██║\033[92m████╗  ██║\033[93m██╔══██╗\033[94m██╔══██╗\033[95m██║     
    \033[91m██║   ██║\033[92m██╔██╗ ██║\033[93m██║  ██║\033[94m███████║\033[95m██║     
    \033[91m╚██╗ ██╔╝\033[92m██║╚██╗██║\033[93m██║  ██║\033[94m██╔══██║\033[95m██║     
    \033[91m ╚████╔╝ \033[92m██║ ╚████║\033[93m██████╔╝\033[94m██║  ██║\033[95m███████╗
    \033[91m  ╚═══╝  \033[92m╚═╝  ╚═══╝\033[93m╚═════╝ \033[94m╚═╝  ╚═╝\033[95m╚══════╝
    \033[0m''')
    print('\033[1m\033[95m✨ VNDAL LP-2.0 Script Berjalan... ✨\033[0m')
    print('\033[94m🌟========================================================🌟\033[0m')
    
    try:
        inputfoldername = input("\n\033[92m🌈 Silakan masukkan Nama Folder Untuk Menyimpan Hasil Dari Script Ini 🌈\033[0m\n\033[93m✏️ Masukkan nama folder:\033[0m ").lower()
        inputfoldername = inputfoldername.replace(" ", "+")
        print('\033[94m🌟========================================================🌟\033[0m')
    except KeyboardInterrupt:
        handle_exit()

    while True:
        try:
            pages_per_domain = int(input("\033[95m🌟 Berapa banyak halaman menakjubkan yang ingin Anda buat per domain? 🌟\033[0m "))
            if pages_per_domain > 0:
                break
            else:
                print("\033[91m❌ Mohon masukkan angka positif yang fantastis. ❌\033[0m")
        except ValueError:
            print("\033[91m❌ Mohon masukkan angka yang valid dan mengagumkan. ❌\033[0m")
        except KeyboardInterrupt:
            handle_exit()

    print('\033[94m🌟========================================================🌟\033[0m')

    try:
        template_choice = input("\n\033[96m🎨 Pilih opsi template yang paling keren: 🎨\033[0m\n\033[92m1. Acak Dari 4 Template (Penuh Kejutan! 🎉)\033[0m\n\033[93m2. Square Space (Klasik tapi Fantastis! ✨)\033[0m\n\033[94m3. Square Space V2 (Elegan dan Menawan! 💫)\033[0m\n\033[95m4. Square Space V3 (Inovatif dan Memukau! 🌈)\033[0m\n\033[91m5. Template Lazada (Trending ! 🔥)\033[0m\n\033[96m🔢 Masukkan pilihan Anda (1-5):\033[0m ")
        if template_choice == '1':
            template_files = ['temp-1.html', 'temp-2.html', 'temp-3.html', 'temp-4.html']
        else:
            template_index = int(template_choice) - 2
            template_files = [f'temp-{template_index + 1}.html']
    except KeyboardInterrupt:
        handle_exit()

    print('\033[94m🌟========================================================🌟\033[0m')

    file_root_normal = f'Landing-page-{inputfoldername.lower()}/'
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

    print(f"\033[92m🌐 Jumlah domain yang luar biasa: {len(domains)} 🌐\033[0m")
    print(f"\033[93m🏷️ Jumlah brand yang akan digunakan secara menakjubkan: {len(spintaxed_brands)} 🏷️\033[0m")

    for domain in domains:
        domain_folder = os.path.join(file_root_normal, domain)
        create_folder_if_not_exists(domain_folder)

    # Fungsi untuk membuat landing page utama
    def create_main_landing_page(domain_folder, domain, template_file, button_url):
        # Siapkan context untuk landing page utama
        main_title = f"{domain} | Kumpulan Situs Slot Online Terpercaya 2024"
        main_description = f"Temukan koleksi lengkap situs slot online terpercaya di {domain}. Kami menyediakan daftar terlengkap provider slot online dengan RTP tinggi dan jackpot besar."
        
        # Ambil beberapa brand untuk ditampilkan di halaman utama
        featured_brands = spintaxed_brands[:min(12, len(spintaxed_brands))]
        
        # Generate warna acak untuk styling
        header_color = random_color()
        products_color = random_color()
        footer_color = random_color()
        base_color = random.choice(colors)
        base_rgb = Color(hex=base_color).rgb
        lighter_rgb = tuple(min(255, int(c * 1.3)) for c in base_rgb)
        lighter_color = '#{:02x}{:02x}{:02x}'.format(*lighter_rgb)
        
        # Generate gradient colors
        gradient_color1 = random.choice(colors)
        gradient_color2 = random.choice(colors)
        gradient = f"linear-gradient(89.87deg, {gradient_color1} 35.41%, {gradient_color2} 121.72%)"
        
        # Generate additional gradient colors
        gradient_color3 = random.choice(colors)
        gradient_color4 = random.choice(colors)
        gradient2 = f"linear-gradient(89.87deg, {gradient_color3} 35.41%, {gradient_color4} 121.72%)"
        
        # Ambil gambar acak
        imageUrl = random.choice(image_urls)
        
        # Generate rating acak
        ratingValue = random.randint(90, 97)
        ratingCount = random.randint(10000, 100000)
        
        # Buat context untuk template
        context = {
            'brand_slug': 'home',
            'brand_name': domain,
            'canonicalUrl': f'https://{domain}/',
            'link': f'https://{domain}/',
            'buttonUrl': button_url,
            'title': main_title,
            'description': main_description,
            'description2': f"""
            <p style="text-align: justify;">{domain} merupakan portal informasi terlengkap tentang situs slot online terpercaya di Indonesia. Kami menyediakan daftar situs slot dengan reputasi terbaik, layanan 24 jam, dan sistem pembayaran yang aman.</p>
            
            <p style="text-align: justify;">Setiap situs yang kami rekomendasikan telah melalui proses seleksi ketat untuk memastikan keamanan dan kepuasan member. Anda bisa bermain dengan tenang dan fokus menikmati sensasi permainan slot online terbaik.</p>
            
            <p style="text-align: justify;">Nikmati berbagai keuntungan seperti bonus new member, bonus deposit, cashback mingguan, dan rollingan dari setiap situs yang kami rekomendasikan.</p>
            """,
            'ratingValue': ratingValue,
            'ratingCount': ratingCount,
            'image_url': imageUrl,
            'base_color': base_color,
            'lighter_color': lighter_color,
            'header_color': header_color,
            'products_color': products_color,
            'footer_color': footer_color,
            'gradient': gradient,
            'gradient2': gradient2,
            'amphtml': '' # Tidak perlu AMP untuk halaman utama
        }
        
        # Buat file index.html menggunakan template yang dipilih
        index_file = os.path.join(domain_folder, "index.html")
        create_html_page(template_file, index_file, context)
        
        print(f"Landing page utama dibuat untuk domain {domain} menggunakan template {template_file}")
        
        # Buat folder setiap featured brand jika belum ada
        for brand in featured_brands:
            try:
                brandName = spintax.spin(brand)
                brandSlug = brandName.replace(" ", "+").lower()
                brand_folder = os.path.join(domain_folder, brandSlug.lower())
                create_folder_if_not_exists(brand_folder)
            except Exception as e:
                print(f"\033[91m❌ Error saat memproses brand untuk halaman utama: {str(e)} ❌\033[0m")
                continue

    try:
        amp_domain = input("\033[95m🔌 Masukkan domain AMP yang keren (contoh: amphost.id): 🔌\033[0m ")
        amp_page_name = input("\033[96m📄 Masukkan nama halaman yang unik untuk file HTML AMP (contoh: mrmouse): 📄\033[0m ")
        print('\033[94m🌟========================================================🌟\033[0m')
    except KeyboardInterrupt:
        handle_exit()

    try:
        buttonUrl = input("\033[91m🔗 Masukkan URL yang menarik untuk tombol (contoh: https://domain.com/foldermu): 🔗\033[0m ")
        print('\033[94m🌟========================================================🌟\033[0m')
    except KeyboardInterrupt:
        handle_exit()

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

    # Buat landing page utama untuk setiap domain
    for domain in domains:
        domain_folder = os.path.join(file_root_normal, domain)
        # Buat landing page utama berdasarkan template yang dipilih
        if template_choice == '1':
            template_file = random.choice(template_files)
        else:
            template_file = template_files[0]
        create_main_landing_page(domain_folder, domain, template_file, buttonUrl)
        total_files_created += 1

    for domain in domains:
        domain_folder = os.path.join(file_root_normal, domain)
        domain_files_created = 0
        
        for spintaxed_brand in spintaxed_brands:
            if domain_files_created >= pages_per_domain:
                break
            
            try:
                brandName = spintax.spin(spintaxed_brand)
                brandSlug = brandName.replace(" ", "-").lower()
                brand_normalized = brandName.replace(" ", "-").lower()
                folder_path = os.path.join(domain_folder, brandSlug.lower())
                create_folder_if_not_exists(folder_path)
                
                output_file = os.path.join(folder_path, "index.html")
                
                if os.path.exists(output_file):
                    print(f"🌟 File sudah ada: {output_file} 🌟")
                    continue

                canonicalUrl = f'https://{domain}/{brandSlug.lower()}/'
                link = f'https://{domain}/{brandSlug.lower()}/'
                canonicalUrl = f'https://{domain}/{brandSlug}/'
                link = f'https://{domain}/{brandSlug}/'
                amphtml = f'https://{amp_domain}/{amp_page_name}-{amp_counter}/'
                
                title_options = [
                    "{brand_normalized}: {{Slot Online|Game Slot|Mesin Slot}} {{Gacor|Maxwin|Terpercaya}} {{2024|Hari Ini}}",
                    "{brand_normalized} - {{Situs|Agen|Bandar}} Slot {{Terpercaya|Terbaik|Resmi}} {{Indonesia|Nusantara}}",
                    "{{Daftar|Main|Akses}} {brand_normalized} {{Slot Gacor|Slot Online|Game Slot}} {{Anti Rungkad|RTP Tinggi}}",
                    "{brand_normalized} {{Link Alternatif|Link Resmi|Link Terbaru}} {{Slot Online|Game Slot}} {{2024|Terkini}}",
                    "{{Slot Gacor|Slot Online|Game Slot}} {brand_normalized} {{Deposit Pulsa|E-Wallet|Bank}} {{24 Jam|Nonstop}}",
                    "{brand_normalized} - {{Situs Judi|Agen Judi|Bandar}} Slot {{Terpercaya|Terbaik|Resmi}} {{2024|Hari Ini}}",
                    "{{Mainkan|Rasakan|Nikmati}} Slot {brand_normalized} {{Winrate|RTP|Persentase}} {{Tertinggi|Maximal}}",
                    "{brand_normalized} {{Provider|Situs|Platform}} Slot {{Terlengkap|Terbaik|Terpopuler}} {{2024|Saat Ini}}",
                    "{{Daftar|Join|Gabung}} {brand_normalized} {{Bonus|Promo|Hadiah}} {{New Member|Welcome|Terbaru}}",
                    "{brand_normalized} {{Slot Online|Game Slot|Mesin Slot}} {{Mudah|Gampang}} {{Menang|Jackpot|Maxwin}}",
                    "{{Situs|Link|Web}} {brand_normalized} {{Slot Gacor|Slot Online}} {{Terpercaya|Terbaik}} {{2024|Hari Ini}}",
                    "{brand_normalized} {{Slot|Game|Permainan}} {{Terbaik|Terpopuler|Favorit}} {{Indonesia|Asia}}",
                    "{{Login|Daftar|Masuk}} {brand_normalized} {{Slot Online|Game Slot}} {{Terpercaya|Resmi|Terbaik}}",
                    "{brand_normalized} {{Situs|Agen|Provider}} {{Slot Gacor|Slot Online}} {{24 Jam|Non-Stop}}",
                    "{{Main|Akses|Coba}} {brand_normalized} {{Slot Online|Game Slot}} {{Deposit|Via}} {{Pulsa|E-Wallet}}",
                    "{brand_normalized} {{Slot Online|Game Slot}} {{Jackpot|Bonus}} {{Terbesar|Melimpah}}",
                    "{{Daftar|Join}} {brand_normalized} {{Slot Online|Game Slot}} {{Modal|Deposit}} {{Kecil|Murah}}",
                    "{brand_normalized} {{Situs|Platform}} {{Judi Online|Slot Online}} {{Terlengkap|Terbaik}}",
                    "{{Mainkan|Nikmati}} {brand_normalized} {{Slot Online|Game Slot}} {{Sensasi|Pengalaman}} {{Berbeda|Terbaik}}",
                    "{{Link|Situs}} {brand_normalized} {{Slot Online|Game Slot}} {{Anti|Bebas}} {{Rungkad|Kalah}}"
                ]
                title_template = random.choice(title_options).format(brand_normalized=brand_normalized)
                title = spintax.spin(title_template)
                
                description_options = [
                    "{brand_normalized} adalah situs slot online terkemuka di Indonesia yang menawarkan {{ratusan|berbagai|puluhan}} game slot {{terbaik|berkualitas|terpopuler}} dari provider terkenal. Dapatkan pengalaman bermain slot dengan {{RTP tinggi|winrate besar|peluang menang maksimal}} dan layanan pelanggan 24 jam nonstop.",
                    
                    "Bergabunglah dengan {brand_normalized}, situs judi slot {{terpercaya|resmi|terbaik}} yang memiliki lisensi resmi. Kami menyediakan {{bonus welcome|promo menarik|cashback mingguan}} untuk member baru dan kemudahan {{deposit via pulsa|transaksi via e-wallet|withdraw cepat}} tanpa potongan.",
                    
                    "{brand_normalized} adalah pilihan utama bagi pecinta slot online di Indonesia dengan koleksi {{game terlengkap|permainan terbaik|slot gacor}} dan sistem keamanan yang terjamin. Daftar sekarang untuk {{akses mudah|bermain kapanpun|menikmati sensasi}} slot online dari provider internasional."
                ]
                description_template = random.choice(description_options).format(brand_normalized=brand_normalized)
                description = spintax.spin(description_template)
                
                description2_template = """
                <p style="text-align: justify;">{brand_normalized} merupakan situs slot online terpercaya di Indonesia yang telah beroperasi sejak {{2018|2019|2020}}. Kami menyediakan {{berbagai|ratusan|puluhan}} permainan slot dari provider ternama seperti {{Pragmatic Play, Habanero, PG Soft|Microgaming, NetEnt, Playtech|Joker Gaming, CQ9, Spadegaming}} dengan tingkat kemenangan tinggi dan jackpot progressive.</p>

                <p style="text-align: justify;">Sebagai platform slot online terbaik, {brand_normalized} mengutamakan keamanan dan kenyamanan member dengan sistem enkripsi data terkini dan layanan customer service 24 jam. Metode transaksi kami mendukung {{semua bank lokal|e-wallet populer|deposit via pulsa}} untuk kemudahan bermain kapan saja dan di mana saja.</p>

                <p style="text-align: justify;">Bergabung dengan {brand_normalized} sangat mudah dan cepat. Anda hanya perlu melakukan pendaftaran, mengisi data dengan benar, dan melakukan deposit minimal {{10 ribu|25 ribu|50 ribu}} rupiah untuk mulai bermain. Nikmati juga berbagai bonus dan promosi menarik seperti {{bonus new member|cashback mingguan|rollingan}} yang bisa meningkatkan peluang kemenangan Anda.</p>
                """
                
                description2 = spintax.spin(description2_template.format(brand_normalized=brand_normalized))

                ratingValue = random.randint(76, 97)
                ratingCount = random.randint(2153, 291721)
                imageUrl = random.choice(image_urls)
                
                base_color = random.choice(colors)
                base_rgb = Color(hex=base_color).rgb
                lighter_rgb = tuple(min(255, int(c * 1.3)) for c in base_rgb)
                lighter_color = '#{:02x}{:02x}{:02x}'.format(*lighter_rgb)

                # Generate gradient colors
                gradient_color1 = random.choice(colors)
                gradient_color2 = random.choice(colors)
                gradient = f"linear-gradient(89.87deg, {gradient_color1} 35.41%, {gradient_color2} 121.72%)"

                # Generate additional gradient colors
                gradient_color3 = random.choice(colors)
                gradient_color4 = random.choice(colors)
                gradient2 = f"linear-gradient(89.87deg, {gradient_color3} 35.41%, {gradient_color4} 121.72%)"

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
                    'gradient': gradient,
                    'gradient2': gradient2,
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
            
            except KeyboardInterrupt:
                handle_exit()
            except Exception as e:
                print(f"\033[91m❌ Error saat memproses brand {spintaxed_brand}: {str(e)} ❌\033[0m")
                continue

        print(f"Telah diproses {domain_files_created} halaman untuk domain {domain}")
        
        # Increment AMP counter untuk domain berikutnya
        amp_counter += 1

    # Buat sitemap untuk setiap domain setelah semua brand diproses
    for domain in domains:
        try:
            domain_folder = os.path.join(file_root_normal, domain)
            create_sitemap(domain_folder, domain)
            print(f"Sitemap telah dibuat untuk {domain}")
        except Exception as e:
            print(f"\033[91m❌ Error saat membuat sitemap untuk {domain}: {str(e)} ❌\033[0m")

    print(f"Total file yang dibuat: {total_files_created}")
    print(f"Jumlah brand yang diproses: {len(spintaxed_brands)}")
    print(f"Jumlah domain: {len(domains)}")
    print("Pembuatan HTML dan sitemap selesai.")

    # Verifikasi
    for domain in domains:
        domain_folder = os.path.join(file_root_normal, domain)
        file_count = sum([len(files) for r, d, files in os.walk(domain_folder)])
        print(f"Jumlah file di {domain}: {file_count}")

    # Fitur tambahan
    try:
        # Tambahkan fitur untuk membuat file verifikasi Google
        def create_google_verification_file(domain_folder):
            verification_content = "google-site-verification: google1b7c57225f16434b.html"
            verification_file = os.path.join(domain_folder, "google1b7c57225f16434b.html")
            
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

        # Tambahkan fitur untuk membuat file txt berisi slug tanpa tanda +
        def create_slug_file(domain_folder, brand):
            slug = brand.replace("+", " ")
            slug_file = os.path.join(domain_folder, "slug.txt")
            
            with open(slug_file, 'a') as f:
                f.write(slug + "\n")
            
            print(f"File slug telah dibuat: {slug_file}")

        # Buat file slug untuk setiap brand di setiap domain
        for domain in domains:
            domain_folder = os.path.join(file_root_normal, domain)
            for brand in spintaxed_brands:
                create_slug_file(domain_folder, brand)

        print("Proses Selesai ~")

    except KeyboardInterrupt:
        handle_exit()
    except Exception as e:
        print(f"\033[91m❌ Error saat membuat file tambahan: {str(e)} ❌\033[0m")
        print("Script selesai dengan beberapa error.")

except KeyboardInterrupt:
    handle_exit()
except Exception as e:
    print(f"\n\033[91m❌ Error tidak terduga: {str(e)} ❌\033[0m")
    print("Script terhenti karena error.")
    sys.exit(1)