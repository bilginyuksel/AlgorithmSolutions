class CountLuck:
    def _findStartPoint(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 'M':
                    return [i, j]
        return None

    def _isValid(self, i, j):
        notOutOfLowerBounds = i >= 0 and j >= 0
        notOutOfUpperBounds = i < len(self.matrix) and j < len(self.matrix[0])
        notOutOfBounds = notOutOfLowerBounds and notOutOfUpperBounds
        return notOutOfBounds and not self.visited[i][j] and self.matrix[i][j] != 'X'

    def _wandCount(self, i, j, wand):
        if self.matrix[i][j] == '*':
            self.sharedWand = wand
            return
        self.visited[i][j] = True
        validPathCount = self._isValid(i+1, j) + self._isValid(i-1, j) + self._isValid(i, j+1) + self._isValid(i, j-1)
        
        if validPathCount > 1:
            wand += 1
            
        if self._isValid(i+1, j):
            self._wandCount(i+1, j, wand)
        if self._isValid(i-1, j):
            self._wandCount(i-1, j, wand)
        if self._isValid(i, j+1):
            self._wandCount(i, j+1, wand)
        if self._isValid(i, j-1):
            self._wandCount(i, j-1, wand)

    def wandCount(self, matrix, guess):
        self.matrix = matrix
        self.visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.startPoint = self._findStartPoint()
        self.sharedWand = None
        self._wandCount(self.startPoint[0], self.startPoint[1], 0)
        return 'Impressed' if  self.sharedWand == guess else 'Oops!'

tests = int(input())
solution = CountLuck()
for _ in range(tests):
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    k = int(input())
    print(solution.wandCount(matrix, k))