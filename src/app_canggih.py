import streamlit as st
import csv
import os
import time
from difflib import SequenceMatcher
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Dr. AI Pro", page_icon="🚑", layout="wide")

# ================= ASSETS =================
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=3)
        return r.json() if r.status_code == 200 else None
    except: return None

lottie_doctor = load_lottieurl("https://lottie.host/575a66a3-2c1e-4537-bfd2-03d32db85f7a/u7Fv9kLz1a.json")
lottie_loading = load_lottieurl("https://lottie.host/b0e51576-6330-4e3a-967b-1178619dfd7b/l8l4t6w9i3.json")

# ================= DATABASE =================
@st.cache_data
def load_database():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    csv_path = os.path.join(parent_dir, 'data', 'dataset_raksasa.csv')
    knowledge_base = []
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            try: next(reader, None)
            except: pass
            for row in reader:
                if len(row) >= 2:
                    knowledge_base.append({"tanya": row[0], "jawab": row[1]})
    return knowledge_base

db = load_database()

# ================= LOGIC PINTAR (ANTI RANCU) =================
def cari_jawaban(user_input):
    user_input = user_input.lower()
    
    jawaban_terbaik = None
    skor_tertinggi = 0
    
    # KATA KUNCI PRIORITAS (Biar gak salah tangkap)
    # Kalau ada kata ini, boost skornya
    keywords_prioritas = ["sakit", "nyeri", "obat", "radang", "demam", "perut", "kepala", "curhat", "berantem"]
    
    for item in db:
        tanya_db = item['tanya'].lower()
        
        # Hitung kemiripan
        kemiripan = SequenceMatcher(None, user_input, tanya_db).ratio()
        
        # LOGIC BOOST: Kalau user ngetik "sakit perut" dan di database ada "sakit perut", 
        # kasih nilai sempurna biar gak kepilih yang lain.
        if tanya_db in user_input:
            kemiripan = 1.0 
        
        if kemiripan > skor_tertinggi:
            skor_tertinggi = kemiripan
            jawaban_terbaik = item['jawab']
    
    # DEBUG: Buka ini kalau mau liat skornya di terminal
    # print(f"Input: {user_input} | Match: {jawaban_terbaik[:20]}... | Skor: {skor_tertinggi}")

    # THRESHOLD
    if skor_tertinggi > 0.6: # Gw naikin jadi 0.6 biar selektif
        return jawaban_terbaik
    else:
        # Fallback kalau skor rendah
        return "Waduh, gw kurang nangkep maksudnya. Coba ketik inti keluhannya aja (Contoh: 'Sakit perut' atau 'Mau curhat')."

# ================= UI =================
st.markdown("""
<style>
    .stApp {background-color: #f0f4f8;}
    .stChatMessage[data-testid="user-message"] {background-color: #e3f2fd; border-radius: 15px 15px 0 15px;}
    .stChatMessage[data-testid="assistant-message"] {background-color: #ffffff; border-radius: 15px 15px 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.05);}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    if lottie_doctor: st_lottie(lottie_doctor, height=180, key="doc")
    else: st.header("👨‍⚕️")
    st.title("Dr. AI Pro")
    st.info("💡 **Tips:** Ketik keluhan langsung. \nContoh: 'Sakit perut' atau 'Obat flu'.")
    if st.button("Reset Chat 🗑️"):
        st.session_state.messages = []
        st.rerun()

st.title("🚑 Asisten Kesehatan & Curhat Pro")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Halo! Mau konsultasi medis atau curhat? Langsung ketik aja."}]

for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="👤" if message["role"] == "user" else "🤖"):
        st.markdown(message["content"])

if prompt := st.chat_input("Ketik keluhan disini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        placeholder = st.empty()
        if lottie_loading:
            with placeholder.container():
                st_lottie(lottie_loading, height=50, key=f"load_{int(time.time())}")
        else: placeholder.markdown("*Menganalisa...*")
        
        time.sleep(0.8) 
        jawaban = cari_jawaban(prompt)
        
        placeholder.empty()
        full_response = ""
        box = st.empty()
        for chunk in jawaban.split():
            full_response += chunk + " "
            time.sleep(0.02)
            box.markdown(full_response + "▌")
        box.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})