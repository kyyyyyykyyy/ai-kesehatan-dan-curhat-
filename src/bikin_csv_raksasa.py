import csv
import os
import random

print("🏭 Memproduksi Dataset FINAL (All-in-One Response)...")

# --- TEMPLATE RAAPIH ---
templates = [
    # ========================================================
    # KATEGORI 1: IZIN CURHAT (PEMICU KHUSUS)
    # ========================================================
    {
        "keywords": ["mau curhat", "pengen cerita", "dengerin gw", "butuh temen ngobrol", "sesi curhat"],
        "prefixes": ["bro", "dok", "min", "tolong"],
        "answer": "🤝 **Siap Bro, Gw Dengerin.**\n\nLu ada masalah apa? Cerita aja semuanya. Gw gak bakal nge-judge. Apakah soal **Cinta**, **Tugas/Kuliah**, atau **Keluarga**?"
    },

    # ========================================================
    # KATEGORI 2: MASALAH HUBUNGAN (BERANTEM)
    # ========================================================
    {
        "keywords": ["berantem", "ribut", "cekcok", "adu mulut", "marahan", "emosi sama"],
        "prefixes": ["sama pacar", "sama dosen", "sama temen", "sama orang tua"],
        "answer": "❄️ **Cooling Down Dulu.**\n\nJangan ambil keputusan pas lagi emosi/marah. Mending lu ngejauh dulu, tarik napas, tidur. Besok pas kepala udah dingin, baru omongin lagi baik-baik."
    },

    # ========================================================
    # KATEGORI 3: MASALAH KULIAH
    # ========================================================
    {
        "keywords": ["nilai jelek", "ipk turun", "dapet e", "mengulang matkul", "remedial"],
        "prefixes": ["stres", "aduh", "takut", "gimana nih"],
        "answer": "🎓 **Tenang, Angka Bukan Segalanya.**\n\nSakit emang liat nilai jelek, tapi itu bukan kiamat.\n1. Cek apa yang salah (cara belajar/dosennya?).\n2. Perbaiki di semester depan.\n3. Fokus cari skill di luar kampus biar CV lu tetep ngeri!"
    },
    {
        "keywords": ["tugas numpuk", "stres tugas", "banyak pr", "skripsi pusing"],
        "prefixes": ["gila", "parah", "aduh", "capek"],
        "answer": "⏳ **Teknik Podomoro Bro.**\n\nJangan liatin tumpukan tugasnya, bikin stres. Kerjain 25 menit fokus, 5 menit main HP. Cicil satu-satu. Selesai gak selesai, yang penting dikerjain."
    },

    # ========================================================
    # KATEGORI 4: MEDIS (JAWABAN LENGKAP: KIMIA + HERBAL)
    # ========================================================
    {
        "keywords": ["sakit perut", "mules", "perih lambung", "maag", "asam lambung", "nyeri perut"],
        "prefixes": ["aduh", "sakit", "perut", "kenapa"],
        "answer": "🚑 **Diagnosa: Gangguan Pencernaan / Maag**\n\n💊 **Medis:**\n- *Antasida* (Promag/Mylanta) untuk netralin asam.\n- *Omeprazole* (kalau sering kambuh).\n\n🌿 **Herbal:**\n- Air rebusan Kunyit (bagus buat luka lambung).\n- Air tajin (air beras).\n- Madu hangat.\n\n⚠️ *Hindari kopi & pedas dulu ya!*"
    },
    {
        "keywords": ["sakit kepala", "pusing", "migrain", "kepala berat", "nyut nyutan"],
        "prefixes": ["aduh", "tolong", "kepala", "kenapa"],
        "answer": "🚑 **Diagnosa: Cephalgia (Sakit Kepala)**\n\n💊 **Medis:**\n- *Paracetamol* atau *Ibuprofen*.\n\n🌿 **Herbal:**\n- Teh Jahe hangat (melancarkan darah).\n- Oles minyak peppermint di pelipis.\n\n💡 *Coba tidur di ruang gelap & jauhkan HP.*"
    },
    {
        "keywords": ["demam", "panas", "meriang", "menggigil", "badan panas"],
        "prefixes": ["kayaknya", "rasanya", "tubuh", "anak"],
        "answer": "🚑 **Diagnosa: Demam (Febris)**\n\n💊 **Medis:**\n- *Paracetamol* (Sanmol/Panadol) tiap 4-6 jam.\n\n🌿 **Herbal:**\n- Air kelapa muda (cegah dehidrasi).\n- Kompres air hangat di lipatan tubuh.\n\n⚠️ *Kalau 3 hari gak turun, wajib cek darah (takut DBD)!*"
    },
    {
        "keywords": ["batuk", "gatal tenggorokan", "batuk kering", "berdahak"],
        "prefixes": ["lagi", "uhuk", "tenggorokan"],
        "answer": "🚑 **Diagnosa: Batuk / Radang**\n\n💊 **Medis:**\n- *OBH* atau *Ambroxol* (Pengencer dahak).\n- *Dextromethorphan* (Batuk kering).\n\n🌿 **Herbal:**\n- Jeruk nipis + Kecap/Madu.\n- Kencur dikunyah.\n\n🚫 *Stop gorengan & es!*"
    },
    {
        "keywords": ["flu", "pilek", "hidung mampet", "meler", "bersin"],
        "prefixes": ["lagi", "kena", "hidung"],
        "answer": "🚑 **Diagnosa: Influenza**\n\n💊 **Medis:**\n- *Mixagrip*, *Procold*, atau *Rhinos*.\n- Vitamin C 500mg.\n\n🌿 **Herbal:**\n- Uap air panas (hirup uapnya).\n- Jahe merah hangat.\n\n💡 *Istirahat total adalah obat terbaik.*"
    },

    # ========================================================
    # KATEGORI 5: BASA BASI (BIAR SOPAN)
    # ========================================================
    {
        "keywords": ["halo", "hi", "pagi", "siang", "malam", "woy", "assalamualaikum"],
        "prefixes": ["", "tes", "cek"],
        "answer": "👋 **Halo Bos!**\n\nGw Dr. AI. Gw siap bantu:\n1. 🚑 Diagnosa & Obat (Kimia/Herbal)\n2. 🧠 Teman Curhat 24 Jam\n\n*Ketik aja keluhan lu...*"
    },
    {
        "keywords": ["makasih", "thanks", "terima kasih", "ok", "siap"],
        "prefixes": ["oke", "sip", "yoi"],
        "answer": "Sama-sama bro! Sehat selalu ya. Jangan lupa istirahat. ✨"
    }
]

# --- MESIN GENERATOR ---
dataset_final = []
dataset_final.append(["pertanyaan", "jawaban"])

target_baris = 5000
count = 0

while count < target_baris:
    for item in templates:
        keyword = random.choice(item["keywords"])
        prefix = random.choice(item["prefixes"])
        
        # Variasi kalimat
        variasi = [
            f"{keyword}",
            f"{prefix} {keyword}",
            f"{keyword} {prefix}",
            f"gw {keyword}",
            f"lagi {keyword}",
            f"obat {keyword}" # Biar kalo nanya "obat sakit kepala" langsung nyambung
        ]
        
        kalimat_input = random.choice(variasi)
        dataset_final.append([kalimat_input, item["answer"]])
        count += 1
        if count >= target_baris: break

# --- SIMPAN ---
current_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.dirname(current_dir)
data_folder = os.path.join(parent_dir, 'data') 
os.makedirs(data_folder, exist_ok=True)
csv_path = os.path.join(data_folder, 'dataset_raksasa.csv')

with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(dataset_final)

print(f"✅ DATASET FINAL SELESAI: {csv_path}")