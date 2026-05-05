################################################################################
################################### NOMOR 1 ####################################
################################################################################

class tumpukan:
    def __init__(self):
        self.items = []
        
    def push(self, url):
        self.items.append(url)
        print(f"url {url} berhasil dimasukkan")
        
    def pop(self):
        if not self._isempty:
            pop = self.items.pop()
            print(f"berhasil menghapus url {pop}")
            return self.pop
        else:
            print("Pop dari stack kosong (underflow)")
    
    def peek(self):
        if not self._isempty:
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def _isempty(self):
        return len(self.items) == 0
        


################################################################################
################################### NOMOR 2 ####################################
################################################################################

class Blok:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push(self, data):
        newBlok = Blok(data)
        
        newBlok.next = self.top
        self.top = newBlok
        
        print("Berhasil menumpuk", data)
        self.size = self.size + 1
        
    def _isempty(self):
        return self.top == None
        
    def pop(self):
        if self._isempty():
            print("Tumpukan Kosong, tidak ada yang bisa dikeluarkan")
            return None
        
        pop = self.top.data
        self.top = self.top.next
        print("Berhasil mengeluarkan ", pop)
        self.size = self.size - 1
        return pop
    
    def peek(self):
        if self._isempty():
            print("Tumpukan kosong, tidak ada yang bisa diintip")
            return None
        return self.top.data
    
    def search(self, data):
        if not self.top:
            print("Tumpukan Kosong")
            return
        
        urutan = 1
        current = self.top
        while current and current.data != data:
            current = current.next
            urutan += 1
            
        if not current.data:
            print(f"data {data} tidak ditemukan")
            
        print(f"data {data} ditemukan di urutan {urutan}")
        
    def ukuran(self):
        return self.size
    
if __name__ == '__main__':
    tump = tumpukan()
    tump.push("a")
    tump.push("b")
    tump.push("c")
    
    
    
    print(f"tump terbaru: {tump.peek()}\n")
    
    tump.pop()
    tump.size()
    
    
    
    
    
    URL = Stack()
    
    URL.push("e")
    URL.push("f")
    URL.push("g")
    
    URL.search("f")
    
    print(f"url terbaru: {URL.peek()}\n")
    
    URL.pop()
    URL.ukuran()
            
        

        
