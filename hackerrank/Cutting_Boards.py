MOD = (10 ** 9) + 7

def mergeCosts(horizontalCosts, verticalCosts):
    arr = []
    for horCost in horizontalCosts:
        arr.append((horCost, 'h'))
    for verCost in verticalCosts:
        arr.append((verCost, 'v'))
    return arr
    
def findBoardCuttingCosts(horizontalCosts, verticalCosts):
   
    totalCost = 0
    arr = mergeCosts(horizontalCosts, verticalCosts)
    arr.sort(key= lambda x: x[0], reverse=True)
    verticalCutCount = horizontalCutCount = 1
    
    for elem in arr:
        cost = elem[0]
        cutStyle = elem[1]
        
        if cutStyle == 'h':
            totalCost += cost * verticalCutCount
            horizontalCutCount += 1
        else:
            totalCost += cost * horizontalCutCount
            verticalCutCount += 1

    return totalCost


queryCount = int(input())
for _ in range(queryCount):
    input() # row and column input not necessary for python
    horizontalCosts = list(map(int, input().split()))
    verticalCosts = list(map(int, input().split()))

    totalCost = findBoardCuttingCosts(horizontalCosts, verticalCosts)
    print(totalCost % MOD)
