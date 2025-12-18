# a. Membuat class Pelanggan
class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"{self.id_pelanggan} - {self.nama} ({self.email})"


# b. Dictionary untuk menyimpan objek pelanggan
data_pelanggan = {}


# c. Fungsi menambah pelanggan
def tambah_pelanggan(data, pelanggan):
    data[pelanggan.id_pelanggan] = pelanggan
    print("Pelanggan berhasil ditambahkan.")


def hapus_pelanggan(data, id_pelanggan):
    if id_pelanggan in data:
        del data[id_pelanggan]
        print("Pelanggan berhasil dihapus.")
    else:
        print("Pelanggan tidak ditemukan.")


def cari_pelanggan(data, id_pelanggan):
    if id_pelanggan in data:
        return data[id_pelanggan]
    return None


# Menambahkan beberapa pelanggan
tambah_pelanggan(data_pelanggan, Pelanggan("PL001", "Andi", "andi@email.com"))
tambah_pelanggan(data_pelanggan, Pelanggan("PL002", "Budi", "budi@email.com"))
tambah_pelanggan(data_pelanggan, Pelanggan("PL003", "Citra", "citra@email.com"))


# d. Menampilkan seluruh daftar pelanggan
print("\n=== Daftar Pelanggan ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())


# Contoh mencari pelanggan
id_cari = "PL002"
hasil = cari_pelanggan(data_pelanggan, id_cari)
if hasil:
    print(f"\nPelanggan ditemukan: {hasil.info()}")
else:
    print("\nPelanggan tidak ditemukan.")
