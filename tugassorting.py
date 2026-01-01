import csv
import time

data_asli = []

with open("student_mat.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data_asli.append(int(row["G3"]))  # nilai akhir


def bubble_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def insertion_sort(arr):
    data = arr.copy()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def selection_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def menu():
    print("\n=== PROGRAM SORTING & SEARCHING NILAI MAHASISWA ===")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")
    print("4. Quick Sort")
    print("5. Merge Sort")
    print("6. Search Data (Binary Search)")
    print("0. Keluar")

data_urut = []

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "0":
        print("Program selesai.")
        break

    elif pilihan in ["1","2","3","4","5"]:
        print("\nData sebelum diurutkan:")
        print(data_asli)

        start = time.time()

        if pilihan == "1":
            data_urut = bubble_sort(data_asli)
            nama = "Bubble Sort"
        elif pilihan == "2":
            data_urut = insertion_sort(data_asli)
            nama = "Insertion Sort"
        elif pilihan == "3":
            data_urut = selection_sort(data_asli)
            nama = "Selection Sort"
        elif pilihan == "4":
            data_urut = quick_sort(data_asli)
            nama = "Quick Sort"
        elif pilihan == "5":
            data_urut = merge_sort(data_asli)
            nama = "Merge Sort"

        end = time.time()

        print("\nData sesudah diurutkan:")
        print(data_urut)
        print(f"Waktu eksekusi {nama}: {end - start:.6f} detik")

    elif pilihan == "6":
        if not data_urut:
            print("⚠ Data belum diurutkan! Silakan sorting dulu.")
        else:
            cari = int(input("Masukkan nilai G3 yang dicari: "))
            hasil = binary_search(data_urut, cari)
            if hasil != -1:
                print(f"Nilai ditemukan pada index ke-{hasil}")
            else:
                print("Nilai tidak ditemukan")

    else:
        print("Pilihan tidak valid!")
