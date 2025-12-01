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
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data


def selection_sort(arr):
    data = arr.copy()
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


def quick_sort(arr):
    data = arr.copy()
    if len(data) <= 1:
        return data
    pivot = data[len(data)//2]
    kiri = [x for x in data if x < pivot]
    tengah = [x for x in data if x == pivot]
    kanan = [x for x in data if x > pivot]
    return quick_sort(kiri) + tengah + quick_sort(kanan)


def merge_sort(arr):
    data = arr.copy()
    if len(data) <= 1:
        return data
    mid = len(data)//2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


def merge(left, right):
    hasil = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            hasil.append(left[i])
            i += 1
        else:
            hasil.append(right[j])
            j += 1

    hasil.extend(left[i:])
    hasil.extend(right[j:])
    return hasil



def input_data():
    n = int(input("\nMasukkan jumlah data: "))
    data = []
    for i in range(n):
        angka = int(input(f"Data ke-{i+1}: "))
        data.append(angka)
    return data


print("PROGRAM SORTING DATA")

data = input_data()  # input pertama

while True:
    print("\nMENU SORTING")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")
    print("4. Quick Sort")
    print("5. Merge Sort")
    print("6. Input Data Baru")
    print("7. Keluar")

    pilih = input("Pilih menu (1-7): ")

    if pilih == "1":
        print("\nHasil Bubble Sort :", bubble_sort(data))

    elif pilih == "2":
        print("\nHasil Insertion Sort :", insertion_sort(data))

    elif pilih == "3":
        print("\nHasil Selection Sort :", selection_sort(data))

    elif pilih == "4":
        print("\nHasil Quick Sort :", quick_sort(data))

    elif pilih == "5":
        print("\nHasil Merge Sort :", merge_sort(data))

    elif pilih == "6":
        print("\n=== Input Data Baru ===")
        data = input_data()  # ulang input data

    elif pilih == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Coba lagi.")
