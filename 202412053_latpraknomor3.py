class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        # public
        self.nim = nim
        self.nama = nama

        # protected
        self._semester = semester

        # private
        self.__ipk = ipk

    def get_semester(self):
        return self._semester

    def get_ipk(self):
        return self.__ipk


# Membuat 2 objek Mahasiswa
m1 = Mahasiswa("23001", "Budi", 8, 3.44)
m2 = Mahasiswa("23002", "Siti", 6, 3.57)

# Menampilkan data
print("=== Data Mahasiswa 1 ===")
print("NIM:", m1.nim)
print("Nama:", m1.nama)
print("Semester:", m1.get_semester())
print("IPK:", m1.get_ipk())

print("\n=== Data Mahasiswa 2 ===")
print("NIM:", m2.nim)
print("Nama:", m2.nama)
print("Semester:", m2.get_semester())
print("IPK:", m2.get_ipk())
