# a. Class Penulis
class Penulis:
    def __init__(self, nama):
        self.nama = nama


# b. Class Buku (composition dengan Penulis)
class Buku:
    def __init__(self, judul, nama_penulis):
        self.judul = judul
        self.penulis = Penulis(nama_penulis)  # composition

    def info(self):
        return f"Buku: {self.judul}, Penulis: {self.penulis.nama}"


# c. Demonstrasi mengakses data penulis dari objek buku
b1 = Buku("Pemrograman Python", "Andi Wijaya")

print(b1.info())           # menampilkan informasi lengkap
print(b1.penulis.nama)     # akses langsung atribut penulis
