class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def __str__(self):
        return f"{self.kode} - {self.nama} ({self.sks} SKS)"


class ProgramStudi:
    def __init__(self, nama_prodi):
        self.nama_prodi = nama_prodi
        self.mata_kuliah = []

    def tambah_mk(self, mk):
        self.mata_kuliah.append(mk)

    def list_mk(self):
        return self.mata_kuliah


class Nilai:
    def __init__(self, mata_kuliah, nilai):
        self.mata_kuliah = mata_kuliah
        self.nilai = nilai


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []

    def tambah_nilai(self, nilai_obj):
        self.daftar_nilai.append(nilai_obj)

    def list_nilai(self):
        return self.daftar_nilai

    # (f) Rata-rata
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0
        total = sum(n.nilai for n in self.daftar_nilai)
        return round(total / len(self.daftar_nilai), 2)


class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.program_studi = []

    def tambah_prodi(self, prodi):
        self.program_studi.append(prodi)

    def list_prodi(self):
        return self.program_studi


# === Function Report Program ===
def report_program(prodi):
    print(f"\n=== REPORT PROGRAM STUDI: {prodi.nama_prodi} ===")
    for mk in prodi.list_mk():
        print(f"- {mk}")


# ===========================================================
#                     BAGIAN UTAMA PROGRAM
# ===========================================================
if  __name__ == "__main__":

    univ = Universitas("Universitas Teknologi Nusantara")

    prodi1 = ProgramStudi("Informatika")
    prodi2 = ProgramStudi("Sistem Informasi")
    univ.tambah_prodi(prodi1)
    univ.tambah_prodi(prodi2)

    mk1 = MataKuliah("IF101", "Algoritma & Struktur Data", 3)
    mk2 = MataKuliah("IF102", "Pemrograman Python", 3)
    prodi1.tambah_mk(mk1)
    prodi1.tambah_mk(mk2)

    mk3 = MataKuliah("SI201", "Analisis Sistem", 3)
    mk4 = MataKuliah("SI202", "Basis Data", 3)
    prodi2.tambah_mk(mk3)
    prodi2.tambah_mk(mk4)

    mhs1 = Mahasiswa("20241001", "musya")
    mhs2 = Mahasiswa("20241002", "tika")
    mhs3 = Mahasiswa("20241003", "ninda")

    mhs1.tambah_nilai(Nilai(mk1, 85))
    mhs1.tambah_nilai(Nilai(mk2, 90))

    mhs2.tambah_nilai(Nilai(mk1, 75))
    mhs2.tambah_nilai(Nilai(mk3, 88))

    mhs3.tambah_nilai(Nilai(mk2, 92))
    mhs3.tambah_nilai(Nilai(mk4, 81))

    print("\n=== DAFTAR MATA KULIAH SETIAP PRODI ===")
    for prodi in univ.list_prodi():
        print(f"\nProgram Studi: {prodi.nama_prodi}")
        for mk in prodi.list_mk():
            print(f"- {mk}")

    print("\n=== DATA NILAI MAHASISWA ===")
    for m in [mhs1, mhs2, mhs3]:
        print(f"\nMahasiswa: {m.nama} ({m.nim})")
        for n in m.list_nilai():
            print(f"- {n.mata_kuliah.nama} : {n.nilai}")

    print("\n=== RATA-RATA NILAI ===")
    for m in [mhs1, mhs2, mhs3]:
        print(f"{m.nama} : {m.rata_rata()}")

    for prodi in univ.list_prodi():
        report_program(prodi)
