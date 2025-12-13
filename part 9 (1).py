pengeluaran = []

while True:
    data = input("Masukkan pengeluaran (atau ketik 'stop' untuk selesai): ")

    if data.lower() == "stop":
        break

    pengeluaran.append(float(data))


if len(pengeluaran) == 0:
    print("Tidak ada data pengeluaran.")
else:
    total = sum(pengeluaran)
    rata2 = total / len(pengeluaran)
    terbesar = max(pengeluaran)
    terkecil = min(pengeluaran)

    print("\n--- Laporan keuangan ---")
    print(f"Total pengeluaran: {total}")
    print(f"Rata-rata: {rata2}")
    print(f"Pengeluaran terbesar: {terbesar}")
    print(f"Pengeluaran terkecil: {terkecil}")
