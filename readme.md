# 📚 Sistem Manajemen Perpustakaan (Python + MySQL)

Aplikasi ini merupakan proyek GUI Python dengan integrasi **MySQL**, menggunakan **Tkinter** sebagai antarmuka.  
Fungsinya untuk mengelola data buku, anggota, dan sistem login sederhana.

---

## 🧩 Fitur Utama

### 🔐 1. Sistem Login
- Form login dengan validasi username & password.
- Autentikasi langsung dari tabel `users` di database.
- Menampilkan pesan kesalahan jika input kosong atau akun tidak ditemukan.

### 🏠 2. Dashboard
- Menampilkan nama user yang login.
- Menu navigasi ke:
  - Manajemen Buku
  - Manajemen Anggota
  - Logout
- Statistik otomatis:
  - Jumlah Buku
  - Jumlah Anggota

### 📚 3. Manajemen Buku
- CRUD (Create, Read, Update, Delete)
- Field:
  - Kode Buku
  - Judul
  - Pengarang
  - Penerbit
  - Tahun Terbit
  - Stok
- Validasi input wajib diisi.
- Data ditampilkan di `Treeview` dengan tampilan tabel.

### 👥 4. Manajemen Anggota
- CRUD (Create, Read, Update, Delete)
- Field:
  - Kode Anggota
  - Nama
  - Alamat
  - Telepon
  - Email
- Validasi input wajib diisi.
- Data ditampilkan di `Treeview`.

### 🎨 5. UI/UX
- Antarmuka dibuat dengan **Tkinter**.
- Layout rapi menggunakan `LabelFrame`, `Frame`, dan `Treeview`.
- Pesan konfirmasi/error menggunakan `messagebox`.

---

## 🧰 Teknologi yang Digunakan

| Komponen | Keterangan |
|-----------|-------------|
| **Bahasa** | Python 3 |
| **GUI Library** | Tkinter |
| **Database** | MySQL |
| **Koneksi DB** | mysql-connector-python |
| **IDE** | Visual Studio Code |

---

## ⚙️ Cara Menjalankan Program

### 1️⃣ Persiapan Lingkungan
Pastikan sudah menginstal:
- **Python 3.8+**
- **MySQL Server / XAMPP**
- **mysql-connector-python**

> Install library jika belum:
```bash
pip install mysql-connector-python
