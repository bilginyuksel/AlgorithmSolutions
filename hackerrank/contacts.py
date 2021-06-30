class TrieNode:
    def __init__(self):
        self.occurrence = 0
        self.children = {}

    def occurenced(self):
        self.occurrence += 1

    def has(self, char):
        return char in self.children


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def update(self, word):
        node = self.root
        for char in word:
            if not node.has(char):
                node.children[char] = TrieNode()
            node = node.children[char]
            node.occurenced()

    def find(self, word):
        node = self.root
        for char in word:
            if not node.has(char):
                return 0
            node = node.children[char]
        return node.occurrence


numberOfQueries = int(input()) 
trie = Trie()
for _ in range(numberOfQueries):
    operation, word = input().split()
    if operation == 'add':
        trie.update(word)
    else:
        print(trie.find(word))



