# Custom Exceptions
class UmurTidakValidError(Exception):
    """Umum: umur tidak masuk akal."""
    pass

class UmurTerlaluMudaError(Exception):
    """Umur < 5 tidak diizinkan."""
    pass

class UmurTerlaluTuaError(Exception):
    """Umur > 100 tidak diizinkan."""
    pass

class AkunTidakDiizinkanError(Exception):
    """Umur < 18 tidak boleh daftar akun."""
    pass


# Validasi umur
def set_umur(umur):
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")

    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda! Minimal 5 tahun.")

    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua! Maksimal 100 tahun.")

    return umur


# Validasi pembuatan akun
def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError("Akun hanya untuk umur 18 ke atas!")
    return "Akun berhasil dibuat."


# Program utama — input berulang hingga valid
if __name__ == "__main__":
    while True:
        try:
            u = int(input("Masukkan umur: "))
            umur = set_umur(u)
            print(f"Umur valid: {umur}")
            break  # keluar dari loop jika valid

        except ValueError:
            print("ERROR: Input harus berupa bilangan bulat!\n")

        except (UmurTidakValidError, UmurTerlaluMudaError, UmurTerlaluTuaError) as e:
            print("ERROR:", e, "\n")

    # Coba daftar akun
    try:
        hasil = daftar_akun(umur)
        print(hasil)
    except AkunTidakDiizinkanError as e:
        print("ERROR:", e)
