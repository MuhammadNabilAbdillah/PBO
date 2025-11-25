# Class Mahasiswa
class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan
    def perkenalan_diri(self):
        return f"Halo, saya {self.nama} ({self.nim}) dari jurusan {self.jurusan}, Universitas {Mahasiswa.universitas}"

    # Method update IPK
    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        return f"IPK {self.nama} telah diperbarui menjadi {self.ipk}"

    # Method predikat kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"


# INSTANSIASI 3 OBJECT
mhs1 = Mahasiswa("Danis Martanius", "202412035", "Teknik Informatika", 3.6)
mhs2 = Mahasiswa("Muhammad Nabil Abdillah", "202412053", "Sistem Informasi", 3.1)
mhs3 = Mahasiswa("Galang Surya", "202412043", "Teknik Informatika", 2.4)

# DEMONSTRASI METHOD
print(mhs1.perkenalan_diri())
print(mhs1.predikat_kelulusan())

print(mhs2.perkenalan_diri())
print(mhs2.update_ipk(3.4))
print(mhs2.predikat_kelulusan())

print(mhs3.perkenalan_diri())
print(mhs3.update_ipk(2.7))
print(mhs3.predikat_kelulusan())
