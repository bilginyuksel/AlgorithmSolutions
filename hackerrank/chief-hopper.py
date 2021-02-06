def findMinEnergy(heights):
    shouldProduceEnergy = 0
    for height in reversed(heights):
        shouldProduceEnergy = (shouldProduceEnergy + height + 1) // 2
    return shouldProduceEnergy

input() # not necessary
heights = list(map(int, input().split()))
print(findMinEnergy(heights))
