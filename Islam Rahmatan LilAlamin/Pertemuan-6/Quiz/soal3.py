import soal2

katalog = [
{'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
{'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]
riwayat_transaksi = set({})


def proses_transaksi(katalog, nama_buku, jumlah_beli):
    a = soal2.cari_buku(katalog, nama_buku)
    for i in range(len(a)):
        try:
            if nama_buku in a[i]["nama"]:
                if a[i]["stok"] >= jumlah_beli:
                    a[i]["stok"] -= jumlah_beli
                    riwayat_transaksi.add(a[i]["nama"])
                    print(a[i])
                else:
                    print("jumlah stok tidak mencukupi")
        except TypeError:
            print("Buku tidak ada")
            break
        
if __name__ == "__main__":
    proses_transaksi(katalog, "Data", 2)
    print(riwayat_transaksi)