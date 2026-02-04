"""
Max Heap Implementation

A Max Heap is a complete binary tree where each parent node is greater than or
equal to its children. The maximum element is always at the root.
"""

class MaxHeap:
    """Max Heap implementation using an array."""
    
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
        """Insert a value into the max heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        """Move element up to maintain heap property."""
        parent = self.parent(i)
        
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)
    
    def extract_max(self):
        """Remove and return the maximum element."""
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return max_val
    
    def _heapify_down(self, i):
        """Move element down to maintain heap property."""
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
        
        if max_index != i:
            self.swap(i, max_index)
            self._heapify_down(max_index)
    
    def peek(self):
        """Return the maximum element without removing it."""
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
    max_heap = MaxHeap()
    
    # Insert values
    values = [5, 3, 7, 1, 9, 4, 6]
    print("Inserting values:", values)
    for val in values:
        max_heap.insert(val)
    
    print(f"\nMax Heap Operations:")
    print(f"Heap array: {max_heap.heap}")
    print(f"Peek (max): {max_heap.peek()}")
    print(f"Size: {max_heap.size()}")
    
    # Extract all elements (should be in reverse sorted order)
    print("\nExtracting all elements:")
    extracted = []
    while not max_heap.is_empty():
        extracted.append(max_heap.extract_max())
    print(f"Extracted (reverse sorted): {extracted}")
    
    # Build heap from array
    print("\nBuilding heap from array [9, 5, 6, 2, 3]:")
    max_heap.heapify([9, 5, 6, 2, 3])
    print(f"Heap array: {max_heap.heap}")
    print(f"Max element: {max_heap.peek()}")
