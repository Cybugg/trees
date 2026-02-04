"""
Binary Tree Implementation

A binary tree is a tree data structure where each node has at most two children,
referred to as the left child and the right child.
"""

class TreeNode:
    """Node in a binary tree."""
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """Binary Tree implementation with common operations."""
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a value into the binary tree using level-order insertion."""
        if not self.root:
            self.root = TreeNode(value)
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            
            if not node.left:
                node.left = TreeNode(value)
                return
            else:
                queue.append(node.left)
            
            if not node.right:
                node.right = TreeNode(value)
                return
            else:
                queue.append(node.right)
    
    def inorder_traversal(self, node=None, result=None):
        """
        Inorder traversal (Left -> Root -> Right).
        Returns list of values.
        """
        if result is None:
            result = []
            node = self.root
        
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        
        return result
    
    def preorder_traversal(self, node=None, result=None):
        """
        Preorder traversal (Root -> Left -> Right).
        Returns list of values.
        """
        if result is None:
            result = []
            node = self.root
        
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        
        return result
    
    def postorder_traversal(self, node=None, result=None):
        """
        Postorder traversal (Left -> Right -> Root).
        Returns list of values.
        """
        if result is None:
            result = []
            node = self.root
        
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
        
        return result
    
    def level_order_traversal(self):
        """
        Level order traversal (breadth-first).
        Returns list of values.
        """
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self, node=None, _initial_call=True):
        """Calculate the height of the tree."""
        if _initial_call and node is None:
            node = self.root
        
        if not node:
            return 0
        
        left_height = self.height(node.left, False)
        right_height = self.height(node.right, False)
        
        return max(left_height, right_height) + 1
    
    def size(self, node=None, _initial_call=True):
        """Calculate the number of nodes in the tree."""
        if _initial_call and node is None:
            node = self.root
        
        if not node:
            return 0
        
        return 1 + self.size(node.left, False) + self.size(node.right, False)


# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    
    # Insert values
    values = [1, 2, 3, 4, 5, 6, 7]
    for val in values:
        tree.insert(val)
    
    print("Binary Tree Operations:")
    print(f"Inorder traversal: {tree.inorder_traversal()}")
    print(f"Preorder traversal: {tree.preorder_traversal()}")
    print(f"Postorder traversal: {tree.postorder_traversal()}")
    print(f"Level order traversal: {tree.level_order_traversal()}")
    print(f"Height: {tree.height()}")
    print(f"Size: {tree.size()}")
