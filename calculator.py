def calculator():
    print("=== Kalkulator Sederhana ===")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    
    pilihan = input("Pilih operasi (1/2/3/4): ")
    
    if pilihan not in ["1", "2", "3", "4"]:
        print("Pilihan tidak valid!")
        return
    
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input harus berupa angka!")
        return
    
    if pilihan == "1":
        hasil = angka1 + angka2
        operasi = "+"
    elif pilihan == "2":
        hasil = angka1 - angka2
        operasi = "-"
    elif pilihan == "3":
        hasil = angka1 * angka2
        operasi = "*"
    elif pilihan == "4":
        if angka2 == 0:
            print("Error: Tidak bisa membagi dengan nol!")
            return
        hasil = angka1 / angka2
        operasi = "/"
    
    print(f"\nHasil: {angka1} {operasi} {angka2} = {hasil}")

calculator()
