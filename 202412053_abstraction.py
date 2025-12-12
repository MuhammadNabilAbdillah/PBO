from abc import ABC, abstractmethod
import math

class Bentuk(ABC):

    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass


class Lingkaran(Bentuk):

    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * math.pi * self.jari_jari


class Persegi(Bentuk):

    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return 4 * self.sisi


class PersegiPanjang(Bentuk):

    def __init__(self, panjang, lebar, warna):
        self.panjang = panjang
        self.lebar = lebar
        self.warna = warna

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def info(self):
        return f"Persegi Panjang berwarna {self.warna}"


# ============================
# Contoh Penggunaan
# ============================

l = Lingkaran(5)
p = PersegiPanjang(4, 3, "biru")
s = Persegi(6)

print(f"Luas Lingkaran: {l.luas():.2f}")
print(f"Keliling Lingkaran: {l.keliling():.2f}")

print(f"Luas Persegi Panjang: {p.luas()}")
print(f"Keliling Persegi Panjang: {p.keliling()}")
print(p.info())     # menampilkan warna

print(f"Luas Persegi: {s.luas()}")
print(f"Keliling Persegi: {s.keliling()}")
