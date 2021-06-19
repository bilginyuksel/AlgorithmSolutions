class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = None

    def update(self, word):
        self.end = True
        self.word = word
    
    def has(self, char):
        return char in self.children

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def build(self, words):
        for word in words:
            node = self.root
            for char in word:
                if not node.has(char):
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.update(word)

    def find(self, i, j, board):
        visited = set()
        result = set()

        def finder(i, j, node):
            if i>=len(board) or j>=len(board[0]) or i<0 or j<0 or (i,j) in visited or not node.has(board[i][j]):
                return

            visited.add((i, j))
            node = node.children[board[i][j]]
    
            if node.end:
                result.add(node.word)

            finder(i-1, j, node)
            finder(i+1, j, node)
            finder(i, j-1, node)
            finder(i, j+1, node)

            visited.remove((i,j))

        finder(i, j, self.root)
        return list(result)


class Solution:
    
    def addToSet(self, simpleSet, arr):
        for elem in arr:
            simpleSet.add(elem)

    def findWords(self, board, words):
        result = set()
        trie = Trie()
        trie.build(words)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if trie.root.has(board[i][j]):
                    res = trie.find(i, j, board)
                    self.addToSet(result, res)
        return result

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

s = Solution()
result = s.findWords(board, words)
print(result)

