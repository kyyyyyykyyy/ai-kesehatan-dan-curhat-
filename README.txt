============================================================
   APLIKASI ASISTEN KESEHATAN & PSIKOLOGI VIRTUAL (AI)
============================================================

Deskripsi:
Aplikasi ini adalah Chatbot Cerdas berbasis Python yang menggunakan 
Big Data (CSV) untuk menangani konsultasi kesehatan, rekomendasi obat, 
hingga sesi curhat psikologi.

Fitur Utama:
1. Listening Mode: Mendengarkan curhat user sebelum memberi saran.
2. Medical Diagnosis: Menganalisa gejala penyakit ringan.
3. Pharmacy Support: Memberikan rekomendasi obat apotek & herbal.
4. Academic Assistant: Memberikan motivasi untuk masalah kuliah.
5. Human-like Conversation: Bisa basa-basi dan bercanda.

------------------------------------------------------------
CARA MENJALANKAN APLIKASI
------------------------------------------------------------

1. Pastikan Python sudah terinstall di komputer.
2. Buka Terminal / CMD.
3. Masuk ke folder project.

4. LANGKAH 1: Generate Database (Hanya perlu sekali)
   Jalankan perintah:
   python src/bikin_csv_raksasa.py

   (Ini akan membuat file 'dataset_raksasa.csv' berisi 5000+ data)

5. LANGKAH 2: Jalankan Bot
   Jalankan perintah:
   python src/jalankan_bot_csv.py

6. Selesai! Silakan berinteraksi dengan AI.

------------------------------------------------------------
STRUKTUR FILE
------------------------------------------------------------
/src
  ├── bikin_csv_raksasa.py  (Generator Data)
  └── jalankan_bot_csv.py   (Engine AI Utama)
/data
  └── dataset_raksasa.csv   (Database Pengetahuan)