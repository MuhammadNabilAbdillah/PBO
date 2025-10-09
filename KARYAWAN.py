class Perusahaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_proyek = [] # agreagtion
        self.daftar_tim = [] # composition

    def buat_proyek(self, nama_proyek, deskripsi):
        proyek_baru = Proyek(nama_proyek, deskripsi)
        self.daftar_proyek.append(proyek_baru)
        print(f"proyek '{nama_proyek}' telah dibuat di {self.nama}")
        return proyek_baru
    def buat_tim(self, nama_tim):
        tim_baru = Tim(nama_tim)
        self.daftar_tim.append(tim_baru)
        return tim_baru
    

class Proyek:
    def __init__(self, nama, deskripsi):
        self.nama = nama
        self.deskripsi = deskripsi
        self.tugas_list = [] 
    def tambah_tugas(self, deskripsi_tugas):
        tugas = Tugas(deskripsi_tugas)
        self.tugas_list.append(tugas)
        print(f"Tugas '{deskripsi_tugas}' telah ditambahkan ke proyek '{self.nama}'")
        return tugas
    

class Tim:
    def __init__(self, nama):
        self.nama = nama
        self.developers = [] 
    def tambah_developer(self, developer):
        self.developers.append(developer)


class Developer:
    def __init__(self, nama, keahlian):
        self.nama = nama
        self.keahlian = keahlian
class Tugas:
    def __init__(self, deskripsi):
        self.deskripsi = deskripsi
        self.developer = [] 
        pass
    def tugaskan_ke(self, developer):
        self.developer = developer
        print(f"Tugas '{self.deskripsi}' ditugaskan ke '{developer.nama}'")
        
perusahaan = Perusahaan("Indominco")

proyek1 = perusahaan.buat_proyek("Website Perusahaan", "toko online")

tim1 = perusahaan.buat_tim("Tim Frontend")

dev1 = Developer("Nabil", "Frontend Developer")
dev2 = Developer("Galang", "Backend Developer")
tim1.tambah_developer(dev1)
tim1.tambah_developer(dev2)


tugas1 = proyek1.tambah_tugas("Membuat data base")
tugas2 = proyek1.tambah_tugas("Membuat sistem login")


tugas1.tugaskan_ke(dev1)
tugas2.tugaskan_ke(dev2)