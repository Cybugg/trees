"""
Trie (Prefix Tree) Implementation

A Trie is a tree-like data structure used to store strings. Each path from the root
to a node represents a string prefix. Tries are efficient for prefix-based operations
like autocomplete and spell checking.
"""

class TrieNode:
    """Node in a Trie."""
    
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """Trie (Prefix Tree) implementation."""
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
    
    def search(self, word):
        """Search for a word in the trie. Returns True if found."""
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """Check if there's any word in the trie that starts with the given prefix."""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
    
    def delete(self, word):
        """Delete a word from the trie."""
        def _delete_recursive(node, word, index):
            if index == len(word):
                # Base case: reached end of word
                if not node.is_end_of_word:
                    return False
                
                node.is_end_of_word = False
                # Return True if node has no children (can be deleted)
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            child_node = node.children[char]
            should_delete_child = _delete_recursive(child_node, word, index + 1)
            
            if should_delete_child:
                del node.children[char]
                # Return True if node has no children and is not end of another word
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        _delete_recursive(self.root, word, 0)
    
    def get_all_words(self):
        """Get all words stored in the trie."""
        words = []
        self._collect_words(self.root, "", words)
        return words
    
    def _collect_words(self, node, prefix, words):
        """Helper method to collect all words from a node."""
        if node.is_end_of_word:
            words.append(prefix)
        
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, words)
    
    def autocomplete(self, prefix):
        """Get all words that start with the given prefix."""
        node = self.root
        
        # Navigate to the prefix
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Collect all words from this point
        words = []
        self._collect_words(node, prefix, words)
        return words


# Example usage
if __name__ == "__main__":
    trie = Trie()
    
    # Insert words
    words = ["apple", "app", "application", "apply", "banana", "band", "bandana"]
    print("Inserting words:", words)
    for word in words:
        trie.insert(word)
    
    print("\nTrie Operations:")
    print(f"Search 'apple': {trie.search('apple')}")
    print(f"Search 'app': {trie.search('app')}")
    print(f"Search 'appl': {trie.search('appl')}")
    print(f"Starts with 'app': {trie.starts_with('app')}")
    print(f"Starts with 'ban': {trie.starts_with('ban')}")
    print(f"Starts with 'cat': {trie.starts_with('cat')}")
    
    print(f"\nAll words: {trie.get_all_words()}")
    print(f"Autocomplete 'app': {trie.autocomplete('app')}")
    print(f"Autocomplete 'ban': {trie.autocomplete('ban')}")
    
    print("\nDeleting 'app'...")
    trie.delete("app")
    print(f"Search 'app': {trie.search('app')}")
    print(f"Search 'apple': {trie.search('apple')}")
