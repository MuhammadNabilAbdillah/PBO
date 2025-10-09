# Class Produk → merepresentasikan barang yang dijual
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama          # Nama produk
        self.harga = harga        # Harga produk
        self.stok = stok          # Jumlah stok produk yang tersedia

    def __str__(self):
        return f"{self.nama} - Rp{self.harga:,} (Stok: {self.stok})"


# Class ItemPesanan → menyimpan data produk dan jumlah yang dipesan
class ItemPesanan:
    def __init__(self, produk, jumlah):
        self.produk = produk      # Produk yang dipesan
        self.jumlah = jumlah      # Jumlah unit yang dipesan

    def hitung_subtotal(self):
        return self.produk.harga * self.jumlah

    def __str__(self):
        return f"{self.produk.nama} x{self.jumlah} = Rp{self.hitung_subtotal():,}"


# Class Keranjang → menyimpan daftar produk yang ingin dibeli pelanggan
class Keranjang:
    def __init__(self):
        self.items = []           # List untuk menampung produk dan jumlahnya

    def tambah_produk(self, produk, jumlah):
        if produk.stok >= jumlah:
            self.items.append(ItemPesanan(produk, jumlah))
            produk.stok -= jumlah  # Kurangi stok saat produk dimasukkan ke keranjang
            print(f"{jumlah} unit {produk.nama} ditambahkan ke keranjang.")
        else:
            print(f"Stok {produk.nama} tidak mencukupi!")

    def tampilkan_keranjang(self):
        print("\nIsi Keranjang:")
        for item in self.items:
            print("-", item)


# Class Pesanan → hasil akhir dari keranjang pelanggan
class Pesanan:
    def __init__(self, pelanggan, items):
        self.pelanggan = pelanggan    # Pelanggan yang membuat pesanan
        self.items = items            # Item dari keranjang
        self.total = sum(item.hitung_subtotal() for item in items)

    def tampilkan_pesanan(self):
        print(f"\n=== Pesanan oleh {self.pelanggan.nama} ===")
        for item in self.items:
            print("-", item)
        print(f"Total: Rp{self.total:,}")


# Class Pelanggan → memiliki keranjang dan dapat membuat pesanan
class Pelanggan:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email
        self.keranjang = Keranjang()   # Komposisi: pelanggan memiliki keranjang
        self.riwayat_pesanan = []      # List untuk menyimpan pesanan yang sudah dibuat

    def buat_pesanan(self):
        if not self.keranjang.items: # Cek apakah keranjang kosong
            print("Keranjang kosong! Tidak bisa membuat pesanan.")
            return None
        pesanan = Pesanan(self, self.keranjang.items)
        self.riwayat_pesanan.append(pesanan)
        self.keranjang = Keranjang()   # Kosongkan keranjang setelah checkout
        print(f"\nPesanan berhasil dibuat oleh {self.nama}.")
        return pesanan


# === PROGRAM UTAMA (Contoh Penggunaan) ===
# Membuat produk
produk1 = Produk("Laptop", 12000000, 5)
produk2 = Produk("Mouse", 200000, 10)

# Membuat pelanggan
pelanggan1 = Pelanggan("Nabil", "nabil@example.com")

# Pelanggan menambahkan produk ke keranjang
pelanggan1.keranjang.tambah_produk(produk1, 1)
pelanggan1.keranjang.tambah_produk(produk2, 2)

# Menampilkan isi keranjang
pelanggan1.keranjang.tampilkan_keranjang()

# Membuat pesanan dari keranjang
pesanan1 = pelanggan1.buat_pesanan()

# Menampilkan detail pesanan
if pesanan1:
    pesanan1.tampilkan_pesanan()
