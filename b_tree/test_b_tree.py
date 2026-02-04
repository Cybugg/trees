"""
Tests for B-Tree implementation
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from b_tree import BTree


def test_insert_and_search():
    btree = BTree(degree=3)
    values = [10, 20, 5, 6, 12, 30]
    
    for val in values:
        btree.insert(val)
    
    for val in values:
        assert btree.search(val) == True
    
    assert btree.search(100) == False


def test_get_all_keys():
    btree = BTree(degree=3)
    values = [10, 20, 5, 6, 12, 30, 7, 17]
    
    for val in values:
        btree.insert(val)
    
    all_keys = btree.get_all_keys()
    assert all_keys == sorted(values)


def test_single_node():
    btree = BTree(degree=3)
    btree.insert(10)
    
    assert btree.search(10) == True
    assert btree.get_all_keys() == [10]


def test_splits():
    # With degree=2, max keys = 3
    btree = BTree(degree=2)
    
    # Insert enough to cause splits
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for val in values:
        btree.insert(val)
    
    # All values should be searchable
    for val in values:
        assert btree.search(val) == True
    
    # Keys should be in sorted order
    assert btree.get_all_keys() == sorted(values)


def test_empty_tree():
    btree = BTree(degree=3)
    
    assert btree.search(10) == False
    assert btree.get_all_keys() == []


if __name__ == "__main__":
    test_insert_and_search()
    test_get_all_keys()
    test_single_node()
    test_splits()
    test_empty_tree()
    print("All B-Tree tests passed!")
