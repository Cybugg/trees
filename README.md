# Trees Data Structure Examples

A comprehensive repository containing implementations and examples of various tree data structures.

## Overview

This repository provides clear, well-documented implementations of common tree data structures used in computer science and software engineering.

## Tree Data Structures Included

### 1. Binary Tree
A tree data structure where each node has at most two children (left and right).

### 2. Binary Search Tree (BST)
A binary tree where the left subtree contains values less than the node, and the right subtree contains values greater than the node.

### 3. AVL Tree
A self-balancing binary search tree where the heights of two child subtrees differ by at most one.

### 4. Red-Black Tree
A self-balancing binary search tree with an extra bit per node for color (red or black).

### 5. Heap (Min-Heap & Max-Heap)
A complete binary tree where parent nodes are either greater (max-heap) or smaller (min-heap) than their children.

### 6. Trie (Prefix Tree)
A tree used for storing strings where each path represents a string prefix.

### 7. B-Tree
A self-balancing tree data structure that maintains sorted data and allows searches, insertions, and deletions in logarithmic time.

### 8. Segment Tree
A tree used for storing intervals or segments, allowing efficient range queries.

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

Each tree implementation includes:
- Core data structure implementation
- Common operations (insert, delete, search, traverse)
- Example usage
- Unit tests

To run tests for any implementation:
```bash
python -m pytest <tree_type>/test_*.py
```

## Contributing

Feel free to contribute by:
- Adding new tree implementations
- Improving existing implementations
- Adding more test cases
- Improving documentation

## License

MIT License - See LICENSE file for details