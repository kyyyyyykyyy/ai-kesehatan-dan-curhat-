import csv
import os
import sys
import time
import random
from difflib import SequenceMatcher

# --- SETUP LOKASI FILE DATA ---
current_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.dirname(current_dir)
csv_path = os.path.join(parent_dir, 'data', 'dataset_raksasa.csv')

def ketik(text, speed=0.015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- 1. BACA FILE CSV ---
knowledge_base = []

if not os.path.exists(csv_path):
    print(f"❌ ERROR: File CSV gak ketemu di {csv_path}")
    print("   Jalanin dulu 'bikin_csv_raksasa.py' bro!")
    sys.exit()

print("Membaca 5000 baris data...", end='\r')

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader) # Skip header (baris pertama)
    for row in reader:
        if len(row) >= 2:
            knowledge_base.append({"tanya": row[0], "jawab": row[1]})

print(f"✅ DATASET SIAP! ({len(knowledge_base)} Data Loaded)       ")
time.sleep(0.5)
clear_screen()

# --- 2. OTAK PENCARI ---
def cari_jawaban(user_input):
    user_input = user_input.lower()
    jawaban_terbaik = None
    skor_tertinggi = 0
    
    # Kita cek data secara acak (sampling) kalau datanya kegedean biar gak lemot
    # Atau cek semua kalau PC kuat. Untuk 5000 baris, cek semua masih cepet kok.
    
    for item in knowledge_base:
        tanya_db = item['tanya'].lower()
        
        # Logika Pencocokan
        kemiripan = SequenceMatcher(None, user_input, tanya_db).ratio()
        
        # Bonus skor kalau kata kunci pas
        if tanya_db in user_input:
            kemiripan += 0.2
            
        if kemiripan > skor_tertinggi:
            skor_tertinggi = kemiripan
            jawaban_terbaik = item['jawab']
    
    # Threshold (Ambang Batas)
    if skor_tertinggi > 0.45:
        return jawaban_terbaik
    return None

# --- 3. PROGRAM UTAMA ---
def main():
    print("==================================================")
    print("      🚑  AI BIG DATA HEALTH ASSISTANT  🚑")
    print(f"        (Powered by {len(knowledge_base)} Datasets)")
    print("==================================================")
    
    ketik("\n[AI]: Halo! Sistem Big Data siap. Silakan curhat atau tanya obat.")
    
    while True:
        print("\n" + "-"*50)
        user_text = input("🗣️  KAMU: ")
        
        if user_text.lower() in ['exit', 'keluar', 'bye']:
            ketik("\n[AI]: Bye! Sehat selalu. 👋")
            break
            
        # Animasi Loading biar keliatan mikir berat
        sys.stdout.write("\n[AI]: Scanning Database")
        for _ in range(3):
            time.sleep(0.1)
            sys.stdout.write(".")
            sys.stdout.flush()
        print("\r" + " "*30 + "\r", end="")
        
        jawaban = cari_jawaban(user_text)
        
        if jawaban:
            ketik(f"[AI]: {jawaban}")
        else:
            ketik("[AI]: Maaf, kombinasi kata ini belum ada di 5000 data saya. Coba persingkat?")

if __name__ == "__main__":
    main()