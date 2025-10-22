import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ====== KONEKSI DATABASE ======
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # ubah sesuai konfigurasi MySQL kamu
            database="pepustakaan"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Gagal koneksi ke database: {err}")
        return None

# ====== LOGIN WINDOW ======
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Sistem Perpustakaan")
        self.root.geometry("350x250")

        tk.Label(root, text="Username").pack(pady=5)
        self.username = tk.Entry(root)
        self.username.pack()

        tk.Label(root, text="Password").pack(pady=5)
        self.password = tk.Entry(root, show="*")
        self.password.pack()

        tk.Button(root, text="Login", command=self.login).pack(pady=15)

    def login(self):
        user = self.username.get()
        pwd = self.password.get()

        if not user or not pwd:
            messagebox.showwarning("Warning", "Username dan Password wajib diisi")
            return

        conn = connect_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, pwd))
            result = cursor.fetchone()
            conn.close()

            if result:
                messagebox.showinfo("Success", f"Selamat datang, {result['username']}!")
                self.root.destroy()
                Dashboard(result).mainloop()
            else:
                messagebox.showerror("Error", "Username atau Password salah!")

# ====== DASHBOARD ======
class Dashboard(tk.Tk):
    def __init__(self, user_info):
        super().__init__()
        self.user_info = user_info
        self.title("Dashboard - Sistem Perpustakaan")
        self.geometry("800x600")

        tk.Label(self, text=f"Selamat datang, {self.user_info['username']}", font=("Arial", 12)).pack(pady=10)

        frame = tk.Frame(self)
        frame.pack(pady=10)
        tk.Button(frame, text="Manajemen Buku", width=20, command=self.open_buku).grid(row=0, column=0, padx=10)
        tk.Button(frame, text="Manajemen Anggota", width=20, command=self.open_anggota).grid(row=0, column=1, padx=10)
        tk.Button(frame, text="Logout", width=20, command=self.logout).grid(row=0, column=2, padx=10)

        # Statistik
        self.stats_label = tk.Label(self, text="")
        self.stats_label.pack(pady=10)
        self.load_stats()

    def load_stats(self):
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM buku")
            buku_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM anggota")
            anggota_count = cursor.fetchone()[0]
            self.stats_label.config(text=f"Jumlah Buku: {buku_count} | Jumlah Anggota: {anggota_count}")
            conn.close()

    def open_buku(self):
        BukuWindow(self)

    def open_anggota(self):
        AnggotaWindow(self)

    def logout(self):
        self.destroy()
        root = tk.Tk()
        LoginWindow(root)
        root.mainloop()

