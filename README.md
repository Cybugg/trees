# Trees Data Structure Examples

A comprehensive repository containing implementations and examples of various tree data structures.

## Overview

This repository provides clear, well-documented implementations of common tree data structures used in computer science and software engineering. Each implementation includes:
- Core data structure with all operations
- Comprehensive test suite
- Example usage demonstrations
- Clear documentation

## Tree Data Structures Included

### 1. Binary Tree
A tree data structure where each node has at most two children (left and right).

**Operations:**
- Insert (level-order)
- Traversals (inorder, preorder, postorder, level-order)
- Height and size calculations

### 2. Binary Search Tree (BST)
A binary tree where the left subtree contains values less than the node, and the right subtree contains values greater than the node.

**Operations:**
- Insert, search, delete
- Find min/max
- Inorder traversal (returns sorted values)
- BST validation

### 3. AVL Tree
A self-balancing binary search tree where the heights of two child subtrees differ by at most one.

**Operations:**
- Balanced insert and delete
- Automatic rotations
- Balance checking
- All BST operations

### 4. Red-Black Tree
A self-balancing binary search tree with an extra bit per node for color (red or black).

**Operations:**
- Balanced insert with color fixing
- Search and traversal
- Red-Black tree property validation

### 5. Heap (Min-Heap & Max-Heap)
A complete binary tree where parent nodes are either greater (max-heap) or smaller (min-heap) than their children.

**Operations:**
- Insert
- Extract min/max
- Peek
- Heapify from array

### 6. Trie (Prefix Tree)
A tree used for storing strings where each path represents a string prefix.

**Operations:**
- Insert, search, delete words
- Prefix checking
- Autocomplete suggestions
- Get all words

### 7. B-Tree
A self-balancing tree data structure that maintains sorted data and allows searches, insertions, and deletions in logarithmic time.

**Operations:**
- Insert with automatic splitting
- Search
- Get all keys in sorted order

### 8. Segment Tree
A tree used for storing intervals or segments, allowing efficient range queries.

**Operations:**
- Range sum queries
- Range minimum queries
- Point updates

## Repository Structure

```
trees/
├── binary_tree/
│   ├── binary_tree.py
│   └── test_binary_tree.py
├── binary_search_tree/
│   ├── bst.py
│   └── test_bst.py
├── avl_tree/
│   ├── avl_tree.py
│   └── test_avl_tree.py
├── red_black_tree/
│   ├── red_black_tree.py
│   └── test_red_black_tree.py
├── heap/
│   ├── min_heap.py
│   ├── max_heap.py
│   └── test_heap.py
├── trie/
│   ├── trie.py
│   └── test_trie.py
├── b_tree/
│   ├── b_tree.py
│   └── test_b_tree.py
└── segment_tree/
    ├── segment_tree.py
    └── test_segment_tree.py
```

## Usage

### Quick Start

Each implementation can be run independently. For example:

```python
# Binary Search Tree
from binary_search_tree.bst import BinarySearchTree

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)

print(bst.search(30))  # True
print(bst.inorder_traversal())  # [30, 50, 70]
```

```python
# Min Heap
from heap.min_heap import MinHeap

heap = MinHeap()
heap.insert(5)
heap.insert(3)
heap.insert(7)

print(heap.peek())  # 3
print(heap.extract_min())  # 3
```

```python
# Trie (Autocomplete)
from trie.trie import Trie

trie = Trie()
trie.insert("apple")
trie.insert("application")
trie.insert("apply")

print(trie.autocomplete("app"))  # ['apple', 'application', 'apply']
```

### Running Examples

To run the example code in any implementation:

```bash
python binary_tree/binary_tree.py
python binary_search_tree/bst.py
python avl_tree/avl_tree.py
# ... etc
```

### Running Tests

To run tests for any implementation:

```bash
python binary_tree/test_binary_tree.py
python binary_search_tree/test_bst.py
python avl_tree/test_avl_tree.py
# ... etc
```

Or run all tests:

```bash
for dir in binary_tree binary_search_tree avl_tree red_black_tree heap trie b_tree segment_tree; do
    python $dir/test_*.py
done
```

## Implementation Details

### Time Complexities

| Data Structure | Insert | Delete | Search | Space |
|---------------|--------|--------|--------|-------|
| Binary Tree | O(n) | O(n) | O(n) | O(n) |
| BST | O(h)* | O(h)* | O(h)* | O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(n) |
| Red-Black Tree | O(log n) | O(log n) | O(log n) | O(n) |
| Min/Max Heap | O(log n) | O(log n) | O(n) | O(n) |
| Trie | O(m) | O(m) | O(m) | O(ALPHABET_SIZE * N * M) |
| B-Tree | O(log n) | O(log n) | O(log n) | O(n) |
| Segment Tree | O(log n) | - | O(log n) | O(n) |

*h = height of tree (can be O(n) worst case for unbalanced BST)  
*m = length of word (for Trie)

## Contributing

Feel free to contribute by:
- Adding new tree implementations
- Improving existing implementations
- Adding more test cases
- Improving documentation
- Fixing bugs

## License

MIT License - See LICENSE file for details