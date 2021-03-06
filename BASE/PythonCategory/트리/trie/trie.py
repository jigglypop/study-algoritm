from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False

    def __repr__(self):
        return f'TrieNode({self.word}:{self.children.items()})'


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # 단어 존재 여부 판별
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        # 단어 끝까지 검사
        return node.word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        # 여기만 다름
        return True


trie = Trie()
trie.add('apple')
trie.add('appeal')
print(trie.search('apple'))
print(trie.startsWith('a'))
