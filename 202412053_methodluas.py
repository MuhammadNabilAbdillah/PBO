import math

# a. Class Bentuk
class Bentuk:
    def luas(self):
        return 0


# b. Class Persegi
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi


# b. Class Lingkaran
class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def luas(self):
        return math.pi * (self.radius ** 2)


# c. Demonstrasi pemanggilan method
p = Persegi(4)
l = Lingkaran(7)

print("Luas Persegi:", p.luas())
print("Luas Lingkaran:", l.luas())
