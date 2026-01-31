import json
import os

print("🧠 Sedang meng-generate DATASET RAKSASA (Listening Mode Enabled)...")

# --- DATABASE PINTAR ---
raw_knowledge = [
    # ================= 1. LISTENING MODE (IZIN CURHAT) =================
    # Ini biar dia gak sotoy langsung kasih saran pas lu baru nyapa
    {
        "patterns": [
            "mau curhat", "pengen cerita", "dengerin gw dong", "boleh curhat ga", 
            "ada waktu ga", "mau ngomong", "butuh temen ngobrol", "gw mau curhat", 
            "curhat dong", "sesi curhat"
        ],
        "answer": "Boleh banget bro. Gw siap dengerin 24 jam. Mau cerita soal apa? Cinta, kerjaan, apa kuliah?"
    },
    {
        "patterns": [
            "bingung mau cerita apa", "gatau mulai darimana", "banyak masalah", "rumit banget"
        ],
        "answer": "Pelan-pelan aja bro. Coba keluarin satu per satu. Apa yang paling bikin kepikiran sekarang?"
    },

    # ================= 2. MASALAH CINTA (KOMPLIT) =================
    {
        "patterns": ["dighosting", "dia ngilang", "di ghosting", "tiba tiba ngilang", "chat ga dibales"],
        "answer": "Ghosting itu jawaban bro. Jawaban kalau dia gak cukup dewasa buat pamit. Jangan dikejar, nanti lu yang capek. Lu berhak dapet yang jelas."
    },
    {
        "patterns": ["friendzone", "kejebak friendzone", "cuma dianggap teman", "kakak adik zone"],
        "answer": "Sakit emang. Pilihannya cuma dua: Ungkapin biar jelas (resiko ditolak), atau mundur teratur buat nyelamatin hati lu."
    },
    {
        "patterns": ["ldr", "hubungan jarak jauh", "kangen pacar", "jarang ketemu"],
        "answer": "LDR itu ujian kepercayaan. Kuncinya komunikasi. Video call rutin, jangan curigaan mulu. Kalau jodoh gak kemana bro."
    },
    {
        "patterns": ["diselingkuhi", "dia selingkuh", "ketahuan chat sama orang lain", "punya simpenan"],
        "answer": "Selingkuh itu penyakit karakter, bukan khilaf. Kalau dia bisa lakuin sekali, dia bisa lakuin lagi. Selamatkan diri lu bro."
    },
    {
        "patterns": ["susah move on", "inget mantan", "kangen mantan", "belum bisa lupa"],
        "answer": "Wajar kok. Coba block sosmed dia dulu. Cari kesibukan baru. Obat patah hati itu cuma waktu dan orang baru (nanti)."
    },

    # ================= 3. KAMPUS & SKRIPSI (RELATABLE) =================
    {
        "patterns": ["nilai jelek", "dapet e", "ipk turun", "remedial", "mengulang matkul"],
        "answer": "Nilai di kertas gak nentuin kesuksesan bro. Evaluasi cara belajar, tapi jangan rendah diri. Masih ada semester depan buat bales dendam!"
    },
    {
        "patterns": ["dosen killer", "dosen galak", "takut sama dosen", "dosen rese"],
        "answer": "Anggap aja latihan mental buat dunia kerja. Ikutin aturannya, sopan, kerjain tugas. Asal nilai aman, kelar urusan."
    },
    {
        "patterns": ["judul skripsi ditolak", "revisian terus", "skripsi dicoret", "pusing skripsi"],
        "answer": "Skripsi yang bagus itu skripsi yang SELESAI. Gak usah perfeksionis. Cicil 1 paragraf sehari gapapa, yang penting maju."
    },
    {
        "patterns": ["salah jurusan", "gak minat kuliah", "terpaksa kuliah"],
        "answer": "Banyak orang sukses kerja gak sesuai jurusan. Jalanin aja kewajiban lu buat dapetin ijazah, sambil asah skill lain yang lu suka di luar kampus."
    },

    # ================= 4. MASALAH HIDUP (GENERAL) =================
    {
        "patterns": ["gak punya duit", "miskin", "bokek", "uang habis", "gaji kecil", "pengangguran"],
        "answer": "Fokus cari peluang, bukan ngeratain nasib. Bisa mulai dari freelance, jualan kecil-kecilan, atau upgrade skill biar nilai jual lu naik."
    },
    {
        "patterns": ["iri sama orang lain", "orang lain sukses", "merasa gagal", "kalah saing"],
        "answer": "Setiap orang punya zonawaktu masing-masing. Obama pensiun di umur 55, Trump baru jadi presiden di umur 70. Lu gak telat, lu cuma lagi proses."
    },
    {
        "patterns": ["capek kerja", "burnout", "lelah bekerja", "pengen resign"],
        "answer": "Kalau fisik capek, istirahat. Kalau hati capek, mungkin butuh liburan. Tapi kalau dompet butuh, ya semangat kerja lagi bro wkwk."
    },

    # ================= 5. KESEHATAN HARIAN (DOKTER) =================
    {
        "patterns": ["masuk angin", "kembung", "sendawa", "mual", "badan greges"],
        "answer": "Saran: Minum jahe hangat atau teh manis panas. Kerokan boleh dikit. Oles minyak kayu putih di perut & punggung."
    },
    {
        "patterns": ["jerawat", "muka jerawatan", "breakout", "wajah kusam"],
        "answer": "Saran: Cuci muka rutin, jangan pegang muka pake tangan kotor. Kurangi gorengan & begadang. Bisa pake obat totol jerawat (Benzolac/Acnes)."
    },
    {
        "patterns": ["rambut rontok", "kebotakan", "rambut tipis"],
        "answer": "Saran: Ganti sampo anti-hairfall. Pakai hair tonic ginseng/lidah buaya. Kurangi stres (stres bikin rontok parah)."
    },
    {
        "patterns": ["sakit pinggang", "boyok", "nyeri punggung", "pegal duduk"],
        "answer": "Saran: Kurangi duduk bungkuk. Lakukan stretching tiap 1 jam. Bisa tempel koyo atau minum Vitamin B Complex (Neurobion)."
    },
    {
        "patterns": ["mata minus", "penglihatan kabur", "sakit mata", "mata merah"],
        "answer": "Saran: Istirahatkan mata tiap 20 menit liat layar (Rumus 20-20-20). Kalau merah iritasi, tetes Insto/Visine. Kalau buram terus, cek optik."
    },
    {
        "patterns": ["sakit kepala", "pusing", "migrain", "kepala berat"],
        "answer": "Saran: Minum Paracetamol. Tidur di ruang gelap. Jangan main HP dulu. Kalau pusing muter-muter (vertigo), jangan bangun mendadak."
    },
    {
        "patterns": ["demam", "panas", "badan hangat", "menggigil"],
        "answer": "Saran: Minum air putih yang banyak. Kompres dahi. Minum Paracetamol. Kalau 3 hari gak turun, cek darah (waspada DBD/Tifus)."
    },
    
    # ================= 6. BASA BASI MANUSIAWI =================
    {
        "patterns": ["halo", "hi", "hai", "pagi", "siang", "sore", "malam", "woy", "tes"],
        "answer": "Halo bos! Sehat? Ada yang bisa dibantu? Mau konsultasi atau sekadar ngobrol?"
    },
    {
        "patterns": ["makasih", "thanks", "terima kasih", "tq", "thank you"],
        "answer": "Sama-sama bro! Sehat selalu ya. Jangan lupa istirahat."
    },
    {
        "patterns": ["siapa kamu", "nama kamu", "bot ya"],
        "answer": "Gw Asisten AI lu. Gw didesain buat jadi temen curhat yang gak ember, plus tau dikit soal medis."
    },
    {
        "patterns": ["haha", "wkwk", "lucu", "kocak", "hehe"],
        "answer": "Ketawa itu sehat bro. Bagus buat imun tubuh!"
    }
]

# --- ENGINE GENERATOR ---
final_dataset = []

for item in raw_knowledge:
    for question in item['patterns']:
        final_dataset.append({
            "tanya": question,
            "jawab": item['answer']
        })

# --- SIMPAN DATA ---
current_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.dirname(current_dir) 
data_folder = os.path.join(parent_dir, 'data') 

os.makedirs(data_folder, exist_ok=True)
file_path = os.path.join(data_folder, 'otak_kesehatan.json')

with open(file_path, 'w') as f:
    json.dump(final_dataset, f, indent=4)

print("="*60)
print(f"✅ DATASET RAKSASA BERHASIL DIBUAT: {len(final_dataset)} Variasi Data")
print("   Sekarang bot lu bisa bedain 'Mau curhat' vs 'Isi curhat'.")
print("="*60)