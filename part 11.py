pengeluaran = []

while True:
    print("\n=== PENCATAT PENGELUARAN ===")
    print("1. Tambah Pengeluaran")
    print("2. Lihat Pengeluaran")
    print("3. Total Pengeluaran")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tanggal = input("Masukkan tanggal (DD-MM-YYYY): ")
        keterangan = input("Masukkan keterangan: ")
        jumlah = int(input("Masukkan jumlah (Rp): "))

        data = {
            "tanggal": tanggal,
            "keterangan": keterangan,
            "jumlah": jumlah
        }

        pengeluaran.append(data)
        print("Pengeluaran berhasil ditambahkan.")

    elif pilihan == "2":
        if len(pengeluaran) == 0:
            print("Belum ada data pengeluaran.")
        else:
            print("\nDaftar Pengeluaran:")
            for i, p in enumerate(pengeluaran, start=1):
                print(f"{i}. {p['tanggal']} | {p['keterangan']} | Rp{p['jumlah']}")

    elif pilihan == "3":
        total = sum(p["jumlah"] for p in pengeluaran)
        print("Total Pengeluaran: Rp", total)

    elif pilihan == "4":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.")
