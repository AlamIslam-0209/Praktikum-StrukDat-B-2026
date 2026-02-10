'''
Diberikan sebuah tuple data mahasiswa:
mahasiswa = ("A001", "Budi", "Informatika")
1. Tampilkan nama mahasiswa dari tuple tersebut.
2. Tampilkan seluruh isi tuple menggunakan perulangan for.
3. Jelaskan satu alasan mengapa tuple tidak bisa diubah.
'''


mahasiswa = ("A001", "Budi", 'Informatika')

print(f"Mahasiswa: {mahasiswa}")

for i in mahasiswa:
    print(i)

""" 
alasan mengapa tuple tidak bisa di ubah karena 
tuple sendiri bersifat immutable atau unchangable 
alias tidak bisa diubah. biasanya tuple digunakan untuk operasi matematika
"""

