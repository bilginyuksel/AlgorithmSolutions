def calculateMaxCost(arr):
    
    high = low = 0
    for i in range(1, len(arr)):
        highLow = abs(arr[i-1] - 1)
        lowHigh = abs(arr[i] - 1)
        highHigh = abs(arr[i] - arr[i-1])

        nextLow = max(low, high + highLow) 
        nextHigh = max(high + highHigh, low + lowHigh)

        low = nextLow
        high = nextHigh

    return max(high, low)


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    maxCost = calculateMaxCost(arr)
    print(maxCost)
