class Kucing:
    def __init__(self,jenis, nama, umur, kecepatan = 10):
        self.kecepatan = kecepatan
        self.jenis = jenis
        self.__nama = nama
        self.umur = umur
        
    def mengeong(self):
        print("Meongg meonggg")
        
    def jalan(self):
        print(f"kucing berjalan dengan kecepatan {self.kecepatan}m/s")
        
    def ubahNama(self, namaBaru):
        self.__nama = namaBaru
        
    def getNama(self):
        return self.__nama
    
K1 = Kucing("Oren", "Akil", 10)
K2 = Kucing("persia", "ilyas", 5, 20)
K3 = Kucing("kampung", "eng", 1)

K1.__nama = "alam"
print(K1.__nama)
print(K1.getNama())
K1.mengeong()
K2.jalan()

print(K3.getNama())
K2.ubahNama("dihar")
print(K2.getNama())

        