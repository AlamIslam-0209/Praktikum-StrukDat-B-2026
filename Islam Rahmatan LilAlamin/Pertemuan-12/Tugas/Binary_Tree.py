class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
class Binary_Tree:
    def __init__(self):
        self.root = None
        
    def Insert_manual(self):
        self.root = Node("A")
        self.root.left = Node("B")
        self.root.right = Node("C")
        self.root.left.left = Node("D")
        self.root.left.right = Node("E")
        self.root.right.right = Node("F")
        
    def Traverse_Preorder(self, node):
        if node is None:
            return []

        return [node.data] + self.Traverse_Preorder(node.left) + self.Traverse_Preorder(node.right)
        
    def Traverse_Inorder(self, node):
        if node is None:
            return []

        return self.Traverse_Inorder(node.left) + [node.data] + self.Traverse_Inorder(node.right)
        
    def Traverse_Postorder(self, node):
        if node is None:
            return []

        return self.Traverse_Postorder(node.left) + self.Traverse_Postorder(node.right) + [node.data]
        
    def Get_Leaf_Nodes(self, node):
        if node is None:
            return []
        
        if node.left is None and node.right is None:
            return [node.data]
        
        return self.Get_Leaf_Nodes(node.left) + self.Get_Leaf_Nodes(node.right)
            
            
if __name__ == "__main__":
    tree = Binary_Tree()
    
    tree.Insert_manual()
    
    print("1. Preorder:", " -> ".join(tree.Traverse_Preorder(tree.root)))
    print("2. Inorder:", " -> ".join(tree.Traverse_Inorder(tree.root)))
    print("3. Postorder:", " -> ".join(tree.Traverse_Postorder(tree.root)))
    
    print("Leaf Nodes:", ", ".join(tree.Get_Leaf_Nodes(tree.root)))