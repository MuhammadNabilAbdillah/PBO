# Class Person
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}"


# Class Mahasiswa (Inheritance dari Person)
class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)   # memanggil constructor parent
        self.nim = nim

    def info(self):
        return f"Mahasiswa: {self.nama}, Umur: {self.umur}, NIM: {self.nim}"


# Instansiasi objek
m1 = Mahasiswa("Rian", 20, "23051001")

# Memanggil method info()
print(m1.info())
