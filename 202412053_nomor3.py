import tkinter as tk
from tkinter import messagebox


class AplikasiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi GUI Sederhana")
        self.root.geometry("300x200")

        # Label
        self.label = tk.Label(
            root,
            text="Masukkan Teks:",
            font=("Arial", 11)
        )
        self.label.pack(pady=10)

        # Entry
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        # Button tampilkan isi Entry
        self.btn_tampil = tk.Button(
            root,
            text="Tampilkan",
            command=self.tampilkan_teks
        )
        self.btn_tampil.pack(pady=5)

        # Button hapus isi Entry
        self.btn_hapus = tk.Button(
            root,
            text="Hapus",
            command=self.hapus_teks
        )
        self.btn_hapus.pack(pady=5)

    def tampilkan_teks(self):
        teks = self.entry.get()
        if teks:
            messagebox.showinfo("Isi Entry", teks)
        else:
            messagebox.showwarning("Peringatan", "Entry masih kosong!")

    def hapus_teks(self):
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiGUI(root)
    root.mainloop()
