"""
Tests for Binary Tree implementation
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from binary_tree import BinaryTree, TreeNode


def test_insert():
    tree = BinaryTree()
    tree.insert(1)
    assert tree.root.value == 1
    
    tree.insert(2)
    assert tree.root.left.value == 2
    
    tree.insert(3)
    assert tree.root.right.value == 3


def test_traversals():
    tree = BinaryTree()
    values = [1, 2, 3, 4, 5, 6, 7]
    for val in values:
        tree.insert(val)
    
    # Test level order
    assert tree.level_order_traversal() == [1, 2, 3, 4, 5, 6, 7]
    
    # Test inorder
    inorder = tree.inorder_traversal()
    assert len(inorder) == 7
    
    # Test preorder
    preorder = tree.preorder_traversal()
    assert preorder[0] == 1  # Root should be first
    
    # Test postorder
    postorder = tree.postorder_traversal()
    assert postorder[-1] == 1  # Root should be last


def test_height():
    tree = BinaryTree()
    assert tree.height() == 0
    
    tree.insert(1)
    assert tree.height() == 1
    
    tree.insert(2)
    tree.insert(3)
    assert tree.height() == 2
    
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    assert tree.height() == 3


def test_size():
    tree = BinaryTree()
    assert tree.size() == 0
    
    tree.insert(1)
    assert tree.size() == 1
    
    tree.insert(2)
    tree.insert(3)
    assert tree.size() == 3
    
    tree.insert(4)
    tree.insert(5)
    assert tree.size() == 5


def test_empty_tree():
    tree = BinaryTree()
    assert tree.inorder_traversal() == []
    assert tree.preorder_traversal() == []
    assert tree.postorder_traversal() == []
    assert tree.level_order_traversal() == []
    assert tree.height() == 0
    assert tree.size() == 0


if __name__ == "__main__":
    test_insert()
    test_traversals()
    test_height()
    test_size()
    test_empty_tree()
    print("All tests passed!")
