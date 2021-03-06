import sys
sys.stdin = open('trie.txt', 'r')


class Node:
    def __init__(self, character, parent):
        self.character = character
        self.parent = parent
        self.children = dict()
        self.terminus = False

    def add(self, child_node):
        self.children[child_node.character] = child_node


class Trie:

    def __init__(self):
        self._root = Node(None, None)

    def insert_and_check(self, word):
        if word:
            current_node = self._root
            for character in word:
                if character in current_node.children:
                    current_node = current_node.children[character]
                    if current_node.terminus:
                        return True
                else:
                    child_node = Node(character, current_node)
                    current_node.add(child_node)
                    current_node = child_node
            current_node.terminus = True
            if current_node.children:
                return True
        return False


loop = int(input())
for _ in range(loop):
    m = int(input())
    trie = Trie()
    check = False
    for _ in range(m):
        target_number = input()
        if check:
            continue
        check = trie.insert_and_check(target_number)
    print('NO' if check else 'YES')
