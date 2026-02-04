"""
Segment Tree Implementation

A Segment Tree is a tree data structure used for storing intervals or segments.
It allows efficient range queries (like sum, min, max) and updates.
"""

class SegmentTree:
    """Segment Tree implementation for range sum queries."""
    
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(arr, 0, 0, self.n - 1)
    
    def _build(self, arr, node, start, end):
        """Build the segment tree."""
        if start == end:
            # Leaf node
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            self._build(arr, left_child, start, mid)
            self._build(arr, right_child, mid + 1, end)
            
            # Internal node stores sum of children
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def update(self, index, value):
        """Update value at index."""
        if 0 <= index < self.n:
            self._update(0, 0, self.n - 1, index, value)
    
    def _update(self, node, start, end, index, value):
        """Helper method for update."""
        if start == end:
            # Leaf node
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            if index <= mid:
                self._update(left_child, start, mid, index, value)
            else:
                self._update(right_child, mid + 1, end, index, value)
            
            # Update internal node
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def query(self, left, right):
        """Query sum in range [left, right]."""
        if 0 <= left <= right < self.n:
            return self._query(0, 0, self.n - 1, left, right)
        return 0
    
    def _query(self, node, start, end, left, right):
        """Helper method for range query."""
        # No overlap
        if right < start or left > end:
            return 0
        
        # Complete overlap
        if left <= start and end <= right:
            return self.tree[node]
        
        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        left_sum = self._query(left_child, start, mid, left, right)
        right_sum = self._query(right_child, mid + 1, end, left, right)
        
        return left_sum + right_sum


class SegmentTreeMin:
    """Segment Tree implementation for range minimum queries."""
    
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (4 * self.n)
        if self.n > 0:
            self._build(arr, 0, 0, self.n - 1)
    
    def _build(self, arr, node, start, end):
        """Build the segment tree."""
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            self._build(arr, left_child, start, mid)
            self._build(arr, right_child, mid + 1, end)
            
            self.tree[node] = min(self.tree[left_child], self.tree[right_child])
    
    def query(self, left, right):
        """Query minimum in range [left, right]."""
        if 0 <= left <= right < self.n:
            return self._query(0, 0, self.n - 1, left, right)
        return float('inf')
    
    def _query(self, node, start, end, left, right):
        """Helper method for range query."""
        if right < start or left > end:
            return float('inf')
        
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        left_min = self._query(left_child, start, mid, left, right)
        right_min = self._query(right_child, mid + 1, end, left, right)
        
        return min(left_min, right_min)
    
    def update(self, index, value):
        """Update value at index."""
        if 0 <= index < self.n:
            self._update(0, 0, self.n - 1, index, value)
    
    def _update(self, node, start, end, index, value):
        """Helper method for update."""
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            if index <= mid:
                self._update(left_child, start, mid, index, value)
            else:
                self._update(right_child, mid + 1, end, index, value)
            
            self.tree[node] = min(self.tree[left_child], self.tree[right_child])


# Example usage
if __name__ == "__main__":
    # Range Sum Segment Tree
    arr = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(arr)
    
    print("Segment Tree (Range Sum) Operations:")
    print(f"Array: {arr}")
    print(f"Sum of range [1, 3]: {seg_tree.query(1, 3)}")  # 3 + 5 + 7 = 15
    print(f"Sum of range [0, 5]: {seg_tree.query(0, 5)}")  # 1 + 3 + 5 + 7 + 9 + 11 = 36
    
    print("\nUpdating index 2 to 6...")
    seg_tree.update(2, 6)
    print(f"Sum of range [1, 3]: {seg_tree.query(1, 3)}")  # 3 + 6 + 7 = 16
    
    # Range Min Segment Tree
    print("\n\nSegment Tree (Range Min) Operations:")
    arr2 = [4, 2, 6, 1, 8, 5]
    seg_tree_min = SegmentTreeMin(arr2)
    
    print(f"Array: {arr2}")
    print(f"Min of range [0, 2]: {seg_tree_min.query(0, 2)}")  # min(4, 2, 6) = 2
    print(f"Min of range [2, 5]: {seg_tree_min.query(2, 5)}")  # min(6, 1, 8, 5) = 1
    
    print("\nUpdating index 3 to 9...")
    seg_tree_min.update(3, 9)
    print(f"Min of range [2, 5]: {seg_tree_min.query(2, 5)}")  # min(6, 9, 8, 5) = 5
