"""
Diberikan dua daftar hadir mahasiswa di dua sesi yang berbeda:
sesi_pagi = {"Andi", "Budi", "Cici"} sesi_siang = {"Budi", "Deni", "Eka"}
a. Tampilkan nama mahasiswa yang hadir di kedua sesi (pagi DAN siang)
b. Tampilkan total daftar nama unik yang hadir hari itu (semua mahasiswa dari kedua
sesi tanpa duplikat).
c. Gabungkan kedua set tersebut menjadi satu set bernama sesi_hari_ini.
"""

sesi_pagi = {"Andi", "Budi", "Cici"} 
sesi_siang = {"Budi", "Deni", "Eka"}

print(sesi_pagi & sesi_siang)

print(sesi_pagi - sesi_siang | sesi_siang - sesi_pagi)

sesi_hari_ini = sesi_pagi | sesi_siang
print(type(sesi_hari_ini))