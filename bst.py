
class Node:
    
    def __init__(self, value):
    
        self.left = None
        self.right = None
        self.value = value


class BST:
    
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
        traversal_result = []
        self.original_tree_state(self.root, traversal_result)
        val = []
        for i in traversal_result:
            val.append(str(i))
        tree_str = ','.join(val)
        return tree_str

    def original_tree_state(self, root, traversal_result:list):
        if root:
            traversal_result.append(root.value)
            self.original_tree_state(root.left, traversal_result)
#             traversal_result.append(root.value)
            self.original_tree_state(root.right, traversal_result)
    
    def deserialize(self, tree: str) -> None:
        a = []
        c = tree.split(",")
        for i in c:
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
    bst = BST()
    num = [32000, 9 , 88, 550, 7 , 10, 11, 15, 20]
    for i in num:
        bst.insert(i)
        
    print(bst.serialize())
    tree = "32000,9,7,88,10,11,15,20,550"
    print(bst.deserialize(tree))
    print("h")
    print(bst.in_order_traversal())
    print("hi")
    print(bst.count_leaves())
    
    print(bst.height())
    print(bst.find_max())
    print(bst.find_min())
    print(bst.in_order_traversal())
    print(f"{bst.serialize()} serialize")
    tree = "3, 4, 5"
    print(bst.deserialize(tree))
    tree = "123654"
    print(bst.deserialize(tree))
    print(bst.count_leaves())    


if __name__ == "__main__":
     main()
        
        
        
