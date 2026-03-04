def tambah_buku(nama, harga, stok):
    if harga <= 0:
        print("harga barang tidak valid")
        return
    if stok < 0:
        print("stok barang tidak boleh negatif")
        return
    
    return {"nama" : nama,
            "harga" : harga,
            "stok" :stok}
  
list_buku = []
if __name__ == "__main__":

    for i in range(3):
        nama_buku = input(f"Masukkan nama buku ke-{i+1}: ")
        harga_buku = float(input(f"Masukan harga buku ke-{i+1}: "))
        stok_buku = int(input(f"masukkan stok buku ke-{i+1}: "))
        print("\n")
        
        list_buku.append(tambah_buku(nama_buku, harga_buku, stok_buku))
        # x += tambah_buku(nama_buku, harga_buku, stok_buku).items()
        # list_buku.append(list(x))
    print(list_buku)