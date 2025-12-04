# a. Dua class berbeda
class Laptop:
    def nyalakan(self):
        return "Laptop menyala..."


class Smartphone:
    def nyalakan(self):
        return "Smartphone menyala..."


# b. Fungsi duck typing
def tes_nyala(obj):
    print(obj.nyalakan())


# c. Demonstrasi duck typing
l = Laptop()
s = Smartphone()

tes_nyala(l)
tes_nyala(s)
