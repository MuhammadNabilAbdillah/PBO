import tkinter as tk
from tkinter import messagebox, ttk, simpledialog


class Tugas:
    def __init__(self, nama, selesai=False):
        self.nama = nama
        self.selesai = selesai


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x400")

        # List untuk menyimpan tugas
        self.daftar_tugas = []

        # Frame input
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack(fill=tk.X)

        tk.Label(frame_input, text="Tugas:").pack(side=tk.LEFT)
        self.entry_tugas = tk.Entry(frame_input, width=30)
        self.entry_tugas.pack(side=tk.LEFT, padx=5)

        tk.Button(frame_input, text="Tambah", command=self.tambah_tugas).pack(side=tk.LEFT, padx=5)

        # Frame tombol aksi
        frame_tombol = tk.Frame(root, padx=10, pady=5)
        frame_tombol.pack(fill=tk.X)

        tk.Button(frame_tombol, text="Hapus", command=self.hapus_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Edit", command=self.edit_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Tandai Selesai", command=self.tandai_selesai).pack(side=tk.LEFT, padx=5)

        # Treeview untuk menampilkan tugas
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame_tabel, columns=("Tugas", "Status"), show="headings")
        self.tree.heading("Tugas", text="Tugas")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame_tabel, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def tambah_tugas(self):
        nama_tugas = self.entry_tugas.get()
        if nama_tugas:
            tugas_baru = Tugas(nama_tugas)
            self.daftar_tugas.append(tugas_baru)
            self.update_treeview()
            self.entry_tugas.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Masukkan tugas terlebih dahulu!")

    def hapus_tugas(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = int(selected_item[0])
            del self.daftar_tugas[index]
            self.update_treeview()
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan dihapus!")

    def edit_tugas(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = int(selected_item[0])
            tugas = self.daftar_tugas[index]
            new_name = simpledialog.askstring("Edit Tugas", "Masukkan nama tugas baru:", initialvalue=tugas.nama)
            if new_name:
                tugas.nama = new_name
                self.update_treeview()
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan diedit!")

    def tandai_selesai(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = int(selected_item[0])
            tugas = self.daftar_tugas[index]
            tugas.selesai = True
            self.update_treeview()
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan ditandai selesai!")

    def update_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for idx, tugas in enumerate(self.daftar_tugas):
            status = "Selesai" if tugas.selesai else "Belum selesai"
            self.tree.insert("", tk.END, iid=idx, values=(tugas.nama, status))


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
