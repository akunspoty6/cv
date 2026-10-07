# 📘 User Manual: Web CV & CMS (Smart Portfolio)

Halo Bang Rafi! Ini adalah panduan lengkap buat lu (atau temen lu) untuk ngejalanin, ngedit konten, sampe nge-push website CV & Portfolio canggih ini ke GitHub.

Website ini dibikin spesial pake **Python (Flask)**, **SQLite** (database ringan & cepet), dan **Tailwind CSS** (buat tampilan ala hacker / startup yang *sleek* & modern).

---

## 🚀 1. Cara Menjalankan Website di VPS
Kalo webnya belum nyala, lu bisa nyalain pake perintah ini di terminal:

```bash
# Pindah ke folder project
cd /root/web-cv-cms

# Aktifin environment Python
source venv/bin/activate

# Jalankan servernya di background (port 8080)
nohup python3 app.py > flask.log 2>&1 &
```

Kalau udah jalan, lu bisa akses webnya dari browser di:
👉 **http://103.147.33.12:8080**

---

## 🔐 2. Cara Masuk ke CMS Admin (Buat Edit Data)
Kalo lu mau ngedit nama, nambahin skill, nambah pengalaman kerja, atau nambahin link repo GitHub baru, lu **kaga usah ngedit kodingan**. Tinggal masuk ke Admin Panel aja!

1. Buka browser: **http://103.147.33.12:8080/login**
2. Masukin kredensial bawaan:
   * **Username:** `admin`
   * **Password:** `admin123`
3. Begitu masuk, lu bakal ngeliat Dashboard CMS.

---

## 📝 3. Cara Ngedit Konten dari Dashboard CMS
Di dalem dashboard sebelah kiri, ada menu tab. Lu tinggal klik mau ngedit apa:

1. **Profil Utama:** 
   Buat ganti Nama Lu, Bio, Jabatan, Nomor WA, Link LinkedIn, sampe URL Foto Profil (Cari foto di internet, copy *Image Address*-nya, paste ke situ).
   *Jangan lupa klik "Simpan Perubahan"!*
2. **Keahlian (Skills):** 
   Klik tombol **"+ Tambah Skill"**, masukin kategori (contoh: *AI & Machine Learning*), nama skill (contoh: *YOLOv8*), dan tingkat persentase kemahiran (10 - 100).
3. **Portfolio Proyek:**
   Klik **"+ Tambah Proyek"**. Di sini lu bisa masukin:
   - Judul proyek lu (contoh: *SmartAgro Deteksi Penyakit*)
   - Deskripsi singkat
   - Tags (contoh: *Python, YOLOv8, Flask*)
   - Link Demo atau Link Repository GitHub lu
   - URL Gambar Thumbnail proyek (Biar keren pas di-showcase).
4. **Riwayat Pengalaman & Pendidikan:**
   Tinggal klik Tambah, masukin periode tahun, dan klik Simpan. Gampang banget!

*Note:* Setiap kali lu klik Simpan, datanya langsung **OTOMATIS** berubah di halaman depan website! Lu bisa klik tombol **"Lihat Website CV"** di pojok kanan atas buat ngecek hasilnya.

---

## 🌐 4. Cara Upload (Push) Kodingan ke GitHub
Kalo lu ngerasa website ini udah danta dan mau lu pamerin atau lu simpen di repository GitHub lu secara permanen, jalankan perintah ini di VPS:

```bash
cd /root/web-cv-cms

# Inisialisasi Git
git init

# Tambahkan file yang mau diupload (kecuali folder venv)
echo "venv/" > .gitignore
echo "__pycache__/" >> .gitignore
echo "flask.log" >> .gitignore

git add .
git commit -m "Initial commit: Web CV & CMS by Hermes"

# Bikin repository baru di GitHub (pake gh CLI)
gh repo create web-cv-cms --public --source=. --remote=origin --push
```
*Note: Pas `gh repo create` dijalanin, otomatis repository bakal kebuat di akun GitHub `akunspoty6` lu!*

---

🎉 **Selesai!** 
Website CV lu udah online, ada CMS-nya, tampilannya kece badai, dan gampang banget di-manage! Kalo ada error atau mau nambah fitur, tinggal panggil *Wowo* aja! 🫡
