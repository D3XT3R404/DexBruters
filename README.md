# DexBruters
# ZIP Password BruteForcer

Sebuah tool sederhana berbasis Python untuk melakukan brute force terhadap file ZIP yang dilindungi password, termasuk yang menggunakan enkripsi AES.

## ✨ Fitur Utama

* ✅ Mendukung ZIP dengan enkripsi AES (via `pyzipper`)
* 📜 Output verbose: setiap password yang dicoba akan ditampilkan
* 📊 Menampilkan jumlah total password dan hasil akhir yang jelas
* ⚙️ Sangat mudah dijalankan tanpa konfigurasi ribet

---

🚀 Cara Pemasangan dan Penggunaan

git clone https://github.com/D3XT3R404/DexBruters

cd DexBruters

1. Install dependencies


pip install -r requirements.txt

jika eror

pip install -r requirements.txt --break-system-packages


2. Jalankan tool-nya


python DexBrute.py


3. Masukkan:

* Path file ZIP yang ingin dibuka
* Path file wordlist (.txt) berisi daftar kemungkinan password

Contoh:


ZIP File Path: /home/nama/secure.zip
Wordlist Path : /home/nama/wordlists/passwords.txt

atau jika kamu berada di satu folder yang sama juga bisa

ZIP File Path: namafile.zip
Wordlist Path : wordlist.txt

---


⚠️ Disclaimer

Tool ini dibuat hanya untuk:

* Edukasi
* Pengujian keamanan sistem milik sendiri

⚠️Jangan gunakan tanpa izin pada file atau sistem yang bukan milikmu. Penyalahgunaan tool ini sepenuhnya menjadi tanggung jawab pengguna.

---

👨‍💻 Author

By David
