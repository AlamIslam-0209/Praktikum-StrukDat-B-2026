from tabulate import tabulate
from kurs import data_kurs
import konverter

def Tampilkan_tabel():
    head = ["Mata Uang", "Nilai(IDR)"]
    data = [[m, n] for m, n in data_kurs.items()]
    print(" ====KONVERTER MATA UANG====")
    print(tabulate(data, headers=head, tablefmt="grid"))

def main():
    Tampilkan_tabel()
    print("\n   =====MENU KONVERSI=====  ")
    print("1. IDR ke Mata Uang Asing")
    print("2. Mata Uang Asing ke IDR")
    pilihan = int(input("Pilih Konversi: "))
    
    if pilihan not in [1, 2]:
        print("Masukkan pilihan dengan benar!")
        return
    
    kode = input("Masukkan kode mata uang (USD/EUR/SGD/JPY): ").upper()
    
    if kode not in data_kurs:
        print("Maaf mata uang tidak tersedia")
        return
    
    nominal = float(input("Msukkan jumlah uang: "))
    
    if pilihan == 1:
        hasil = konverter.idr_to_asing(nominal, kode)
        print(f"{nominal:.2f} IDR = {hasil:.2f} {kode}")
        
    if pilihan == 2:
        hasil = konverter.asing_to_idr(nominal, kode)
        print(f"{nominal:.2f} {kode} = {hasil:.2f} IDR")
        
        
if __name__ == "__main__":
    main()