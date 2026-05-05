pasien_hari_ini = [
{"id": "P001", "nama": "Andi", "usia": 34, "penyakit":
"Flu", "bayar": False},
{"id": "P002", "nama": "Budi", "usia": 22, "penyakit":
"Tifus", "bayar": True},
{"id": "P003", "nama": "Cici", "usia": 45, "penyakit":
"Flu", "bayar": False},
{"id": "P004", "nama": "Dani", "usia": 30, "penyakit":
"Maag", "bayar": True},
{"id": "P005", "nama": "Eva", "usia": 28, "penyakit":
"Tifus", "bayar": False},
{"id": "P006", "nama": "Fajar", "usia": 17, "penyakit":
"Maag", "bayar": False},
]

## SOal 1

def Tampilkan_pasien(lst):
    print("No |  ID   |  Nama  | Usia |  Penyakit  |  Status Bayar")
    for i in range(len(lst)):
        print(i + 1, end="  |  ")
        for j in lst[i]:
            print(str(lst[i][j]), end=" | ",)
        print()
        
Tampilkan_pasien(pasien_hari_ini)

def filter_belum_bayar(lst):
    belum = []
    for i in range(len(lst)):
        if not lst[i]["bayar"]:
            belum.append(lst[i]["nama"])
    belum = sorted(belum)
    print("===pasien belum bayar===")
    for i, nama in enumerate(belum):
        print(f"{i+1}.", nama)
    print("Total belum bayar:", len(belum))
    return belum
    
filter_belum_bayar(pasien_hari_ini)



#Soal 2

def info_klinik():
    nama   = "Nama   : Klinik Sehat Bersama"
    alamat = "Alamat : Jalan Merdeka No. 10, Pekanbaru"
    telp   = "Telp   : 0761-12345"
    
    return nama, alamat, telp

nama_klinik, alamat_klinik, telp_klinik = info_klinik()
# print(nama_klinik, alamat_klinik, telp_klinik)
print("Info klinik")
print(nama_klinik)
print(alamat_klinik)
print(telp_klinik)

def rekap_penyakit(lst):
    result = list()
    
    for i in range(len(lst)):
        result.append(lst[i]["penyakit"])
    print(result)
    penyakit = set(result)
    
    print("Jenis penyakit unik:", penyakit)
    
    print("Rekap Per penyakit")
    for nama in penyakit:
        jlh = result.count(nama)
        print(nama, ':', jlh)
        
    penyakit_terbanyak = max(penyakit)
    print("Penyakit terbanyak:",penyakit_terbanyak)
        
rekap_penyakit(pasien_hari_ini)


#soal 3


class Pasien:
    jumlah_pasien = 0
    def __init__(self, id, nama, penyakit):
        self.__id = id
        self.__nama = nama
        self.__penyakit = penyakit
        self.jumlah_pasien += 1
        
    def get_id(self):
        return self.__id
    
    def get_nama(self):
        return self.__nama
    
    def get_penyakit(self):
        return self.__penyakit
    
    @staticmethod
    def hitung_pasien():
        return Pasien.jumlah_pasien
    
class PasienDarurat(Pasien):
    def __init__(self, id, nama, penyakit, prioritas):
        super.__init__(id, nama, penyakit)
        self.prioritas = prioritas
        
    def tampilkan_info(self):
        if self.prioritas == "darurat":
            print("daruratt")
    
        

#soal 4
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class AntrianPasien:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def TambahDiawal(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.next = self.head
        self.head = newNode
        
    def tambahDiakhir(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            return
        
        self.tail.next = newNode
        self.tail = newNode
        
    def tampilkan(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
    def panggil_berikutnya(self):
        if not self.head:
            print("antrian kosong")
        print("paling depan:", self.head.data)
        
        self.head = self.head.next
    
    def cari_nama(self, data):
        if not self.head:
            print("antrian kosong")
            return

        if self.head.data == data:
            print("posisi 1")
            return
        
        current = self.head
        n = 0
        while current.next and current.next.data != data:
            current = current.next
            n += 1
            
        if not current.next:
            print(f"nama {data} tidak ditemukan")
            return

        if current.next == self.tail:
            print(data, "berada di akhir, posisi:", n)
            return
        
        print("posisi", data, ":", n)
        
    def hapus_berdasarkan_id(self, id):
        if id == self.head.data["id"]:
            self.head = self.head.next
        
        

antrian = AntrianPasien()
antrian.tambahDiakhir({"id": "P001", "nama": "Andi", "penyakit":
"Flu"})
antrian.tambahDiakhir({"id": "P002", "nama": "Budi", "penyakit":
"Tifus"})
antrian.tambahDiakhir({"id": "P003", "nama": "Cici", "penyakit":
"Flu"})
antrian.tambahDiakhir({"id": "P004", "nama": "Dani", "penyakit":
"Maag"})
antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
# antrian.hapus_berdasarkan_id("P003")
antrian.tampilkan()