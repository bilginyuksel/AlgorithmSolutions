int(input())
arr = list(map(int, input().split()))

def countSkyScrapersToTravel(heights):
    heightStk = []
    count = 0
    for heightIdx in range(len(heights)):
        currentHeight = heights[heightIdx]
        while len(heightStk) > 0 and currentHeight > heightStk[-1][0]:
            heightStk.pop()

        if len(heightStk) > 0 and currentHeight == heightStk[-1][0]:
            print('StkHeight: %s, CurrHeight: %d, CurrCount: %d' % (heightStk[-1], currentHeight, count))
            count += heightStk[-1][1]
            heightStk[-1][1] += 1
        else:
            heightStk.append([heights[heightIdx], 1])

    return count * 2

print(countSkyScrapersToTravel(arr))