class PrefixError(RuntimeError):
    def __init__(self, value):
        self.value = value

class TrieNode:
    def __init__(self, word= None):
        self.children = {}
        self.word = word
    
    def has(self, char):
        return char in self.children

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def update(self, word):
        node = self.root
        for char in word:
            if node.word is not None:
                raise PrefixError(word)
            if not node.has(char):
                node.children[char] = TrieNode()
            node = node.children[char]
        if len(node.children) > 0 or node.word == word:
            raise PrefixError(word)
        node.word = word
            
def noPrefix(words):
    trie = Trie()
    for word in words:
        try:
            trie.update(word)
        except PrefixError as e:
            print('BAD SET')
            print(e.value)
            return
    print('GOOD SET')
    
if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
