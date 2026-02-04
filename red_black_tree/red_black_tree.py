"""
Red-Black Tree Implementation

A Red-Black Tree is a self-balancing binary search tree with the following properties:
1. Every node is either red or black
2. The root is black
3. All leaves (NIL) are black
4. Red nodes have black children
5. Every path from root to leaf has the same number of black nodes
"""

class Color:
    RED = 0
    BLACK = 1


class TreeNode:
    """Node in a Red-Black Tree."""
    
    def __init__(self, value, color=Color.RED):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    """Red-Black Tree implementation."""
    
    def __init__(self):
        self.NIL = TreeNode(None, Color.BLACK)
        self.root = self.NIL
    
    def insert(self, value):
        """Insert a value into the Red-Black Tree."""
        new_node = TreeNode(value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        
        parent = None
        current = self.root
        
        # Find position for new node
        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right
        
        new_node.parent = parent
        
        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        
        # Fix Red-Black Tree properties
        self._fix_insert(new_node)
    
    def _fix_insert(self, node):
        """Fix Red-Black Tree properties after insertion."""
        while node.parent and node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                
                if uncle.color == Color.RED:
                    # Case 1: Uncle is red
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: Node is right child
                        node = node.parent
                        self._rotate_left(node)
                    
                    # Case 3: Node is left child
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                
                if uncle.color == Color.RED:
                    # Case 1: Uncle is red
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2: Node is left child
                        node = node.parent
                        self._rotate_right(node)
                    
                    # Case 3: Node is right child
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._rotate_left(node.parent.parent)
        
        self.root.color = Color.BLACK
    
    def _rotate_left(self, x):
        """Perform left rotation."""
        y = x.right
        x.right = y.left
        
        if y.left != self.NIL:
            y.left.parent = x
        
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
    
    def _rotate_right(self, y):
        """Perform right rotation."""
        x = y.left
        y.left = x.right
        
        if x.right != self.NIL:
            x.right.parent = y
        
        x.parent = y.parent
        
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        
        x.right = y
        y.parent = x
    
    def search(self, value):
        """Search for a value in the tree."""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper method for recursive search."""
        if node == self.NIL:
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
        
        if node != self.NIL:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        
        return result
    
    def is_valid_red_black_tree(self):
        """Verify Red-Black Tree properties."""
        if self.root.color != Color.BLACK:
            return False
        
        def check_properties(node, black_count, path_black_count):
            if node == self.NIL:
                if path_black_count[0] == -1:
                    path_black_count[0] = black_count
                return path_black_count[0] == black_count
            
            if node.color == Color.RED:
                if (node.left.color == Color.RED or 
                    node.right.color == Color.RED):
                    return False
            else:
                black_count += 1
            
            return (check_properties(node.left, black_count, path_black_count) and
                    check_properties(node.right, black_count, path_black_count))
        
        return check_properties(self.root, 0, [-1])


# Example usage
if __name__ == "__main__":
    rbt = RedBlackTree()
    
    # Insert values
    values = [10, 20, 30, 15, 25, 5, 1]
    print("Inserting values:", values)
    for val in values:
        rbt.insert(val)
    
    print("\nRed-Black Tree Operations:")
    print(f"Inorder traversal: {rbt.inorder_traversal()}")
    print(f"Search 15: {rbt.search(15)}")
    print(f"Search 100: {rbt.search(100)}")
    print(f"Is valid Red-Black Tree: {rbt.is_valid_red_black_tree()}")
