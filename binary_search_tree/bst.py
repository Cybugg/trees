"""
Binary Search Tree (BST) Implementation

A Binary Search Tree is a binary tree where for each node:
- All values in the left subtree are less than the node's value
- All values in the right subtree are greater than the node's value
"""

class TreeNode:
    """Node in a binary search tree."""
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree implementation with common operations."""
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a value into the BST."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper method for recursive insertion."""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Search for a value in the BST. Returns True if found, False otherwise."""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper method for recursive search."""
        if node is None:
            return False
        
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        """Delete a value from the BST."""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        """Helper method for recursive deletion."""
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: get inorder successor
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        
        return node
    
    def _find_min(self, node):
        """Find the node with minimum value in a subtree."""
        current = node
        while current.left:
            current = current.left
        return current
    
    def find_min(self):
        """Find the minimum value in the BST."""
        if not self.root:
            return None
        return self._find_min(self.root).value
    
    def find_max(self):
        """Find the maximum value in the BST."""
        if not self.root:
            return None
        
        current = self.root
        while current.right:
            current = current.right
        return current.value
    
    def inorder_traversal(self, node=None, result=None):
        """
        Inorder traversal (Left -> Root -> Right).
        Returns sorted list of values.
        """
        if result is None:
            result = []
            node = self.root
        
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        
        return result
    
    def height(self, node=None, _initial_call=True):
        """Calculate the height of the BST."""
        if _initial_call and node is None:
            node = self.root
        
        if not node:
            return 0
        
        left_height = self.height(node.left, False)
        right_height = self.height(node.right, False)
        
        return max(left_height, right_height) + 1
    
    def is_valid_bst(self, node=None, min_val=float('-inf'), max_val=float('inf'), _initial_call=True):
        """Check if the tree is a valid BST."""
        if _initial_call and node is None:
            node = self.root
        
        if not node:
            return True
        
        if node.value <= min_val or node.value >= max_val:
            return False
        
        return (self.is_valid_bst(node.left, min_val, node.value, False) and
                self.is_valid_bst(node.right, node.value, max_val, False))


# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    
    print("Binary Search Tree Operations:")
    print(f"Inorder traversal (sorted): {bst.inorder_traversal()}")
    print(f"Search 40: {bst.search(40)}")
    print(f"Search 100: {bst.search(100)}")
    print(f"Min value: {bst.find_min()}")
    print(f"Max value: {bst.find_max()}")
    print(f"Height: {bst.height()}")
    print(f"Is valid BST: {bst.is_valid_bst()}")
    
    # Delete a value
    print(f"\nDeleting 30...")
    bst.delete(30)
    print(f"Inorder traversal: {bst.inorder_traversal()}")
