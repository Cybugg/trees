"""
Tests for Heap implementations (Min Heap and Max Heap)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from min_heap import MinHeap
from max_heap import MaxHeap


# Min Heap Tests
def test_min_heap_insert():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    
    assert heap.peek() == 3


def test_min_heap_extract():
    heap = MinHeap()
    values = [5, 3, 7, 1, 9, 4, 6]
    
    for val in values:
        heap.insert(val)
    
    # Extract should give elements in sorted order
    extracted = []
    while not heap.is_empty():
        extracted.append(heap.extract_min())
    
    assert extracted == [1, 3, 4, 5, 6, 7, 9]


def test_min_heap_heapify():
    heap = MinHeap()
    heap.heapify([9, 5, 6, 2, 3])
    
    assert heap.peek() == 2


def test_min_heap_size():
    heap = MinHeap()
    assert heap.size() == 0
    
    heap.insert(1)
    assert heap.size() == 1
    
    heap.insert(2)
    heap.insert(3)
    assert heap.size() == 3
    
    heap.extract_min()
    assert heap.size() == 2


# Max Heap Tests
def test_max_heap_insert():
    heap = MaxHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    
    assert heap.peek() == 7


def test_max_heap_extract():
    heap = MaxHeap()
    values = [5, 3, 7, 1, 9, 4, 6]
    
    for val in values:
        heap.insert(val)
    
    # Extract should give elements in reverse sorted order
    extracted = []
    while not heap.is_empty():
        extracted.append(heap.extract_max())
    
    assert extracted == [9, 7, 6, 5, 4, 3, 1]


def test_max_heap_heapify():
    heap = MaxHeap()
    heap.heapify([9, 5, 6, 2, 3])
    
    assert heap.peek() == 9


def test_max_heap_size():
    heap = MaxHeap()
    assert heap.size() == 0
    
    heap.insert(1)
    assert heap.size() == 1
    
    heap.insert(2)
    heap.insert(3)
    assert heap.size() == 3
    
    heap.extract_max()
    assert heap.size() == 2


def test_empty_heaps():
    min_heap = MinHeap()
    max_heap = MaxHeap()
    
    assert min_heap.peek() is None
    assert max_heap.peek() is None
    assert min_heap.extract_min() is None
    assert max_heap.extract_max() is None
    assert min_heap.is_empty() == True
    assert max_heap.is_empty() == True


if __name__ == "__main__":
    test_min_heap_insert()
    test_min_heap_extract()
    test_min_heap_heapify()
    test_min_heap_size()
    test_max_heap_insert()
    test_max_heap_extract()
    test_max_heap_heapify()
    test_max_heap_size()
    test_empty_heaps()
    print("All Heap tests passed!")
