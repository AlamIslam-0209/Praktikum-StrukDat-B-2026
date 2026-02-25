"""
2. Diberikan sebuah list yang berisi beberapa tuple. Setiap tuple berisi (Nama, Nilai):
kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]
a. Gunakan perulangan untuk memproses setiap tuple tersebut. Jika nilai >= 75,
tampilkan: "Selamat [Nama], Anda Lulus!". Jika di bawah 75, tampilkan: "Maaf
[Nama], Anda harus remidi."
"""
kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]

print("\n".join(f"Selamat {data[0]}, Anda Lulus!" if data[1] >= 75 else f"Maaf {data[0]}, Anda harus remidi." for data in kumpulan_nilai))

# for data in kumpulan_nilai:
#     if data[1] >= 75:
#         print(f"Selamat {data[0]}, Anda Lulus!")
        
#     else:
#         print(f"Maaf {data[0]}, Anda harus remidi.")