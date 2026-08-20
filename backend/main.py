from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import sqlite3
import os

# inisiasi aplikasi server API

app = FastAPI(
    title="Backend AI Service",
    version="1.0"
)

DB_PATH = "presensi.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS presensi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL)
        ''')
    conn.commit()
    conn.close()

init_db()

# Mendefinisikan skema input JSON menggunakan Pydantic
class SkemaInputWajah(BaseModel):
    id_kamera: str
    vektor_fitur: list

@app.get("/")
def home():
    return {
        "status": "Online",
        "service": "Server Backend API"
    }

# Endpoint khusus prosessing Model AI (HTTP POST)
@app.post("/api/v1/deteksi-wajah")
def deteksi_wajah(payload: SkemaInputWajah):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO presensi (nama) VALUES (?)", (f"Siswa_{payload.id_kamera}",))
    conn.commit()
    conn.close()

    #kita kembalikan menkadi paket data JSON standar
    return{
        "status_respon": "Sukses",
        "kamera_asal": payload.id_kamera,
        "hasil_identifikasi": "Siswa_Terverifikasi",   
    }

@app.get("/api/v1/data-presensi")
def get_presensi():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM presensi")
    data = cursor.fetchall()
    conn.close()
    return {"Total": len(data), "records": data}