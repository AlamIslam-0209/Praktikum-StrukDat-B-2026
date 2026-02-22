'''
Diberikan sebuah list angka:
angka = [10, 20, 30, 40, 50]
1. Tambahkan angka 60 ke dalam list.
2. Hapus angka 20 dari list.
3. Tampilkan angka tertinggi dan terendah
4. Hitung rata-rata angka setelah perubahan data
5. Tampilkan seluruh isi list setelah perubahan.
'''

angka = [10, 20, 30, 40, 50]
print(f"def: {angka}")

angka.append(60)
print(f"Setelah ditambah 60: {angka}")

angka.remove(20)
print(f"setelah dikurang 20: {angka}")

print("maksimum angka:",max(angka))

print("minimum angka:", min(angka))

total = 0
for num in angka:
    total += num
mean = total / len(angka)
print("rata rata:", mean)
print(angka)