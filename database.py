import psycopg2
from fastapi import HTTPException

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="perpus",
            user="username",   # Sesuaikan dengan username basis data Anda
            password="password",  # Sesuaikan dengan password basis data Anda
            host="localhost",
            port="3306"
        )
        return conn
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Koneksi ke basis data gagal: {e}")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS buku (
            id SERIAL PRIMARY KEY,
            judul VARCHAR(255) NOT NULL,
            penulis VARCHAR(255) NOT NULL,
            penerbit VARCHAR(255),
            tahun_terbit INT,
            konten TEXT,
            iktisar TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def get_buku(judul):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM buku WHERE judul = %s", (judul,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row

def post_buku(buku):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, konten, iktisar)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, '\n'.join(buku.konten), buku.iktisar))
    conn.commit()
    cursor.close()
    conn.close()
