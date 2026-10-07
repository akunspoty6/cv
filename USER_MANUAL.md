# 📘 User Manual: Web CV & CMS (Dark Mode Linear Design)

Halo Bang Rafi! Ini adalah panduan lengkap untuk ngejalanin, ngedit konten, dan ngerawat website CV & Portfolio lu.

Website ini dibikin spesial pake **Python (Flask)**, **SQLite** (database ringan & cepet), dan UI **Dark Mode Native ala Linear** (bukan AI Slop).

---

## 🚀 1. Cara Menjalankan Website (Lokal/VPS)
Kalo lu mau jalanin ulang webnya di komputer lu sendiri atau di VPS lain:

```bash
# Buka terminal dan clone repo ini
git clone https://github.com/akunspoty6/cv.git
cd cv

# Bikin environment Python dan aktifkan
python3 -m venv venv
source venv/bin/activate

# Install library yang dibutuhin
pip install -r requirements.txt

# Jalankan servernya
python3 app.py
```
Web bakal jalan di port 8080 (buka `http://127.0.0.1:8080` di browser).

---

## 🔐 2. Cara Masuk ke CMS Admin (Buat Edit Data)
Kalo lu mau ngedit nama, nambahin skill, proyek, atau pengalaman kerja, **kaga usah ngedit kodingan sama sekali**.

1. Buka browser: `http://localhost:8080/login`
2. Masukin kredensial:
   * **Username:** `admin`
   * **Password:** `admin123`
3. Masuk ke Dashboard CMS!

---

## 📝 3. Cara Ngedit Konten dari Dashboard
Di panel kiri, klik tab menu yang mau diubah:
1. **Profil Utama:** Ganti Nama, Bio, Nomor WA, Link LinkedIn, sampe URL Foto Profil (Cari foto di internet, copy *Image Address*, paste). Jangan lupa klik "Simpan"!
2. **Keahlian (Skills):** Klik "+ Tambah Skill", masukin kategori (contoh: *Machine Learning*), nama skill, dan persentase.
3. **Portfolio Proyek:** Klik "+ Tambah Proyek". Masukin judul, tag (koma-pisahkan), link repo GitHub, link demo, dan link gambar thumbnail proyek lu.
4. **Riwayat Pengalaman & Pendidikan:** Tinggal klik tambah, masukin info tahun dan deskripsi.

*Semua data kesimpen di file `cv.db`. File database ini ikut ke-push ke GitHub lu.*

---

## ☁️ 4. Deploy (Rekomendasi Hosting Gratis)
Karena kodingan ini udah rapi pake Python Flask, lu bisa hosting **GRATIS** selamanya pake **Render.com** atau **PythonAnywhere**.
Caranya di Render:
1. Buka [render.com](https://render.com) dan login pake akun GitHub `akunspoty6`.
2. Bikin *New Web Service*, pilih repo `cv`.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app --bind 0.0.0.0:$PORT` (jangan lupa tambahin `gunicorn` di `requirements.txt`).
5. Selesai! Web CV lu online 24 jam gratis.

---

🎉 **Selesai!** 
Website lu udah nangkring rapi di GitHub `https://github.com/akunspoty6/cv`. Gampang banget di-manage! Kalo ada error, tinggal calling Wowo! 🫡