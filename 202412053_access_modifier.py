class ProgramStudi:
    def __init__(self, kode, ketua):
        # public
        self.kode = kode
        
        # protected
        self._ketua = ketua
        
        # private
        self.__anggaran = 500000000

    # Getter protected
    def get_ketua(self):
        return self._ketua

    # Setter protected
    def set_ketua(self, nama_baru):
        if not nama_baru:
            raise ValueError("Nama ketua tidak boleh kosong.")
        self._ketua = nama_baru

    # Getter private (wajib karena anggaran private)
    def get_anggaran(self):
        return self.__anggaran

    # Setter private
    def set_anggaran(self, nilai):
        if nilai < 0:
            raise ValueError("Anggaran tidak boleh negatif.")
        self.__anggaran = nilai

    def kurangi_anggaran(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah harus positif.")
        if jumlah > self.__anggaran:
            raise ValueError("Anggaran tidak mencukupi.")
        self.__anggaran -= jumlah
        return self.__anggaran


# Contoh penggunaan
if __name__ == "__main__":
    ps = ProgramStudi("TI", "Pak Wayan")

    print("Kode:", ps.kode)
    print("Ketua Prodi:", ps.get_ketua())
    print("Anggaran:", ps.get_anggaran())

    ps.set_ketua("Bu Diah")
    print("Ketua Prodi (baru):", ps.get_ketua())

    ps.kurangi_anggaran(100_000_000)
    print("Anggaran Tersisa:", ps.get_anggaran())
