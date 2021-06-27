
def countLShapedPlots(grid):
    top = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    left = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0: continue
            top[i][j] = top[i-1][j] + 1
            left[i][j] = left[i][j-1] + 1

    print(top)
    print(left)

    return 1

numberOfTests = int(input())
for i in range(numberOfTests):
    rows, cols = map(int, input().split())
    grid = []
    for _ in range(rows):
        grid.append(list(map(int, input().split())))

    count  = countLShapedPlots(grid)
    print('Case #%d: %d' % (i + 1, count))