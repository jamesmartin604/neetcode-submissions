class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        count = 0
        for x in words:
            if x.startswith(pref):
                count += 1
        return count


        