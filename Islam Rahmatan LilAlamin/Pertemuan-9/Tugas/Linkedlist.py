# ==========================================
# BAGIAN A: DOUBLE LINKED LIST (Toko Buku)
# ==========================================

class NodeBuku:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_tail(self, judul, pengarang):
        node_baru = NodeBuku(judul, pengarang)
        if not self.head:
            self.head = node_baru
            self.tail = node_baru
            return
        
        self.tail.next = node_baru
        node_baru.prev = self.tail  
        self.tail = node_baru
        
    def delete_by_judul(self, judul):
        if not self.head:
            print("List kosong")
            return
        
        if self.head.judul == judul:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
                
        current = self.head
        while current and current.judul != judul:
            current = current.next
            
        if not current:
            print(f"Buku '{judul}' tidak ditemukan")
            return
        
        if current == self.tail:
            self.tail = current.prev
            self.tail.next = None
            return
        
        current.prev.next = current.next
        current.next.prev = current.prev

    def print_forward(self):
        current = self.head
        print("Maju: ", end="")
        while current:
            print(f"[{current.judul} - {current.pengarang}]", end=" <-> ")
            current = current.next
        print("None")

    def print_backward(self):
        current = self.tail
        print("Mundur: ", end="")
        while current:
            print(f"[{current.judul} - {current.pengarang}]", end=" <-> ")
            current = current.prev
        print("None")


# ==========================================
# BAGIAN B: CIRCULAR LINKED LIST (Antrian)
# ==========================================

class NodeAntrian:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_tail(self, nama):
        node_baru = NodeAntrian(nama)
        if not self.head:
            self.head = node_baru
            self.tail = node_baru
            self.tail.next = self.head
            return
            
        self.tail.next = node_baru
        self.tail = node_baru
        self.tail.next = self.head
        
    def delete_head(self):
        if not self.head:
            print("Antrian kosong")
            return

        print(f"Melayani dan menghapus: {self.head.nama}")
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
            
        self.head = self.head.next
        self.tail.next = self.head
        
    def print_antrian(self):
        if not self.head:
            print("Antrian kosong")
            return
            
        current = self.head
        print("Antrian: ", end="")
        while True:
            print(current.nama, end=" -> ")
            current = current.next
            if current == self.head: 
                break
        print(f"(kembali ke {self.head.nama})")


if __name__ == "__main__":
    print("--- BAGIAN A ---")
    dll = DoublyLinkedList()
    dll.insert_tail("Laskar Pelangi", "Andrea Hirata")
    dll.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
    dll.insert_tail("Sang Pemimpi", "Andrea Hirata")

    dll.print_forward()
    dll.print_backward()

    print("\nMenghapus 'Bumi Manusia'...")
    dll.delete_by_judul("Bumi Manusia")
    dll.print_forward()

    print("\n\n--- BAGIAN B ---")
    cll = CircularLinkedList()
    cll.insert_tail("Andi")
    cll.insert_tail("Budi")
    cll.insert_tail("Citra")
    cll.insert_tail("Dina")

    cll.print_antrian()

    print("\nMenambahkan Edo...")
    cll.insert_tail("Edo")
    cll.print_antrian()

    print("\nMenghapus pelanggan di depan (Head)...")
    cll.delete_head()
    cll.print_antrian()