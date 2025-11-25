class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"{self.nama} sedang mengajar mata kuliah {mata_kuliah}."
    
# Membuat objek dosen
dosen1 = Dosen("Ir. Abadi Nugroho, S.Kom., M.Kom.", "1104129002")
dosen2 = Dosen("Herri Susanto, SS., M.Hum.", "1118097701")

# Menampilkan data
print(f"Nama Dosen : {dosen1.nama}")
print(f"NIDN       : {dosen1.nidn}")
print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))

print()

print(f"Nama Dosen : {dosen2.nama}")
print(f"NIDN       : {dosen2.nidn}")
print(dosen2.ajar_mata_kuliah("Publik Speaking"))
