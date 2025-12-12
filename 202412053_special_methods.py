class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

    # b. Mengembalikan panjang nama
    def __len__(self):
        return len(self.nama)

    # c. Mahasiswa dianggap sama jika nilai mereka sama
    def __eq__(self, other):
        return self.nilai == other.nilai


# d. Contoh penggunaan (minimal 2 objek)
m1 = Mahasiswa("Ahmad", 90)
m2 = Mahasiswa("Budi", 80)
m3 = Mahasiswa("Caca", 90)

print("=== Representasi String ===")
print(m1)
print(m2)
print(m3)

print("\n=== Perbandingan Kesetaraan Nilai (==) ===")
print("m1 == m2 :", m1 == m2)   # False
print("m1 == m3 :", m1 == m3)   # True → nilai sama (90)

print("\n=== Operasi Matematika ===")
print("m1 + m2 =", m1 + m2)
print("m1 * 2  =", m1 * 2)

print("\n=== Panjang Nama Mahasiswa (__len__) ===")
print("len(m1) =", len(m1))
print("len(m2) =", len(m2))

print("\n=== Sorting Berdasarkan Nilai ===")
list_mahasiswa = [m1, m2, m3]
sorted_list = sorted(list_mahasiswa, key=lambda x: x.nilai)

for m in sorted_list:
    print(m)
