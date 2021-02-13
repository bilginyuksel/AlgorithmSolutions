def findRegionCells(cells, visited, i, j):
    if i >= len(cells) or j >= len(cells[0]) or i < 0 or j < 0 or visited[i][j] or cells[i][j] == 0:
        return 0

    visited[i][j] = True
    count = 1
    count += findRegionCells(cells, visited, i-1, j) 
    count += findRegionCells(cells, visited, i, j-1)
    count += findRegionCells(cells, visited, i+1, j)
    count += findRegionCells(cells, visited, i, j+1)
    count += findRegionCells(cells, visited, i+1, j+1)
    count += findRegionCells(cells, visited, i-1, j-1)
    count += findRegionCells(cells, visited, i+1, j-1)
    count += findRegionCells(cells, visited, i-1, j+1)

    return count


def findMaxRegionCellCount(cells):
    # look for 1's find the maxRegion
    maxCells = 0
    visited = [[False for _ in range(len(cells[0]))] for _ in range(len(cells))]
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            if not visited[i][j] and cells[i][j] == 1:
                potentialMaxCells = findRegionCells(cells, visited, i, j)
                maxCells = max(maxCells, potentialMaxCells)
    return maxCells

rows = int(input())
columns = int(input())

cells = []
for _ in range(rows):
    cells.append(list(map(int, input().split())))

result = findMaxRegionCellCount(cells)
print(result)
