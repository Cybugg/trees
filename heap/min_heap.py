"""
Min Heap Implementation

A Min Heap is a complete binary tree where each parent node is smaller than or
equal to its children. The minimum element is always at the root.
"""

class MinHeap:
    """Min Heap implementation using an array."""
    
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        """Get parent index."""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Get left child index."""
        return 2 * i + 1
    
    def right_child(self, i):
        """Get right child index."""
        return 2 * i + 2
    
    def swap(self, i, j):
        """Swap two elements in the heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, value):
        """Insert a value into the min heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        """Move element up to maintain heap property."""
        parent = self.parent(i)
        
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)
    
    def extract_min(self):
        """Remove and return the minimum element."""
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return min_val
    
    def _heapify_down(self, i):
        """Move element down to maintain heap property."""
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        
        if min_index != i:
            self.swap(i, min_index)
            self._heapify_down(min_index)
    
    def peek(self):
        """Return the minimum element without removing it."""
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def size(self):
        """Return the number of elements in the heap."""
        return len(self.heap)
    
    def is_empty(self):
        """Check if the heap is empty."""
        return len(self.heap) == 0
    
    def heapify(self, arr):
        """Build a heap from an array."""
        self.heap = arr[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)


# Example usage
if __name__ == "__main__":
    min_heap = MinHeap()
    
    # Insert values
    values = [5, 3, 7, 1, 9, 4, 6]
    print("Inserting values:", values)
    for val in values:
        min_heap.insert(val)
    
    print(f"\nMin Heap Operations:")
    print(f"Heap array: {min_heap.heap}")
    print(f"Peek (min): {min_heap.peek()}")
    print(f"Size: {min_heap.size()}")
    
    # Extract all elements (should be in sorted order)
    print("\nExtracting all elements:")
    extracted = []
    while not min_heap.is_empty():
        extracted.append(min_heap.extract_min())
    print(f"Extracted (sorted): {extracted}")
    
    # Build heap from array
    print("\nBuilding heap from array [9, 5, 6, 2, 3]:")
    min_heap.heapify([9, 5, 6, 2, 3])
    print(f"Heap array: {min_heap.heap}")
    print(f"Min element: {min_heap.peek()}")
