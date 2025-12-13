nama = input("Masukkan nama mahasiswa: ")

jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
total_nilai = 0

for i in range(1, jumlah_matkul + 1):
    nilai = float(input(f"Masukkan nilai mata kuliah ke-{i}: "))
    total_nilai += nilai

rata_rata = total_nilai / jumlah_matkul

if rata_rata >= 90:
    predikat = "A (Sangat Baik)"
elif rata_rata >= 80:
    predikat = "B (Baik)"
elif rata_rata >= 70:
    predikat = "C (Cukup)"
else:
    predikat = "D (Kurang)"

print("\n=== HASIL ===")
print("Nama Mahasiswa :", nama)
print("Rata-rata Nilai:", rata_rata)
print("Predikat      :", predikat)