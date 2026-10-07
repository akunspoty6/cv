import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), 'cv.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # Table: Admin
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    ''')

    # Table: Profile
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        title TEXT NOT NULL,
        tagline TEXT,
        bio TEXT,
        email TEXT,
        phone TEXT,
        location TEXT,
        github TEXT,
        linkedin TEXT,
        avatar_url TEXT
    )
    ''')

    # Table: Skills
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        name TEXT NOT NULL,
        level INTEGER DEFAULT 80
    )
    ''')

    # Table: Experience
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS experiences (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL,
        company TEXT NOT NULL,
        period TEXT NOT NULL,
        description TEXT,
        order_num INTEGER DEFAULT 0
    )
    ''')

    # Table: Education
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS education (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        institution TEXT NOT NULL,
        degree TEXT NOT NULL,
        period TEXT NOT NULL,
        description TEXT,
        order_num INTEGER DEFAULT 0
    )
    ''')

    # Table: Projects
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        category TEXT,
        tags TEXT,
        link_demo TEXT,
        link_github TEXT,
        image_url TEXT,
        featured INTEGER DEFAULT 1,
        order_num INTEGER DEFAULT 0
    )
    ''')

    # Seed Admin if not exists
    cursor.execute("SELECT id FROM admin WHERE username = 'admin'")
    if not cursor.fetchone():
        default_pwd = generate_password_hash('admin123')
        cursor.execute("INSERT INTO admin (username, password_hash) VALUES ('admin', ?)", (default_pwd,))

    # Seed Profile if empty
    cursor.execute("SELECT id FROM profile LIMIT 1")
    if not cursor.fetchone():
        cursor.execute('''
        INSERT INTO profile (full_name, title, tagline, bio, email, phone, location, github, linkedin, avatar_url)
        VALUES (
            'Muhammad Raafi Al Hafiidh',
            'Project Manager & AI Engineer',
            'Membangun Solusi Cerdas Berbasis AI, IoT, dan Web Development',
            'Mahasiswa S-1 Teknik Informatika Telkom University Purwokerto dengan fokus riset pada Computer Vision (Deep Learning) dan Internet of Things (IoT). Berpengalaman sebagai Project Manager yang memimpin koordinasi tim pengembang dari tahap riset, perancangan arsitektur, hingga implementasi produk fungsional.',
            'raafialhafiidh@gmail.com',
            '+62 838-9534-7678',
            'Bekasi / Purwokerto, Indonesia',
            'https://github.com/akunspoty6',
            'https://linkedin.com',
            'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&q=80'
        )
        ''')

    # Seed Skills if empty
    cursor.execute("SELECT COUNT(*) as count FROM skills")
    if cursor.fetchone()['count'] == 0:
        initial_skills = [
            ('AI & Machine Learning', 'YOLOv8 & Computer Vision', 90),
            ('AI & Machine Learning', 'PyTorch / Python', 85),
            ('AI & Machine Learning', 'Roboflow Dataset Prep', 88),
            ('IoT & Embedded', 'ESP32 & Arduino', 85),
            ('IoT & Embedded', 'Sensor Integration & MQTT', 80),
            ('Web & Backend', 'Python (Flask / FastAPI)', 88),
            ('Web & Backend', 'Node.js & JavaScript', 82),
            ('Web & Backend', 'RESTful API & SQLite/Postgres', 85),
            ('Management & Tools', 'Agile / Scrum Project Management', 92),
            ('Management & Tools', 'Git & GitHub Collaboration', 88),
            ('Management & Tools', 'Linux VPS & Server Administration', 85)
        ]
        cursor.executemany("INSERT INTO skills (category, name, level) VALUES (?, ?, ?)", initial_skills)

    # Seed Experiences if empty
    cursor.execute("SELECT COUNT(*) as count FROM experiences")
    if cursor.fetchone()['count'] == 0:
        initial_exp = [
            ('Project Manager & AI Engineer', 'SmartAgro - Computing Project Tel-U', '2026 - Sekarang', 'Memimpin tim pengembang beranggotakan 3 orang dalam membangun sistem pertanian cerdas terpadu. Bertanggung jawab atas manajemen sprint, arsitektur backend, dan pelatihan model YOLOv8 untuk deteksi dini penyakit daun padi dan jagung.', 1),
            ('Software Developer & System Integrator', 'Tugas Besar Struktur Data', '2025', 'Merancang dan mengimplementasikan algoritma Graph dan Dijkstra untuk simulasi penentuan rute jaringan terpendek, menghasilkan laporan teknis komprehensif dan implementasi kode modular.', 2),
            ('Student Researcher', 'Telkom University Purwokerto', '2023 - Sekarang', 'Aktif melakukan eksplorasi di bidang AI-Enabled IoT, pengolahan citra digital, manajemen database, dan deployment arsitektur komputasi awan.', 3)
        ]
        cursor.executemany("INSERT INTO experiences (role, company, period, description, order_num) VALUES (?, ?, ?, ?, ?)", initial_exp)

    # Seed Education if empty
    cursor.execute("SELECT COUNT(*) as count FROM education")
    if cursor.fetchone()['count'] == 0:
        initial_edu = [
            ('Telkom University Purwokerto', 'S-1 Teknik Informatika', '2023 - Sekarang', 'Fokus pada Software Engineering, AI & Machine Learning, Internet of Things, dan Manajemen Proyek Teknologi Informasi.', 1),
            ('SMK Telekomunikasi Telesandi Bekasi', 'Teknik Komputer dan Jaringan', '2020 - 2023', 'Mempelajari dasar-dasar jaringan komputer, konfigurasi server Linux, routing, switching, dan logika pemrograman dasar.', 2)
        ]
        cursor.executemany("INSERT INTO education (institution, degree, period, description, order_num) VALUES (?, ?, ?, ?, ?)", initial_edu)

    # Seed Projects if empty
    cursor.execute("SELECT COUNT(*) as count FROM projects")
    if cursor.fetchone()['count'] == 0:
        initial_proj = [
            (
                'SmartAgro: AI & IoT Plant Disease Detection',
                'Sistem cerdas deteksi penyakit tanaman padi dan jagung berbasis Computer Vision YOLOv8 yang terintegrasi dengan sensor kelembapan tanah dan monitoring iklim mikro sawah berbasis ESP32.',
                'AI & IoT',
                'Python, YOLOv8, ESP32, Flask, TailwindCSS',
                '#',
                'https://github.com/akunspoty6',
                'https://images.unsplash.com/photo-1586771107445-d3ca888129ff?auto=format&fit=crop&w=800&q=80',
                1,
                1
            ),
            (
                'IoT Microclimate & Irrigation Monitoring',
                'Purwarupa node sensor hemat daya untuk memantau intensitas sinar matahari dan kadar air tanah secara real-time untuk mencegah over-watering pada tanaman.',
                'IoT',
                'C++, ESP32, MQTT, Dashboard Web',
                '#',
                'https://github.com/akunspoty6',
                'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80',
                1,
                2
            ),
            (
                'Graph Routing Simulation System',
                'Implementasi algoritma Graph dan pencarian rute terpendek untuk analisis efisiensi jaringan data berskala besar.',
                'Algorithms',
                'Python, Network Analysis, Data Structures',
                '#',
                'https://github.com/akunspoty6',
                'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=800&q=80',
                0,
                3
            )
        ]
        cursor.executemany("INSERT INTO projects (title, description, category, tags, link_demo, link_github, image_url, featured, order_num) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", initial_proj)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == '__main__':
    init_db()
