import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os


# 1. Class Mahasiswa
class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self):
        return f"{self.nim} - {self.nama} ({self.jurusan}) - IPK: {self.ipk:.2f}"

    def update_ipk(self, new_ipk):
        self.ipk = new_ipk


# 2. Sistem Manajemen Mahasiswa
class ManajemenMahasiswaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Mahasiswa")
        self.root.geometry("800x500")

        # Dictionary untuk menyimpan objek mahasiswa dengan NIM sebagai key
        self.data_mahasiswa = {}

        # === Frame Input ===
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack(fill=tk.X)

        tk.Label(frame_input, text="NIM:").grid(row=0, column=0, sticky=tk.W)
        self.entry_nim = tk.Entry(frame_input, width=20)
        self.entry_nim.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_input, text="Nama:").grid(row=1, column=0, sticky=tk.W)
        self.entry_nama = tk.Entry(frame_input, width=20)
        self.entry_nama.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame_input, text="Jurusan:").grid(row=0, column=2, sticky=tk.W)
        self.entry_jurusan = tk.Entry(frame_input, width=20)
        self.entry_jurusan.grid(row=0, column=3, padx=5, pady=2)

        tk.Label(frame_input, text="IPK:").grid(row=1, column=2, sticky=tk.W)
        self.entry_ipk = tk.Entry(frame_input, width=20)
        self.entry_ipk.grid(row=1, column=3, padx=5, pady=2)

        # === Frame Tombol CRUD & Lainnya ===
        frame_tombol = tk.Frame(root, padx=10, pady=5)
        frame_tombol.pack(fill=tk.X)

        tk.Button(frame_tombol, text="Tambah", command=self.tambah_mahasiswa).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus", command=self.hapus_mahasiswa).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Cari", command=self.cari_mahasiswa).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Update IPK", command=self.update_ipk_mahasiswa).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Filter Jurusan", command=self.filter_jurusan).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Rata-rata IPK", command=self.rata_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="IPK Tertinggi", command=self.ipk_tertinggi).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Eksport Data", command=self.eksport_data).pack(side=tk.LEFT, padx=5)

        # === Treeview untuk menampilkan data mahasiswa ===
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame_tabel, columns=("NIM", "Nama", "Jurusan", "IPK"), show="headings")
        self.tree.heading("NIM", text="NIM")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Jurusan", text="Jurusan")
        self.tree.heading("IPK", text="IPK")
        self.tree.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame_tabel, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # ===== Fungsi CRUD & Lainnya =====
    def tambah_mahasiswa(self):
        nim = self.entry_nim.get().strip()
        nama = self.entry_nama.get().strip()
        jurusan = self.entry_jurusan.get().strip()
        ipk_text = self.entry_ipk.get().strip()

        if not nim or not nama or not jurusan or not ipk_text:
            messagebox.showwarning("Peringatan", "Harap isi semua field!")
            return

        try:
            ipk = float(ipk_text)
            if ipk < 0 or ipk > 4:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Peringatan", "IPK harus angka 0-4")
            return

        if nim in self.data_mahasiswa:
            messagebox.showwarning("Peringatan", "Mahasiswa dengan NIM ini sudah ada!")
            return

        mhs = Mahasiswa(nim, nama, jurusan, ipk)
        self.data_mahasiswa[nim] = mhs
        self.update_treeview()
        self.clear_entries()
        messagebox.showinfo("Sukses", "Mahasiswa berhasil ditambahkan!")

    def hapus_mahasiswa(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih mahasiswa yang akan dihapus!")
            return

        nim = self.tree.item(selected_item[0])["values"][0]
        if nim in self.data_mahasiswa:
            del self.data_mahasiswa[nim]
            self.update_treeview()
            messagebox.showinfo("Sukses", "Mahasiswa berhasil dihapus!")

    def cari_mahasiswa(self):
        keyword = simpledialog.askstring("Cari Mahasiswa", "Masukkan NIM atau Nama:")
        if not keyword:
            return

        hasil = [m for m in self.data_mahasiswa.values()
                 if keyword.lower() in m.nim.lower() or keyword.lower() in m.nama.lower()]

        self.tree.delete(*self.tree.get_children())
        for mhs in hasil:
            self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def update_ipk_mahasiswa(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih mahasiswa untuk update IPK!")
            return

        nim = self.tree.item(selected_item[0])["values"][0]
        mhs = self.data_mahasiswa.get(nim)
        if not mhs:
            return

        new_ipk_text = simpledialog.askstring("Update IPK", f"Masukkan IPK baru untuk {mhs.nama} (0-4):")
        if not new_ipk_text:
            return

        try:
            new_ipk = float(new_ipk_text)
            if new_ipk < 0 or new_ipk > 4:
                raise ValueError
            mhs.update_ipk(new_ipk)
            self.update_treeview()
        except ValueError:
            messagebox.showwarning("Peringatan", "IPK harus angka 0-4")

    def filter_jurusan(self):
        jurusan = simpledialog.askstring("Filter Jurusan", "Masukkan jurusan:")
        if not jurusan:
            return
        hasil = [m for m in self.data_mahasiswa.values() if jurusan.lower() in m.jurusan.lower()]
        self.tree.delete(*self.tree.get_children())
        for mhs in hasil:
            self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def rata_ipk(self):
        if not self.data_mahasiswa:
            messagebox.showinfo("Info", "Belum ada mahasiswa")
            return
        total = sum(m.ipk for m in self.data_mahasiswa.values())
        rata = total / len(self.data_mahasiswa)
        messagebox.showinfo("Rata-rata IPK", f"Rata-rata IPK: {rata:.2f}")

    def ipk_tertinggi(self):
        if not self.data_mahasiswa:
            messagebox.showinfo("Info", "Belum ada mahasiswa")
            return
        mhs_max = max(self.data_mahasiswa.values(), key=lambda m: m.ipk)
        messagebox.showinfo("IPK Tertinggi", f"{mhs_max.info()}")

    def eksport_data(self):
        if not self.data_mahasiswa:
            messagebox.showinfo("Info", "Belum ada mahasiswa")
            return
        with open("data_mahasiswa.txt", "w") as f:
            for mhs in self.data_mahasiswa.values():
                f.write(f"{mhs.nim},{mhs.nama},{mhs.jurusan},{mhs.ipk}\n")
        messagebox.showinfo("Sukses", f"Data berhasil dieksport ke {os.path.abspath('data_mahasiswa.txt')}")

    # Utility
    def update_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def clear_entries(self):
        self.entry_nim.delete(0, tk.END)
        self.entry_nama.delete(0, tk.END)
        self.entry_jurusan.delete(0, tk.END)
        self.entry_ipk.delete(0, tk.END)


# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = ManajemenMahasiswaApp(root)
    root.mainloop()
