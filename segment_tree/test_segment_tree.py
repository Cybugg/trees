"""
Tests for Segment Tree implementation
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from segment_tree import SegmentTree, SegmentTreeMin


def test_segment_tree_sum_query():
    arr = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(arr)
    
    assert seg_tree.query(1, 3) == 15  # 3 + 5 + 7
    assert seg_tree.query(0, 5) == 36  # 1 + 3 + 5 + 7 + 9 + 11
    assert seg_tree.query(2, 4) == 21  # 5 + 7 + 9


def test_segment_tree_sum_update():
    arr = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(arr)
    
    seg_tree.update(2, 6)
    assert seg_tree.query(1, 3) == 16  # 3 + 6 + 7
    assert seg_tree.query(2, 2) == 6


def test_segment_tree_min_query():
    arr = [4, 2, 6, 1, 8, 5]
    seg_tree_min = SegmentTreeMin(arr)
    
    assert seg_tree_min.query(0, 2) == 2  # min(4, 2, 6)
    assert seg_tree_min.query(2, 5) == 1  # min(6, 1, 8, 5)
    assert seg_tree_min.query(0, 5) == 1  # min of all


def test_segment_tree_min_update():
    arr = [4, 2, 6, 1, 8, 5]
    seg_tree_min = SegmentTreeMin(arr)
    
    seg_tree_min.update(3, 9)
    assert seg_tree_min.query(2, 5) == 5  # min(6, 9, 8, 5)
    assert seg_tree_min.query(0, 5) == 2  # min of all


def test_single_element():
    arr = [5]
    seg_tree = SegmentTree(arr)
    
    assert seg_tree.query(0, 0) == 5
    
    seg_tree.update(0, 10)
    assert seg_tree.query(0, 0) == 10


def test_empty_array():
    arr = []
    seg_tree = SegmentTree(arr)
    
    assert seg_tree.query(0, 0) == 0


if __name__ == "__main__":
    test_segment_tree_sum_query()
    test_segment_tree_sum_update()
    test_segment_tree_min_query()
    test_segment_tree_min_update()
    test_single_element()
    test_empty_array()
    print("All Segment Tree tests passed!")
