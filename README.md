# 🔐 ZIP, RAR, 7z Password BruteForcer

![image](https://github.com/user-attachments/assets/7aa2eeb7-3cab-454a-ae80-6d771afa09e7)


Sebuah tool sederhana dan simpel berbasis Python untuk melakukan brute force terhadap 3 jenis file arsip yang dilindungi password(Terkunci), termasuk ZIP (AES), RAR, dan 7z.

## ✨ Fitur Utama

* ✅ Mendukung ZIP dengan enkripsi AES (via `pyzipper`)
* ✅ Mendukung RAR dan 7z (via `rarfile` dan `py7zr`)
* 📜 Output verbose: setiap password yang dicoba akan ditampilkan
* 📊 Menampilkan jumlah total password dan hasil akhir yang jelas
* ⚙️ Sangat mudah dijalankan tanpa konfigurasi ribet dan simpel


---


# 🚀 Cara Pemasangan dan Penggunaan

git clone https://github.com/D3XT3R404/DexBruters

cd DexBruters


1. Install dependencies


pip install -r requirements.txt


Jika terjadi error:

pip install -r requirements.txt --break-system-packages


Atau install manual:


pip install pyzipper rarfile py7zr colorama --break-system-packages


2. Jalankan tool-nya


python DexBrut.py


3. Masukkan:

* Path filenya (.zip/.rar/.7z) yang ingin dibuka/di brute force
* Path file wordlist (.txt) berisi daftar kata kata yang akan di coba untuk brute force


Contoh:


Masukkan path filenya (zip/rar/7z): /home/nama/namafile.7z
Masukkan path wordlist: /home/nama/wordlists/wordlist.txt


Atau jika berada di folder yang sama:


Masukkan path filenya (zip/rar/7z): secure.zip
Masukkan path wordlist: wordlist.txt


---


## ⚠️ Disclaimer

Tool ini dibuat hanya untuk:

* Edukasi
* Pengujian keamanan milik sendiri

## ⚠️ Jangan gunakan tanpa izin pada file atau sistem yang bukan milikmu. Penyalahgunaan tool ini sepenuhnya menjadi tanggung jawab pengguna.

---

## 👨‍💻 Author

By Muhammad David
