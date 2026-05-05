class Pasien:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def Banyak(self):
        print("Antrian saat ini sebanyak:", self.size)
        
    def isEmpty(self):
        return self.head is None
        
    def enque(self, nama, keluhan):
        newNode = Pasien(nama, keluhan)
        
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            self.size += 1
            print("menambahkan", nama)
            return
            
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1
        print("menambahkan", nama)
        
    def deque(self):
        if self.isEmpty():
            print("Antrian Kosong")
            return
        
        pop = self.head
        self.head = self.head.next
        
        if not self.head:
            self.tail = None
        self.size -= 1
        print("Melayani:", pop.nama)
    
    def peek(self):
        if self.isEmpty():
            print("Antrian Kosong")
            return None
        print("yang paling depan adalah: ", self.head.nama)
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("antrian dikosongkan")
        
    def display(self):
        if self.isEmpty():
            print("Antrian Kosong")
            return
        print("No |  Nama  |  Keluhan")
        current = self.head
        i = 1
        while current:
            print(f"{i}. {current.nama}: { current.keluhan}")
            i +=1
            current = current.next
        
    
if __name__ == "__main__":
    Antrian = Queue()
    Antrian.display()
    Antrian.enque("Budi", "demam tinggi")
    Antrian.enque("Ani", "Batuk pilek")
    Antrian.enque("Citra", "sakit kepala")
    Antrian.Banyak()
    Antrian.peek()
    Antrian.deque()
    Antrian.enque("Dodi", "Nyeri perut")
    Antrian.display()
    Antrian.deque()
    Antrian.Banyak()
    Antrian.clear()
    Antrian.display()
    
