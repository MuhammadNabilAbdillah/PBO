class Buku:
    # Class attribute
    perpustakaan = "Perpustakaan STITEK"

    # Constructor
    def __init__(self, judul, penulis, tahun):
        # Instance attributes
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info_buku(self):
        return f"Buku {self.judul} oleh {self.penulis} ({self.tahun})"


# Instansiasi object
buku1 = Buku("Pemrograman Python", "John Doe", 2023)
buku2 = Buku("Struktur Data", "Jane Doe", 2022)

print(buku1.info_buku())
print(buku2.info_buku())
print(f"Lokasi: {Buku.perpustakaan}")