# ====== CRUD BUKU ======
class BukuWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Manajemen Buku")
        self.geometry("900x500")

        # Form input
        form_frame = tk.LabelFrame(self, text="Data Buku")
        form_frame.pack(fill="x", padx=10, pady=5)

        self.fields = {}
        labels = ["Kode Buku", "Judul", "Pengarang", "Penerbit", "Tahun Terbit", "Stok"]
        for i, label in enumerate(labels):
            tk.Label(form_frame, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=3)
            entry = tk.Entry(form_frame)
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.fields[label.lower().replace(" ", "_")] = entry

        tk.Button(form_frame, text="Tambah", command=self.tambah_buku).grid(row=0, column=2, padx=5)
        tk.Button(form_frame, text="Update", command=self.update_buku).grid(row=1, column=2, padx=5)
        tk.Button(form_frame, text="Hapus", command=self.hapus_buku).grid(row=2, column=2, padx=5)
        tk.Button(form_frame, text="Reset", command=self.clear_form).grid(row=3, column=2, padx=5)

        # Tabel data
        self.tree = ttk.Treeview(self, columns=("kode", "judul", "pengarang", "penerbit", "tahun", "stok"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.title())
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree.bind("<ButtonRelease-1>", self.select_item)

        self.load_buku()

    def load_buku(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT kode_buku, judul, pengarang, penerbit, tahun_terbit, stok FROM buku")
            for row in cursor.fetchall():
                self.tree.insert("", "end", values=row)
            conn.close()

    def tambah_buku(self):
        data = [self.fields[f].get() for f in self.fields]
        if not all(data):
            messagebox.showwarning("Warning", "Semua field wajib diisi!")
            return
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO buku (kode_buku, judul, pengarang, penerbit, tahun_terbit, stok)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, tuple(data))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sukses", "Data buku berhasil ditambahkan!")
            self.load_buku()
            self.clear_form()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Gagal menambah data: {err}")

    def select_item(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            for i, key in enumerate(self.fields):
                self.fields[key].delete(0, tk.END)
                self.fields[key].insert(0, values[i])

    def update_buku(self):
        data = [self.fields[f].get() for f in self.fields]
        if not all(data):
            messagebox.showwarning("Warning", "Semua field wajib diisi!")
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE buku SET judul=%s, pengarang=%s, penerbit=%s, tahun_terbit=%s, stok=%s
            WHERE kode_buku=%s
        """, (data[1], data[2], data[3], data[4], data[5], data[0]))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sukses", "Data buku berhasil diupdate!")
        self.load_buku()

    def hapus_buku(self):
        kode = self.fields["kode_buku"].get()
        if not kode:
            messagebox.showwarning("Warning", "Pilih data buku yang ingin dihapus!")
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM buku WHERE kode_buku=%s", (kode,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
        self.load_buku()
        self.clear_form()

    def clear_form(self):
        for field in self.fields.values():
            field.delete(0, tk.END)

# ====== CRUD ANGGOTA ======
class AnggotaWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Manajemen Anggota")
        self.geometry("900x500")

        form_frame = tk.LabelFrame(self, text="Data Anggota")
        form_frame.pack(fill="x", padx=10, pady=5)

        self.fields = {}
        labels = ["Kode Anggota", "Nama", "Alamat", "Telepon", "Email"]
        for i, label in enumerate(labels):
            tk.Label(form_frame, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=3)
            entry = tk.Entry(form_frame)
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.fields[label.lower().replace(" ", "_")] = entry

        tk.Button(form_frame, text="Tambah", command=self.tambah).grid(row=0, column=2, padx=5)
        tk.Button(form_frame, text="Update", command=self.update).grid(row=1, column=2, padx=5)
        tk.Button(form_frame, text="Hapus", command=self.hapus).grid(row=2, column=2, padx=5)
        tk.Button(form_frame, text="Reset", command=self.clear_form).grid(row=3, column=2, padx=5)

        self.tree = ttk.Treeview(self, columns=("kode", "nama", "alamat", "telepon", "email"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.title())
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree.bind("<ButtonRelease-1>", self.select_item)

        self.load_data()

    def load_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT kode_anggota, nama, alamat, telepon, email FROM anggota")
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)
        conn.close()

    def tambah(self):
        data = [self.fields[f].get() for f in self.fields]
        if not all(data):
            messagebox.showwarning("Warning", "Semua field wajib diisi!")
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO anggota (kode_anggota, nama, alamat, telepon, email)
            VALUES (%s, %s, %s, %s, %s)
        """, tuple(data))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sukses", "Data anggota berhasil ditambahkan!")
        self.load_data()
        self.clear_form()

    def select_item(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            for i, key in enumerate(self.fields):
                self.fields[key].delete(0, tk.END)
                self.fields[key].insert(0, values[i])

    def update(self):
        data = [self.fields[f].get() for f in self.fields]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE anggota SET nama=%s, alamat=%s, telepon=%s, email=%s WHERE kode_anggota=%s
        """, (data[1], data[2], data[3], data[4], data[0]))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sukses", "Data anggota berhasil diupdate!")
        self.load_data()

    def hapus(self):
        kode = self.fields["kode_anggota"].get()
        if not kode:
            messagebox.showwarning("Warning", "Pilih data yang ingin dihapus!")
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM anggota WHERE kode_anggota=%s", (kode,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
        self.load_data()
        self.clear_form()

    def clear_form(self):
        for field in self.fields.values():
            field.delete(0, tk.END)

# ====== MAIN ======
if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()
