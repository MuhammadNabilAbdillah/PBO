class ManajerInventori:
    def __init__(self):
        self.inventori = {}

    def tambah_barang(self, nama, jumlah):
        if jumlah <= 0:
            return "Jumlah harus lebih dari 0"
        if nama in self.inventori:
            self.inventori[nama] += jumlah
        else:
            self.inventori[nama] = jumlah
        return f"Berhasil menambahkan {jumlah} {nama}. Stok sekarang: {self.inventori[nama]}"

    def hapus_barang(self, nama, jumlah):
        if nama not in self.inventori:
            return "Barang tidak ditemukan."
        if jumlah <= 0:
            return "Jumlah harus lebih dari 0"
        if jumlah > self.inventori[nama]:
            return "Stok tidak mencukupi."
        self.inventori[nama] -= jumlah
        if self.inventori[nama] == 0:
            del self.inventori[nama]
        return f"Berhasil mengurangi {jumlah} {nama}."

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong."
        output = "=== Daftar Inventori ===\n"
        for nama, stok in self.inventori.items():
            output += f"{nama}: {stok}\n"
        return output


# Demonstrasi
inv = ManajerInventori()

print(inv.tambah_barang("Pensil", 50))
print(inv.tambah_barang("Buku", 30))
print(inv.tambah_barang("Pensil", 20))  # Menambah stok barang yang sudah ada

print(inv.hapus_barang("Buku", 10))     # Mengurangi stok
print(inv.hapus_barang("Pensil", 70))    # Mengurangi stok hingga habis atau tidak cukup

print(inv.lihat_inventori())
