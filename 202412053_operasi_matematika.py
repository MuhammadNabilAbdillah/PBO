def operasi():
    print("=== Operasi Matematika Aman ===")
    print("Pilih operasi:")
    print("1. Pembagian")
    print("2. Perkalian")

    pilihan = input("Masukkan pilihan (1/2): ").strip()
    x = input("Masukkan angka pertama: ").strip()
    y = input("Masukkan angka kedua: ").strip()

    try:
        # validasi input tidak boleh kosong
        if x == "" or y == "":
            raise ValueError("Input tidak boleh kosong")

        a = float(x)
        b = float(y)

        # validasi bilangan harus positif
        if a < 0 or b < 0:
            raise ValueError("Hanya angka positif yang diperbolehkan")

        if pilihan == "1":
            # PEMBAGIAN (bisa memunculkan ZeroDivisionError)
            hasil = a / b
        elif pilihan == "2":
            # PERKALIAN
            hasil = a * b
        else:
            raise ValueError("Pilihan operasi tidak valid. Gunakan 1 atau 2.")

    except ValueError as ve:
        print("Input salah:", ve)

    except ZeroDivisionError:
        print("Penyebut tidak boleh nol pada operasi pembagian!")

    except Exception as e:
        print("Terjadi kesalahan:", e)

    else:
        # hanya berjalan jika tidak ada error
        print(f"Hasil operasi: {hasil}")

    finally:
        print("Selesai memproses input.")


if __name__ == "__main__":
    operasi()
