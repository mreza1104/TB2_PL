class Buku:
    def __init__(self, judul, penulis, penerbit=None, tahun_terbit=None, konten=None, iktisar=None):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.konten = konten if konten is not None else []
        self.iktisar = iktisar
