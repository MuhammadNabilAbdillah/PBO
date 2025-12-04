class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        return f"{self.nama} | Gaji Pokok: {self.gaji_pokok}"


# =============================
# 2. Child Class: Manager
# =============================
class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def info_gaji(self):   # overriding
        total = self.gaji_pokok + self.tunjangan
        return f"Manager {self.nama} | Total Gaji: {total}"


# =============================
# 3. Child Class: Programmer
# =============================
class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    def info_gaji(self):   # overriding
        total = self.gaji_pokok + self.bonus
        return f"Programmer {self.nama} | Total Gaji: {total}"


# =============================
# 4. Composition: Departemen
# =============================
class Departemen:
    def __init__(self, nama_dept):
        self.nama_dept = nama_dept
        self.daftar_karyawan = []  # list of objects → composition

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_karyawan(self):
        print(f"\n=== DAFTAR KARYAWAN DEPARTEMEN {self.nama_dept} ===")
        for k in self.daftar_karyawan:
            print(k.info_gaji())   # polymorphism (method overriding)


# =============================
# 5. INSTANSIASI
# =============================

# 2 Manager
m1 = Manager("Andi", 5_000_000, 2_000_000)
m2 = Manager("Dina", 6_000_000, 2_500_000)

# 2 Programmer
p1 = Programmer("Rizky", 4_500_000, 1_000_000)
p2 = Programmer("Siti", 4_800_000, 1_200_000)

# Departemen
dept = Departemen("IT")

# Tambahkan ke departemen
dept.tambah_karyawan(m1)
dept.tambah_karyawan(m2)
dept.tambah_karyawan(p1)
dept.tambah_karyawan(p2)

# Tampilkan info
dept.tampilkan_karyawan()
