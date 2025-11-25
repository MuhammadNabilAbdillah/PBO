class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        # Instance attributes
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info(self):
        return f"{self.merk} ({self.warna}, {self.tahun})"


# Membuat objek
mobil1 = Kendaraan("Toyota", "Merah", 2020)
mobil2 = Kendaraan("Honda", "Hitam", 2022)

# Menampilkan instance attribute
print("=== Instance Attribute ===")
print(mobil1.info())
print(mobil2.info())

# Menampilkan class attribute
print("\n=== Class Attribute ===")
print(f"Bahan Bakar (akses via class): {Kendaraan.bahan_bakar}")
print(f"Bahan Bakar (akses via objek mobil1): {mobil1.bahan_bakar}")
print(f"Bahan Bakar (akses via objek mobil2): {mobil2.bahan_bakar}")
