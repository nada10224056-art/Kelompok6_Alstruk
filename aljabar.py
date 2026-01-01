import tkinter as tk
from tkinter import messagebox

# =========================
# FUNGSI MATRIKS
# =========================

def tambah():
    try:
        a11 = float(e_a11.get()); a12 = float(e_a12.get())
        a21 = float(e_a21.get()); a22 = float(e_a22.get())
        b11 = float(e_b11.get()); b12 = float(e_b12.get())
        b21 = float(e_b21.get()); b22 = float(e_b22.get())

        hasil = (
            f"[{a11+b11}  {a12+b12}]\n"
            f"[{a21+b21}  {a22+b22}]"
        )
        output.set(hasil)
    except:
        messagebox.showerror("Error", "Input tidak valid")

def kurang():
    try:
        a11 = float(e_a11.get()); a12 = float(e_a12.get())
        a21 = float(e_a21.get()); a22 = float(e_a22.get())
        b11 = float(e_b11.get()); b12 = float(e_b12.get())
        b21 = float(e_b21.get()); b22 = float(e_b22.get())

        hasil = (
            f"[{a11-b11}  {a12-b12}]\n"
            f"[{a21-b21}  {a22-b22}]"
        )
        output.set(hasil)
    except:
        messagebox.showerror("Error", "Input tidak valid")

def transpose():
    try:
        a11 = float(e_a11.get()); a12 = float(e_a12.get())
        a21 = float(e_a21.get()); a22 = float(e_a22.get())

        hasil = (
            f"[{a11}  {a21}]\n"
            f"[{a12}  {a22}]"
        )
        output.set(hasil)
    except:
        messagebox.showerror("Error", "Input tidak valid")

def determinan():
    try:
        a11 = float(e_a11.get()); a12 = float(e_a12.get())
        a21 = float(e_a21.get()); a22 = float(e_a22.get())

        det = a11*a22 - a12*a21
        output.set(f"Determinan = {det}")
    except:
        messagebox.showerror("Error", "Input tidak valid")

def invers():
    try:
        a11 = float(e_a11.get()); a12 = float(e_a12.get())
        a21 = float(e_a21.get()); a22 = float(e_a22.get())

        det = a11*a22 - a12*a21
        if det == 0:
            output.set("Tidak memiliki invers")
        else:
            hasil = (
                f"[{a22/det}  {-a12/det}]\n"
                f"[{-a21/det}  {a11/det}]"
            )
            output.set(hasil)
    except:
        messagebox.showerror("Error", "Input tidak valid")

def spl():
    try:
        a11 = float(e_a11.get()); a12 = float(e_a12.get())
        a21 = float(e_a21.get()); a22 = float(e_a22.get())
        b1 = float(e_b11.get()); b2 = float(e_b21.get())

        det = a11*a22 - a12*a21
        if det == 0:
            output.set("Tidak ada solusi unik")
        else:
            x = (b1*a22 - b2*a12)/det
            y = (a11*b2 - a21*b1)/det
            output.set(f"x = {x}\ny = {y}")
    except:
        messagebox.showerror("Error", "Input tidak valid")

# =========================
# GUI
# =========================

root = tk.Tk()
root.title("Tugas Besar Aljabar Geometri")
root.geometry("420x520")

tk.Label(root, text="Matriks A", font=("Arial", 12, "bold")).pack()
frameA = tk.Frame(root); frameA.pack()
e_a11 = tk.Entry(frameA, width=5); e_a11.grid(row=0, column=0)
e_a12 = tk.Entry(frameA, width=5); e_a12.grid(row=0, column=1)
e_a21 = tk.Entry(frameA, width=5); e_a21.grid(row=1, column=0)
e_a22 = tk.Entry(frameA, width=5); e_a22.grid(row=1, column=1)

tk.Label(root, text="Matriks B / b", font=("Arial", 12, "bold")).pack()
frameB = tk.Frame(root); frameB.pack()
e_b11 = tk.Entry(frameB, width=5); e_b11.grid(row=0, column=0)
e_b12 = tk.Entry(frameB, width=5); e_b12.grid(row=0, column=1)
e_b21 = tk.Entry(frameB, width=5); e_b21.grid(row=1, column=0)
e_b22 = tk.Entry(frameB, width=5); e_b22.grid(row=1, column=1)

tk.Label(root, text="Operasi", font=("Arial", 12, "bold")).pack(pady=5)
tk.Button(root, text="Penjumlahan", command=tambah).pack(fill="x")
tk.Button(root, text="Pengurangan", command=kurang).pack(fill="x")
tk.Button(root, text="Transpose", command=transpose).pack(fill="x")
tk.Button(root, text="Determinan", command=determinan).pack(fill="x")
tk.Button(root, text="Invers", command=invers).pack(fill="x")
tk.Button(root, text="SPL (Ax=b)", command=spl).pack(fill="x")

output = tk.StringVar()
tk.Label(root, text="Hasil:", font=("Arial", 12, "bold")).pack()
tk.Label(root, textvariable=output, bg="white", width=40, height=6).pack()

root.mainloop()
