class Karyawan:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        return self.gaji_pokok

    def info(self):
        return f"Karyawan : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji()}"


class Manager(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

    def info(self):
        return f"Manager : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji()}"


class Programmer(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, bonus):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.bonus = bonus

    def hitung_gaji(self):
        return self.gaji_pokok + self.bonus

    def info(self):
        return f"Programmer : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji()}"


# === Program utama ===
m = Manager("Muhammad Nabil Abdillah", "202412053", 17000000, 3000000)
p = Programmer("Taroqi", "P001", 13000000, 3000000)

print(m.info())
print(p.info())
