"""
AVL Tree Implementation

An AVL tree is a self-balancing binary search tree where the heights of the two
child subtrees of any node differ by at most one. When this property is violated
after an insertion or deletion, the tree is rebalanced using rotations.
"""

class TreeNode:
    """Node in an AVL tree."""
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """AVL Tree implementation with automatic balancing."""
    
    def __init__(self):
        self.root = None
    
    def _get_height(self, node):
        """Get the height of a node."""
        if not node:
            return 0
        return node.height
    
    def _get_balance(self, node):
        """Get the balance factor of a node."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _update_height(self, node):
        """Update the height of a node."""
        if node:
            node.height = 1 + max(self._get_height(node.left), 
                                  self._get_height(node.right))
    
    def _rotate_right(self, z):
        """Perform right rotation."""
        y = z.left
        T3 = y.right
        
        # Perform rotation
        y.right = z
        z.left = T3
        
        # Update heights
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def _rotate_left(self, z):
        """Perform left rotation."""
        y = z.right
        T2 = y.left
        
        # Perform rotation
        y.left = z
        z.right = T2
        
        # Update heights
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def insert(self, value):
        """Insert a value into the AVL tree."""
        self.root = self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper method for recursive insertion with balancing."""
        # Standard BST insertion
        if not node:
            return TreeNode(value)
        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            # Duplicate values not allowed
            return node
        
        # Update height
        self._update_height(node)
        
        # Get balance factor
        balance = self._get_balance(node)
        
        # Left Left Case
        if balance > 1 and value < node.left.value:
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and value > node.right.value:
            return self._rotate_left(node)
        
        # Left Right Case
        if balance > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Left Case
        if balance < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def delete(self, value):
        """Delete a value from the AVL tree."""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        """Helper method for recursive deletion with balancing."""
        if not node:
            return node
        
        # Standard BST deletion
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        
        # Update height
        self._update_height(node)
        
        # Get balance factor
        balance = self._get_balance(node)
        
        # Left Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        
        # Left Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        
        # Right Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _find_min(self, node):
        """Find the node with minimum value in a subtree."""
        current = node
        while current.left:
            current = current.left
        return current
    
    def search(self, value):
        """Search for a value in the AVL tree."""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper method for recursive search."""
        if not node:
            return False
        
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def inorder_traversal(self, node=None, result=None):
        """Inorder traversal (Left -> Root -> Right)."""
        if result is None:
            result = []
            node = self.root
        
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        
        return result
    
    def is_balanced(self, node=None, _initial_call=True):
        """Check if the tree is balanced (AVL property)."""
        if _initial_call and node is None:
            node = self.root
        
        if not node:
            return True
        
        balance = self._get_balance(node)
        
        if abs(balance) > 1:
            return False
        
        return self.is_balanced(node.left, False) and self.is_balanced(node.right, False)


# Example usage
if __name__ == "__main__":
    avl = AVLTree()
    
    # Insert values
    values = [10, 20, 30, 40, 50, 25]
    print("Inserting values:", values)
    for val in values:
        avl.insert(val)
    
    print("\nAVL Tree Operations:")
    print(f"Inorder traversal: {avl.inorder_traversal()}")
    print(f"Is balanced: {avl.is_balanced()}")
    print(f"Search 25: {avl.search(25)}")
    print(f"Search 100: {avl.search(100)}")
    
    # Delete a value
    print(f"\nDeleting 40...")
    avl.delete(40)
    print(f"Inorder traversal: {avl.inorder_traversal()}")
    print(f"Is balanced: {avl.is_balanced()}")
