"""
Tests for AVL Tree implementation
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from avl_tree import AVLTree


def test_insert():
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]
    
    for val in values:
        avl.insert(val)
    
    # Check if all values are inserted
    for val in values:
        assert avl.search(val) == True


def test_balance():
    avl = AVLTree()
    # This sequence would create unbalanced BST
    values = [1, 2, 3, 4, 5, 6, 7]
    
    for val in values:
        avl.insert(val)
    
    # AVL tree should remain balanced
    assert avl.is_balanced() == True


def test_inorder_traversal():
    avl = AVLTree()
    values = [30, 20, 40, 10, 25, 35, 50]
    
    for val in values:
        avl.insert(val)
    
    # Inorder traversal should be sorted
    assert avl.inorder_traversal() == [10, 20, 25, 30, 35, 40, 50]


def test_delete():
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]
    
    for val in values:
        avl.insert(val)
    
    # Delete and check balance
    avl.delete(40)
    assert avl.search(40) == False
    assert avl.is_balanced() == True
    
    avl.delete(10)
    assert avl.search(10) == False
    assert avl.is_balanced() == True


def test_search():
    avl = AVLTree()
    values = [30, 20, 40, 10, 25]
    
    for val in values:
        avl.insert(val)
    
    assert avl.search(30) == True
    assert avl.search(20) == True
    assert avl.search(100) == False
    assert avl.search(0) == False


def test_empty_tree():
    avl = AVLTree()
    assert avl.inorder_traversal() == []
    assert avl.search(10) == False
    assert avl.is_balanced() == True


def test_duplicate_values():
    avl = AVLTree()
    avl.insert(10)
    avl.insert(10)  # Should not insert duplicate
    
    assert avl.inorder_traversal() == [10]


if __name__ == "__main__":
    test_insert()
    test_balance()
    test_inorder_traversal()
    test_delete()
    test_search()
    test_empty_tree()
    test_duplicate_values()
    print("All AVL Tree tests passed!")
