# a. Membuat class Buku
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"{self.judul} - {self.penulis} ({self.tahun})"


# b. Membuat list berisi 5 objek Buku
daftar_buku = [
    Buku("Laskar Pelangi", "Andrea Hirata", 2005),
    Buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980),
    Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009),
    Buku("Sang Pemimpi", "Andrea Hirata", 2006),
    Buku("Ayat-Ayat Cinta", "Habiburrahman El Shirazy", 2004)
]


# c. Fungsi untuk mencari buku berdasarkan penulis
def cari_buku_berdasarkan_penulis(daftar_buku, nama_penulis):
    hasil = []
    for buku in daftar_buku:
        if buku.penulis.lower() == nama_penulis.lower():
            hasil.append(buku)
    return hasil


# d. Menampilkan hasil pencarian
penulis_dicari = "Andrea Hirata"
hasil_pencarian = cari_buku_berdasarkan_penulis(daftar_buku, penulis_dicari)

print(f"=== Hasil Pencarian Buku oleh {penulis_dicari} ===")
if hasil_pencarian:
    for buku in hasil_pencarian:
        print(buku.info())
else:
    print("Buku tidak ditemukan.")
