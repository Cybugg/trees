"""
B-Tree Implementation

A B-Tree is a self-balancing tree data structure that maintains sorted data and
allows searches, sequential access, insertions, and deletions in logarithmic time.
It's commonly used in databases and file systems.
"""

class BTreeNode:
    """Node in a B-Tree."""
    
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf
    
    def split(self, parent, payload):
        """Split a full node and push the middle key up to the parent."""
        new_node = BTreeNode(leaf=self.leaf)
        mid_index = len(self.keys) // 2
        mid_key = self.keys[mid_index]
        
        # Split keys
        new_node.keys = self.keys[mid_index + 1:]
        self.keys = self.keys[:mid_index]
        
        # Split children if not a leaf
        if not self.leaf:
            new_node.children = self.children[mid_index + 1:]
            self.children = self.children[:mid_index + 1]
        
        # Insert middle key into parent
        parent.keys.insert(payload, mid_key)
        parent.children.insert(payload + 1, new_node)


class BTree:
    """B-Tree implementation."""
    
    def __init__(self, degree=3):
        """
        Initialize B-Tree with given minimum degree.
        Minimum degree (t) is the minimum number of keys in a non-root node.
        Maximum keys in a node = 2*t - 1
        """
        self.root = BTreeNode()
        self.degree = degree
    
    def search(self, key, node=None):
        """Search for a key in the B-Tree."""
        if node is None:
            node = self.root
        
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        
        if i < len(node.keys) and key == node.keys[i]:
            return True
        elif node.leaf:
            return False
        else:
            return self.search(key, node.children[i])
    
    def insert(self, key):
        """Insert a key into the B-Tree."""
        if len(self.root.keys) >= 2 * self.degree - 1:
            # Root is full, split it
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self.root.split(new_root, 0)
            self.root = new_root
        
        self._insert_non_full(self.root, key)
    
    def _insert_non_full(self, node, key):
        """Insert a key into a non-full node."""
        i = len(node.keys) - 1
        
        if node.leaf:
            # Insert key in sorted order
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            # Find child to insert into
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            
            # Check if child is full
            if len(node.children[i].keys) >= 2 * self.degree - 1:
                node.children[i].split(node, i)
                if key > node.keys[i]:
                    i += 1
            
            self._insert_non_full(node.children[i], key)
    
    def print_tree(self, node=None, level=0):
        """Print the B-Tree structure."""
        if node is None:
            node = self.root
        
        print(f"Level {level}: {node.keys}")
        
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)
    
    def get_all_keys(self, node=None):
        """Get all keys in sorted order."""
        if node is None:
            node = self.root
        
        keys = []
        
        if node.leaf:
            return node.keys[:]
        else:
            for i, key in enumerate(node.keys):
                keys.extend(self.get_all_keys(node.children[i]))
                keys.append(key)
            keys.extend(self.get_all_keys(node.children[-1]))
        
        return keys


# Example usage
if __name__ == "__main__":
    btree = BTree(degree=3)
    
    # Insert values
    values = [10, 20, 5, 6, 12, 30, 7, 17]
    print("Inserting values:", values)
    for val in values:
        btree.insert(val)
    
    print("\nB-Tree Operations:")
    print("Tree structure:")
    btree.print_tree()
    
    print(f"\nAll keys (sorted): {btree.get_all_keys()}")
    print(f"Search 6: {btree.search(6)}")
    print(f"Search 15: {btree.search(15)}")
    
    # Insert more values to see splits
    print("\nInserting more values: [25, 40, 50]")
    for val in [25, 40, 50]:
        btree.insert(val)
    
    print("\nUpdated tree structure:")
    btree.print_tree()
    print(f"All keys (sorted): {btree.get_all_keys()}")
