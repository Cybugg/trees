"""
Tests for Trie (Prefix Tree) implementation
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from trie import Trie


def test_insert_and_search():
    trie = Trie()
    
    trie.insert("hello")
    trie.insert("world")
    
    assert trie.search("hello") == True
    assert trie.search("world") == True
    assert trie.search("hell") == False
    assert trie.search("worlds") == False


def test_starts_with():
    trie = Trie()
    
    trie.insert("apple")
    trie.insert("app")
    trie.insert("application")
    
    assert trie.starts_with("app") == True
    assert trie.starts_with("appl") == True
    assert trie.starts_with("banana") == False


def test_delete():
    trie = Trie()
    
    trie.insert("apple")
    trie.insert("app")
    
    assert trie.search("app") == True
    
    trie.delete("app")
    assert trie.search("app") == False
    assert trie.search("apple") == True


def test_get_all_words():
    trie = Trie()
    
    words = ["cat", "car", "card", "dog"]
    for word in words:
        trie.insert(word)
    
    all_words = trie.get_all_words()
    assert sorted(all_words) == sorted(words)


def test_autocomplete():
    trie = Trie()
    
    words = ["apple", "app", "application", "apply"]
    for word in words:
        trie.insert(word)
    
    suggestions = trie.autocomplete("app")
    assert len(suggestions) == 4
    assert "apple" in suggestions
    assert "app" in suggestions
    assert "application" in suggestions
    assert "apply" in suggestions


def test_empty_trie():
    trie = Trie()
    
    assert trie.search("test") == False
    assert trie.starts_with("test") == False
    assert trie.get_all_words() == []
    assert trie.autocomplete("test") == []


def test_prefix_that_is_word():
    trie = Trie()
    
    trie.insert("car")
    trie.insert("card")
    
    assert trie.search("car") == True
    assert trie.search("card") == True
    assert trie.starts_with("car") == True


if __name__ == "__main__":
    test_insert_and_search()
    test_starts_with()
    test_delete()
    test_get_all_words()
    test_autocomplete()
    test_empty_trie()
    test_prefix_that_is_word()
    print("All Trie tests passed!")
