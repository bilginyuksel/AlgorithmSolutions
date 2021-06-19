class Solution:

    def findStartingPoint(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return i, j
        return None, None
    
    def allVisited(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    return False
        return True

    def countUniquePaths(self, grid,x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == -1:
            return 0

        if grid[x][y] == 2:
            return self.allVisited(grid)

        grid[x][y] = -1
        count = 0
        count += self.countUniquePaths(grid, x-1, y)
        count += self.countUniquePaths(grid, x+1, y)
        count += self.countUniquePaths(grid, x, y-1)
        count += self.countUniquePaths(grid, x, y+1)
        grid[x][y] = 0

        return count

    def uniquePathsIII(self, grid):
        startX, startY = self.findStartingPoint(grid)
        if startX is None or startY is None: return 0

        return self.countUniquePaths(grid, startX, startY)

t = Solution()
res = t.uniquePathsIII([[1,0,0,0], [0,0,0,0], [0,0,2,-1]])
print('expected: 2, given: %d' % res)
