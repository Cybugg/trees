"""
Tests for Red-Black Tree implementation
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from red_black_tree import RedBlackTree, Color


def test_insert_and_search():
    rbt = RedBlackTree()
    values = [10, 20, 30, 15, 25, 5, 1]
    
    for val in values:
        rbt.insert(val)
    
    for val in values:
        assert rbt.search(val) == True
    
    assert rbt.search(100) == False


def test_inorder_traversal():
    rbt = RedBlackTree()
    values = [10, 20, 30, 15, 25, 5, 1]
    
    for val in values:
        rbt.insert(val)
    
    # Inorder traversal should be sorted
    assert rbt.inorder_traversal() == sorted(values)


def test_root_is_black():
    rbt = RedBlackTree()
    rbt.insert(10)
    
    assert rbt.root.color == Color.BLACK


def test_is_valid_red_black_tree():
    rbt = RedBlackTree()
    values = [10, 20, 30, 15, 25, 5, 1, 40, 50]
    
    for val in values:
        rbt.insert(val)
    
    assert rbt.is_valid_red_black_tree() == True


def test_sequential_insertion():
    rbt = RedBlackTree()
    # Insert in order - this would make BST unbalanced
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for val in values:
        rbt.insert(val)
    
    # Should maintain Red-Black Tree properties
    assert rbt.is_valid_red_black_tree() == True
    assert rbt.inorder_traversal() == values


def test_empty_tree():
    rbt = RedBlackTree()
    
    assert rbt.search(10) == False
    assert rbt.inorder_traversal() == []
    assert rbt.is_valid_red_black_tree() == True


if __name__ == "__main__":
    test_insert_and_search()
    test_inorder_traversal()
    test_root_is_black()
    test_is_valid_red_black_tree()
    test_sequential_insertion()
    test_empty_tree()
    print("All Red-Black Tree tests passed!")
