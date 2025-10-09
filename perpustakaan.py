# === TUGAS 1: SISTEM MANAJEMEN PERPUSTAKAAN ===

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []       # Menyimpan koleksi semua buku
        self.anggota_terdaftar = [] # Menyimpan daftar anggota yang sudah mendaftar
        self.data_peminjaman = []   # Menyimpan riwayat peminjaman buku

    def tambah_buku(self, buku):
        """Menambahkan buku ke koleksi perpustakaan"""
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.judul}' berhasil dimasukkan ke koleksi {self.nama}.")

    def tambah_anggota(self, anggota):
        """Mendaftarkan anggota baru ke perpustakaan"""
        self.anggota_terdaftar.append(anggota)
        print(f"Anggota baru '{anggota.nama}' telah resmi bergabung dengan {self.nama}.")

    def pinjam_buku(self, anggota, buku, tanggal_pinjam):
        """Melakukan proses peminjaman buku oleh anggota"""
        if buku in self.daftar_buku:
            transaksi = Peminjaman(anggota, buku, tanggal_pinjam)
            self.data_peminjaman.append(transaksi)
            print(f"{anggota.nama} meminjam '{buku.judul}' pada tanggal {tanggal_pinjam}.")
        else:
            print(f"Maaf, buku '{buku.judul}' tidak tersedia di {self.nama}.")

    def tampilkan_peminjaman(self):
        """Menampilkan seluruh data peminjaman yang terjadi"""
        print("\n=== DAFTAR PEMINJAMAN BUKU ===")
        if not self.data_peminjaman:
            print("Belum ada buku yang dipinjam.")
        else:
            for p in self.data_peminjaman:
                print(f"- {p.anggota.nama} meminjam '{p.buku.judul}' pada {p.tanggal_pinjam}")


# Class Buku: merepresentasikan informasi tentang buku
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis


# Class Anggota: menyimpan informasi tentang anggota perpustakaan
class Anggota:
    def __init__(self, nama):
        self.nama = nama


# Class Peminjaman: mencatat transaksi peminjaman buku
class Peminjaman:
    def __init__(self, anggota, buku, tanggal_pinjam):
        self.anggota = anggota
        self.buku = buku
        self.tanggal_pinjam = tanggal_pinjam


# === PROGRAM UTAMA ===
# Membuat objek perpustakaan
perpus = Perpustakaan("Perpustakaan Daerah")

# Membuat objek buku
buku1 = Buku("Sejarah Indonesia", "Pramoedya Ananta Toer")
buku2 = Buku("Hutan Amazon", "Pramoedya Ananta Toer")

# Membuat objek anggota
anggota1 = Anggota("Galang")

# Menambahkan buku ke koleksi
perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)

# Mendaftarkan anggota ke perpustakaan
perpus.tambah_anggota(anggota1)

# Melakukan peminjaman buku
perpus.pinjam_buku(anggota1, buku2, "2023-08-19")

# Menampilkan status seluruh peminjaman
perpus.tampilkan_peminjaman()
