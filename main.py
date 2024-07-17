from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from buku import Buku
from database import create_table, get_buku, post_buku
from logger import log_info, log_error

app = FastAPI()

class BukuModel(BaseModel):
    judul: str
    penulis: str
    penerbit: str
    tahun_terbit: int
    konten: List[str]
    iktisar: str

@app.on_event("startup")
def startup():
    create_table()
    log_info("Tabel buku dibuat.")

@app.post("/buku/", response_model=BukuModel)
def create_buku(buku: BukuModel):
    buku_obj = Buku(buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, buku.konten, buku.iktisar)
    post_buku(buku_obj)
    log_info(f"Buku '{buku.judul}' oleh {buku.penulis} telah disimpan.")
    return buku

@app.get("/buku/{judul}", response_model=BukuModel)
def read_buku(judul: str):
    data_buku = get_buku(judul)
    if data_buku:
        return BukuModel(
            judul=data_buku[1],
            penulis=data_buku[2],
            penerbit=data_buku[3],
            tahun_terbit=data_buku[4],
            konten=data_buku[5].split('\n') if isinstance(data_buku[5], str) else [],
            iktisar=data_buku[6]
        )
    else:
        log_error(f"Buku dengan judul '{judul}' tidak ditemukan.")
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
