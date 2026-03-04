katalog = [
{'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
{'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

def cari_buku(katalog, keyword):
    key = keyword
    count = 0

    ketemu = False
    for elemen in range(len(katalog)):
        if keyword in katalog[elemen]["nama"]:
            # print(katalog[elemen])
            ketemu = True
            if ketemu:
                count =+ 1
    if not ketemu:
        # print("Buku tidak ditemukan"
        pass
        
    # return katalog[elemen] if keyword in katalog[elemen]["nama"]  for elemen in range(len(katalog))
    return katalog[:count+1] if ketemu else f"buku tidak ketemu"
    
    
if __name__ == "__main__":
    a = cari_buku(katalog, 'D')
    print(a)
    