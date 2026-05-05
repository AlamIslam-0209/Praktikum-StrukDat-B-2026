## Metode List

antrian = ['A', 'B', 'C']

def sisipkan_pasien(nama_pasien, posisi):
    antrian.insert(posisi - 1, nama_pasien)

sisipkan_pasien("D", 2)
sisipkan_pasien("E", 3)
sisipkan_pasien("F", 4)
sisipkan_pasien("x", 1)
print(antrian)


## Metode LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class AntrianLinkedList:
    def __init__(self):
        self.head = None
        
    def sisipkanPasien(self, nama_pasien, posisi):
        newNode = Node(nama_pasien)
        
        if posisi <= 1 or self.head is None:
            newNode.next = self.head
            self.head = newNode
            return 

        currentNode = self.head
        
        for _ in range(posisi - 2):
            if currentNode.next is None:
                break
            currentNode = currentNode.next

        newNode.next = currentNode.next
        currentNode.next = newNode
    
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    
Antrian = AntrianLinkedList()

Antrian.sisipkanPasien("A", 1) 
Antrian.sisipkanPasien("B", 2) 
Antrian.sisipkanPasien("C", 3) 

Antrian.sisipkanPasien("D", 2)
Antrian.sisipkanPasien("E", 3)
Antrian.sisipkanPasien("F", 4)
Antrian.sisipkanPasien("X", 1)

Antrian.print_list()