class Mesin:
    def __init__(self, jenis):
        self.jenis = jenis

    def hidupkan(self):
        return f"Mesin {self.jenis} hidup"


class Mobil:
    def __init__(self, merk, mesin):
        self.merk = merk
        self.mesin = mesin  # Composition

    def info(self):
        return f"Mobil {self.merk} dengan {self.mesin.hidupkan()}"


# Instansiasi
mesin = Mesin("Bensin")
mobil = Mobil("Honda", mesin)

print(mobil.info())
