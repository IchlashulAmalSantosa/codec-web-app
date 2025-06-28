# 🎬 Sistem Codec & Steganografi Multimedia

Proyek UAS Mata Kuliah **Sistem Multimedia**  
Dibuat menggunakan **Flask**, aplikasi ini memungkinkan pengguna untuk melakukan:

- ✅ Kompresi Audio
- ✅ Kompresi Video
- ✅ Steganografi Gambar (LSB) – Encode & Decode
- ✅ Tampilan berbasis Web Interaktif + Animasi Footer

---

## 📌 Fitur Utama

### 📷 Steganografi Gambar (LSB)

- Menyisipkan pesan ke dalam gambar (encode)
- Mengekstrak pesan rahasia dari gambar stego (decode)
- Mendukung download gambar hasil encode

### 🎧 Kompresi Audio

- Upload file audio dan kompres dengan bitrate yang lebih rendah
- Dukung berbagai format (mp3, wav)

### 🎥 Kompresi Video

- Upload video dan atur bitrate untuk memperkecil ukuran file
- Mendukung preview dan download hasil

---

## 🖼️ Tampilan Antarmuka

> Aplikasi ini berbasis web menggunakan HTML, CSS, JavaScript dengan backend Flask.

- Form upload untuk masing-masing fitur
- Preview hasil kompresi/stego (image, audio, video)
- Tombol download hasil
- Footer animasi berjalan

---

## 🚀 Cara Menjalankan Lokal

### 1. Clone Repository

```bash
git clone https://github.com/username/codec-web-app.git
cd codec-web
```

### 2. Buat & Aktifkan Virtual Environment

```python -m venv venv```

# Windows

```venv\Scripts\activate```

# Linux/macOS

```source venv/bin/activate```

### 3. Install Dependensi

```pip install -r requirements.txt```

### 4. Jalankan Aplikasi

```python app.py```

Lalu buka browser ke: ```http://127.0.0.1:5000```

### 📁 Struktur Proyek

![image](https://github.com/user-attachments/assets/9a6b3f4d-27cc-49e2-9763-ea5dc0690ab1)


### 👨‍💻 Dibuat Oleh

Nama: **Ichlashul 'Amal Santosa (1227050054) & Ilham Marwan Sidik (1227050055)**

### 📃 Lisensi

Proyek ini dibuat untuk keperluan edukasi dan tugas akhir. Tidak untuk distribusi komersial.
