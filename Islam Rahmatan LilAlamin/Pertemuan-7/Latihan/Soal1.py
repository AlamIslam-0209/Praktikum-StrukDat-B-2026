## 1. Metode List

history_array = ["google.com", "python.org"]

search = str("random")

def tambah_pencarian_array(Keyword):
    history_array.insert(0, Keyword)
    
while search :
    search = input("search: ")
    
    if search == "/":
        print("keluar dari loop")
        break
    
    tambah_pencarian_array(search)
    print("Browsing", search, "...")
    print("Berhasil menemukan", search, "\n")
    
print(history_array)


## 2. Metode Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HistoryLinkedList:
    def __init__(self):
        self.head = None
        
    def tambah(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 
    
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    
# Inisialisas Riwayat
riwayat = HistoryLinkedList()

print("Menambahkan riwayat awal...")
riwayat.tambah("python.org")
riwayat.tambah("google.com")

while True:
    search = input("search (ketik '/' untuk keluar): ")
    
    if search == "/":
        print("Keluar dari loop...")
        break
        
    riwayat.tambah(search)

# Cetak semua node
print("\nSemua riwayat pencarian (dari yang terbaru):")
riwayat.print_list()

