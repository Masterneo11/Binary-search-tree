
class Node:
    
    def __init__(self, value):
    
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    
    def __init__(self):
        
        self.root = None

                                                
    def insert(self, node_number :int) -> None:
            
        if self.root is None:
            self.root = Node(node_number)               # basically if theres nothing it assignes the root the node number
            return
        
        current_node = self.root
        while current_node != None:
            
            if current_node.value < node_number:
                if current_node.right is None:
                    
                    current_node.right = Node(node_number)
                    return 
                    
                else:
                    current_node = current_node.right
                    
            elif current_node.value > node_number:
                    if current_node.left is None:
                        current_node.left = Node(node_number)
                        return 
                    else:
                        current_node = current_node.left
            else:
                return 
        
        
        
    def search(self, node_number: int) -> bool:
            
        
        current_node = self.root
        while current_node != None:
            
            if node_number == current_node.value:
                return True
            
            elif current_node.value < node_number:
                current_node = current_node.right
            else:
                current_node = current_node.left
                
        
        return False 
    
    def find_min(self) -> int:
        current_node = self.root
        while current_node != None:
            if current_node.left is None:
                return current_node.value
            else:
                current_node = current_node.left
        
    def find_max(self) -> int:
        current_node = self.root
        while current_node != None:
            if current_node.right is None:
                return current_node.value
            else:
                current_node = current_node.right
                
    def serialize(self) -> str:
        
        a = []
        self.traverse(self.root, a)
        for i in range(len(a)):
            a[i] = str(a[i])
        b = ''.join(a)
        return b
    
    def deserialize(self, tree: str) -> None:
        
        a = []
        for i in tree:
            a.append(int(i))
        self.root = None
        for i in a:
            self.insert(i)
                
    def traverse(self, root, a:list):
        
        if root:
            self.traverse(root.left, a)
            a.append(root.value)  
            self.traverse(root.right, a)

    def in_order_traversal(self) -> list[int]:
        
        a = []
        self.traverse(self.root, a)
        return a
    
    def recusive_height(self, root):
        
        if root == None:
            return 0
        left_height = self.recusive_height(root.left)
        right_height = self.recusive_height(root.right)
        return max(left_height, right_height) + 1
    
    def height(self) -> int:
        return self.recusive_height(self.root)
    
    
    def helper_count(self, root):
        
        if root == None:
            return 0
        if(root.left == None and root.right == None):
            return 1
        else:
            return self.helper_count(root.left) + self.helper_count(root.right)
        
    def count_leaves(self):
        
        return self.helper_count(self.root)
    
        
        
    
def main():
    bst = BinarySearchTree()
    num = [9, 8, 7, 6, 5, 4, 3, 2, 12]
    for i in num:
        bst.insert(i)
    #print(bst.in_order_traversal())
    print(bst.count_leaves()) 
    print(bst.height())
    print(bst.find_max())
    print(bst.find_min())
    print(bst.in_order_traversal())
    print(bst.serialize())
    tree = "123654"
    print(bst.deserialize(tree))
    print(bst.count_leaves())    


if __name__ == "__main__":
     main()
        
        
        
