from abc import ABC, abstractmethod

# ===============================
# 1. ABSTRACT CLASS
# ===============================
class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass


# ===============================
# 4. CUSTOM EXCEPTION
# ===============================
class PoinTidakValidError(Exception):
    """Error untuk poin negatif"""
    pass


# ===============================
# 2. CLASS TURUNAN + SPECIAL METHODS
# ===============================
class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    def akses(self):
        print(f"{self.nama} memiliki akses sebagai Member Premium.")

    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    def __add__(self, other):
        return self.poin + other.poin

    def __len__(self):
        return len(self.nama)


# ===============================
# FUNGSI VALIDASI INPUT POIN
# ===============================
def input_poin():
    nilai = input("Masukkan poin member: ").strip()

    if nilai == "":
        raise ValueError("Input tidak boleh kosong!")

    try:
        poin = int(nilai)
    except:
        raise ValueError("Poin harus berupa angka!")

    if poin < 0:
        raise PoinTidakValidError("Poin tidak boleh negatif!")

    return poin


# ===============================
# 3 & 5. PROGRAM UTAMA
# ===============================
if __name__ == "__main__":

    print("=== Membuat Member 1 ===")
    while True:
        try:
            p1 = input_poin()
            break
        except (ValueError, PoinTidakValidError) as e:
            print("ERROR:", e)

    m1 = Member("Ahmad", p1)

    print("\n=== Membuat Member 2 ===")
    while True:
        try:
            p2 = input_poin()
            break
        except (ValueError, PoinTidakValidError) as e:
            print("ERROR:", e)

    m2 = Member("Budi", p2)

    # ===========================
    # OUTPUT / DEMO
    # ===========================
    print("\n=== INFORMASI MEMBER ===")
    print(m1)
    print(m2)

    print("\n=== AKSES ===")
    m1.akses()
    m2.akses()

    print("\n=== OPERASI TAMBAHAN ===")
    print("Jumlah poin (m1 + m2):", m1 + m2)
    print("Panjang nama m1:", len(m1))
