from bst import BinarySearchTree
import pytest

@pytest.fixture
def create_a_bst():
    a = BinarySearchTree()
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in b:
        a.insert(i)
    return a
        
def test_serialize(create_a_bst):
    
    expected = "123456789"
    assert create_a_bst.serialize() == expected
    
def test_deserialize():

    expected = "123456789"
    c = BinarySearchTree()
    c.deserialize(expected)
    assert c.in_order_traversal() == [1, 2, 3, 4, 5, 6, 7, 8, 9 ]

def test_search(create_a_bst):
    
   expected = 7
   assert create_a_bst.search(7) == True
    

def test_find_min(create_a_bst):
    
    expected = 1
    assert create_a_bst.find_min() == expected
    
def test_find_max(create_a_bst):
    
    expected = 9
    assert create_a_bst.find_max() == expected

def test_in_order_traversal(create_a_bst):
    
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert create_a_bst.in_order_traversal() == expected

def test_insert(create_a_bst):
    
    expected = None
    assert create_a_bst.insert(11) == expected

def test_height(create_a_bst):
    
    expected = 9
    assert create_a_bst.height() == expected
    

def test_count_leaves(create_a_bst):
    
    expected = 1
    assert create_a_bst.count_leaves() == expected
    
    







    