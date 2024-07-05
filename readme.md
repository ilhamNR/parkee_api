# Aplikasi Manipulasi Data Universitas

Aplikasi ini adalah contoh implementasi untuk mengambil data universitas dari sebuah API, melakukan manipulasi data menggunakan Pandas, dan menyimpan hasilnya ke dalam sebuah file CSV.

## Instalasi

1. Pastikan Python 3 sudah terinstal di komputer Anda.
2. Clone repositori ini ke dalam komputer Anda:
   ```bash
   git clone <link_repositori_anda>
   cd <nama_folder_repositori>
3. Install semua dependencies yang dibutuhkan dengan menjalankan perintah:
   ```bash
   pip install -r requirements.txt

## Penggunaan
1. Buka terminal atau command prompt.
2. Jalankan aplikasi dengan mengetikkan perintah:
   ```bash
   python app.py
3. Aplikasi akan melakukan hal berikut:
    * Mengambil data universitas dari API yang disediakan.
    * Membuat DataFrame menggunakan Pandas dan mengisi dengan data universitas.
    * Memfilter data berdasarkan kolom 'state-province'.
    * Menampilkan hasil filter ke layar.
    * Menyimpan data yang sudah difilter ke dalam file CSV universities_united_states_filtered.csv.
4. Anda dapat membuka file CSV tersebut untuk melihat hasil filter data universitas.
