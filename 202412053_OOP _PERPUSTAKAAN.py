# ================================
# CLASS BUKU
# ================================
class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul                # public
        self.penulis = penulis            # public
        self.kode_buku = kode_buku        # public
        self._stok = stok                 # protected
        self.__lokasi_rak = lokasi_rak    # private

    # Getter lokasi rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    # Setter lokasi rak
    def set_lokasi_rak(self, lokasi_baru):
        self.__lokasi_rak = lokasi_baru

    # Menambah stok
    def tambah_stok(self, jumlah):
        self._stok += jumlah

    # Mengurangi stok
    def kurangi_stok(self, jumlah):
        if self._stok >= jumlah:
            self._stok -= jumlah
        else:
            print("Stok tidak mencukupi!")

    def info_buku(self):
        return f"{self.judul} | {self.penulis} | Stok: {self._stok} | Rak: {self.get_lokasi_rak()}"


# ================================
# CLASS PEMINJAMAN
# ================================
class Peminjaman:
    def __init__(self, kode_buku, tanggal_pinjam, tanggal_kembali, status):
        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status  # "Dipinjam" / "Dikembalikan"

    def info_peminjaman(self):
        return f"{self.kode_buku} | Pinjam: {self.tanggal_pinjam} | Kembali: {self.tanggal_kembali} | Status: {self.status}"


# ================================
# CLASS ANGGOTA
# ================================
class Anggota:
    def __init__(self, id_anggota, nama):
        self.id_anggota = id_anggota           # public
        self.nama = nama                       # public
        self._maks_pinjam = 3                  # protected
        self.__status_aktif = True             # private
        self.daftar_peminjaman = []            # aggregation

    # getter / setter status
    def get_status(self):
        return self.__status_aktif

    def set_status(self, status):
        self.__status_aktif = status

    # Pinjam buku
    def pinjam_buku(self, buku: Buku, tanggal_pinjam, tanggal_kembali):
        if not self.__status_aktif:
            print("Anggota tidak aktif!")
            return

        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print("Maksimum peminjaman tercapai!")
            return

        if buku._stok <= 0:
            print(f"Buku '{buku.judul}' tidak tersedia!")
            return

        buku.kurangi_stok(1)
        peminjaman = Peminjaman(buku.kode_buku, tanggal_pinjam, tanggal_kembali, "Dipinjam")
        self.daftar_peminjaman.append(peminjaman)

    # Kembalikan buku
    def kembalikan_buku(self, buku: Buku):
        for pinjam in self.daftar_peminjaman:
            if pinjam.kode_buku == buku.kode_buku and pinjam.status == "Dipinjam":
                pinjam.status = "Dikembalikan"
                buku.tambah_stok(1)
                return
        print("Peminjaman tidak ditemukan!")

    def info_anggota(self):
        return f"{self.nama} ({self.id_anggota}) | Status: {'Aktif' if self.__status_aktif else 'Tidak Aktif'}"


# ================================
# CLASS PERPUSTAKAAN (composition)
# ================================
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.buku_list = []  # composition

    def tambah_buku(self, buku: Buku):
        self.buku_list.append(buku)


# ================================
# PROGRAM UTAMA
# ================================
if __name__ == "__main__":
    # Buat perpustakaan
    perpustakaan = Perpustakaan("Perpustakaan Kota")

    # 3 buku
    b1 = Buku("Algoritma", "Joko", "BK001", 3, "A1")
    b2 = Buku("Python Dasar", "Siti", "BK002", 2, "B2")
    b3 = Buku("Database", "Budi", "BK003", 4, "C3")

    perpustakaan.tambah_buku(b1)
    perpustakaan.tambah_buku(b2)
    perpustakaan.tambah_buku(b3)

    # 2 anggota
    a1 = Anggota("AG001", "Andi")
    a2 = Anggota("AG002", "Maya")

    # Peminjaman
    a1.pinjam_buku(b1, "2024-12-01", "2024-12-10")
    a1.pinjam_buku(b2, "2024-12-01", "2024-12-10")

    a2.pinjam_buku(b3, "2024-12-02", "2024-12-11")

    # Pengembalian
    a1.kembalikan_buku(b1)

    # ============================================
    # DEMONSTRASI OUTPUT
    # ============================================
    print("\n=== INFORMASI BUKU ===")
    for b in perpustakaan.buku_list:
        print(b.info_buku())

    print("\n=== INFORMASI ANGGOTA ===")
    print(a1.info_anggota())
    print(a2.info_anggota())

    print("\n=== DAFTAR PEMINJAMAN ANGGOTA ===")
    for a in [a1, a2]:
        print(f"\n{a.nama}:")
        if not a.daftar_peminjaman:
            print("  Tidak ada peminjaman.")
        for p in a.daftar_peminjaman:
            print(" ", p.info_peminjaman())
