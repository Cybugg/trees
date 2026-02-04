"""
Tests for Binary Search Tree implementation
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bst import BinarySearchTree


def test_insert_and_search():
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    for val in values:
        bst.insert(val)
    
    # Test search
    assert bst.search(50) == True
    assert bst.search(30) == True
    assert bst.search(80) == True
    assert bst.search(100) == False
    assert bst.search(0) == False


def test_inorder_traversal():
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    for val in values:
        bst.insert(val)
    
    # Inorder traversal of BST should be sorted
    assert bst.inorder_traversal() == [20, 30, 40, 50, 60, 70, 80]


def test_min_max():
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    for val in values:
        bst.insert(val)
    
    assert bst.find_min() == 20
    assert bst.find_max() == 80


def test_delete():
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    for val in values:
        bst.insert(val)
    
    # Delete leaf node
    bst.delete(20)
    assert bst.search(20) == False
    assert bst.inorder_traversal() == [30, 40, 50, 60, 70, 80]
    
    # Delete node with one child
    bst.delete(30)
    assert bst.search(30) == False
    assert bst.inorder_traversal() == [40, 50, 60, 70, 80]
    
    # Delete node with two children
    bst.delete(70)
    assert bst.search(70) == False
    assert bst.inorder_traversal() == [40, 50, 60, 80]


def test_height():
    bst = BinarySearchTree()
    assert bst.height() == 0
    
    bst.insert(50)
    assert bst.height() == 1
    
    bst.insert(30)
    bst.insert(70)
    assert bst.height() == 2
    
    bst.insert(20)
    assert bst.height() == 3


def test_is_valid_bst():
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    for val in values:
        bst.insert(val)
    
    assert bst.is_valid_bst() == True


def test_empty_tree():
    bst = BinarySearchTree()
    assert bst.search(10) == False
    assert bst.find_min() is None
    assert bst.find_max() is None
    assert bst.inorder_traversal() == []
    assert bst.height() == 0
    assert bst.is_valid_bst() == True


if __name__ == "__main__":
    test_insert_and_search()
    test_inorder_traversal()
    test_min_max()
    test_delete()
    test_height()
    test_is_valid_bst()
    test_empty_tree()
    print("All BST tests passed!")
