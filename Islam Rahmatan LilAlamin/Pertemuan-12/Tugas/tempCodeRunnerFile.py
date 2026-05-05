if node is None:
            return []
        
        if node.left is None and node.right is None:
            return [node.data]
        
        return self.Get_Leaf_Nodes(node.left) + self.Get_Leaf_Nodes(node.right)