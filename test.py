from bst import BST
import pytest

@pytest.fixture
def create_a_bst():
    a = BST()
    b = [7, 9, 550, 32000, 88]
    for i in b:
        a.insert(i)
        print(a)
    return a
        
def test_serialize(create_a_bst):
    expected = "7,9,550,88,32000"
    assert create_a_bst.serialize() == expected
    
def test_deserialize():
    tree = "9,55,11,4"
    a = BST()
    a.deserialize(tree)
    assert a.root.value == 9
    assert a.root.right.value == 55
    assert a.root.right.left.value == 11
    assert a.root.left.value == 4


def test_search(create_a_bst):
    
   expected = 7
   assert create_a_bst.search(7) == True
    

def test_find_min(create_a_bst):
    
    expected = 7
    assert create_a_bst.find_min() == expected
    
def test_find_max(create_a_bst):
    
    expected = 32000
    assert create_a_bst.find_max() == expected

def test_in_order_traversal(create_a_bst):
    
    expected = [7, 9 , 88, 550, 32000]
    assert create_a_bst.in_order_traversal() == expected

def test_insert(create_a_bst):
    
    expected = None
    assert create_a_bst.insert(21) == expected

def test_height(create_a_bst):
    
    expected = 4
    assert create_a_bst.height() == expected
    

def test_count_leaves(create_a_bst):
    
    expected = 2
    assert create_a_bst.count_leaves() == expected
    
    







    