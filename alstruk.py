import tkinter as tk
from tkinter import messagebox

pesanan = []
total_penjualan = 0
jumlah_transaksi = 0


def pesan_menu():
    global total_penjualan, jumlah_transaksi

    nama = entry_nama.get()
    meja = entry_meja.get()
    menu = entry_menu.get()
    harga = entry_harga.get()

    if nama == "" or meja == "" or menu == "" or harga == "":
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")
        return

    data = {
        "nama": nama,
        "meja": int(meja),
        "menu": menu,
        "harga": int(harga)
    }

    pesanan.append(data)
    total_penjualan += int(harga)     
    jumlah_transaksi += 1             

    tampil_pesanan()
    messagebox.showinfo("Sukses", "Pesanan berhasil ditambahkan!")

    entry_nama.delete(0, tk.END)
    entry_meja.delete(0, tk.END)
    entry_menu.delete(0, tk.END)
    entry_harga.delete(0, tk.END)


    pesanan.append(data)
    total_penjualan += int(harga)
    tampil_pesanan()
    messagebox.showinfo("Sukses", "Pesanan berhasil ditambahkan!")

    entry_nama.delete(0, tk.END)
    entry_meja.delete(0, tk.END)
    entry_menu.delete(0, tk.END)
    entry_harga.delete(0, tk.END)

def tampil_pesanan():
    listbox.delete(0, tk.END)
    for p in pesanan:
        listbox.insert(
            tk.END,
            f"Meja {p['meja']} | {p['nama']} | {p['menu']} | Rp{p['harga']}"
        )
def pesan_menu():
    global total_penjualan, jumlah_transaksi

    nama = entry_nama.get()
    meja = entry_meja.get()
    menu = entry_menu.get()
    harga = entry_harga.get()

    if nama == "" or meja == "" or menu == "" or harga == "":
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")
        return

    data = {
        "nama": nama,
        "meja": int(meja),
        "menu": menu,
        "harga": int(harga)
    }

    pesanan.append(data)
    total_penjualan += int(harga)     
    jumlah_transaksi += 1             

    tampil_pesanan()
    messagebox.showinfo("Sukses", "Pesanan berhasil ditambahkan!")

    entry_nama.delete(0, tk.END)
    entry_meja.delete(0, tk.END)
    entry_menu.delete(0, tk.END)
    entry_harga.delete(0, tk.END)  

def proses_pesanan():
    if not pesanan:
        messagebox.showinfo("Info", "Tidak ada pesanan.")
        return

    p = pesanan.pop(0)  # QUEUE
    tampil_pesanan()
    messagebox.showinfo(
        "Proses Pesanan",
        f"Pesanan Meja {p['meja']} sedang diproses"
    )

def urutkan_pesanan():
    if not pesanan:
        messagebox.showinfo("Info", "Belum ada pesanan.")
        return

    pesanan.sort(key=lambda x: x['meja'])  
    tampil_pesanan()

    messagebox.showinfo(
        "Sukses",
        "Pesanan berhasil diurutkan berdasarkan nomor meja"
    )


def laporan_penjualan():
    messagebox.showinfo(
        "Laporan Penjualan",
        f"=== LAPORAN PENJUALAN KESELURUHAN ===\n"
        f"Jumlah Transaksi : {jumlah_transaksi}\n"
        f"Total Penjualan  : Rp{total_penjualan}"
    )


# ================= GUI =================
root = tk.Tk()
root.title("Sistem Layanan Restoran")
root.geometry("500x600")

tk.Label(root, text="SISTEM LAYANAN RESTORAN", font=("Arial", 14, "bold")).pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nama Pelanggan").grid(row=0, column=0)
tk.Label(frame_input, text="Nomor Meja").grid(row=1, column=0)
tk.Label(frame_input, text="Menu").grid(row=2, column=0)
tk.Label(frame_input, text="Harga").grid(row=3, column=0)

entry_nama = tk.Entry(frame_input)
entry_meja = tk.Entry(frame_input)
entry_menu = tk.Entry(frame_input)
entry_harga = tk.Entry(frame_input)

entry_nama.grid(row=0, column=1)
entry_meja.grid(row=1, column=1)
entry_menu.grid(row=2, column=1)
entry_harga.grid(row=3, column=1)

tk.Button(root, text="Pesan Menu", width=25, command=pesan_menu).pack(pady=5)
tk.Button(root, text="Proses Pesanan", width=25, command=proses_pesanan).pack(pady=5)
tk.Button(root, text="Urutkan Berdasarkan Meja", width=25, command=urutkan_pesanan).pack(pady=5)
tk.Button(root, text="Laporan Penjualan", width=25, command=laporan_penjualan).pack(pady=5)

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

tk.Button(root, text="Keluar", width=25, command=root.quit).pack(pady=10)

root.mainloop()
