import streamlit as st
import requests
import os

# Mengambil URL Backend dari DMS Docker
API_URL =  os.getenv("API_URL", "http://backend_service:8000")

st.title("System Presensi AI - Streamlit Web")

st.subheader("1. Simulasi Absensi Wajah")
id_kamera = st.text_input("ID KAMERA", value="CAM_LAB_01")

if st.button("Kirim Presensi"):
    payload = {
        "id_kamera": id_kamera,
        "vektor_fitur": [0.1, 0.2, 0.3]
    }
    try:
        res = requests.post(f"{API_URL}/api/v1/deteksi-wajah", json=payload)
        st.success(res.json())
    except Exception as e:
        st.error(f"gagal terhubung ke Backend: {e}")

st.divider()

st.subheader("2. Data Presensi di Database (SQLite)")
if st.button("Kirim Presensi"):

    try:
        res = requests.post(f"{API_URL}api/v1/data-presensi")
        st.json(res.json())
    except Exception as e:
        st.error(f"Gagal mengambil data: {e}")