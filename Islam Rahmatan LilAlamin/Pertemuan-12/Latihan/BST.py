class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        self.now = None
    def insert(self, data):
        new = Node(data)
        if not self.root:
            self.root = new
            return
        
        p = self.root
        q = self.root
        
        while q != None and new.data != p.data:
            p = q
            
            if new.data < p.data:
                q = p.left
                
            else:
                q = p.right
                
        if new.data == p.data:
            print(f"data {p.data} sudah ada oi")
            return
        
        if new.data < p.data:
            p.left = new
            
        else:
            p.right = new
            
            
class BinaryTree2:
    """Implementasi Binary Tree"""
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)

    def insert_left(self, parent_node, data):
        """Memasukkan child kiri dari suatu node"""
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        """Memasukkan child kanan dari suatu node"""
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node
            
    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)

        
            
if __name__ == "__main__":  
    
    tree = BinaryTree2()

    tree.insert_root("F")
    tree.insert_left(tree.root, "B")
    tree.insert_right(tree.root, "G")
    tree.insert_left(tree.root.left, "A")
    tree.insert_right(tree.root.left, "D")
    tree.insert_left(tree.root.left.right, "C")
    tree.insert_right(tree.root.left.right, "E")
    tree.insert_right(tree.root.right, "I")
    tree.insert_left(tree.root.right.right, "C")
    
    tree.in_order(tree.root)    