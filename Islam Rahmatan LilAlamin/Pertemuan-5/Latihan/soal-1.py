'''
1. Diberikan list nilai mahasiswa: nilai_tugas = [70, 85, 90, 65, 80]
a. Ganti nilai 65 menjadi 75 menggunakan pencarian indeks.
b. Tambahkan nilai 95 ke dalam list, lalu urutkan list tersebut dari yang terbesar ke
terkecil.
c. Tampilkan jumlah total seluruh nilai dalam list tersebut.
d. Tampilkan pesan "Ada nilai sempurna" jika angka 100 ada di dalam list, jika tidak
tampilkan "Tidak ada”.
'''

nilai_tugas = [70, 85, 90, 65, 80]

nilai_tugas[nilai_tugas.index(65)] = 75

nilai_tugas.append(95)
nilai_tugas.sort(reverse=True)

print(nilai_tugas)

