def getProductCountByTimePassed(machines, timePassed):
    productCount = 0
    for dayToProduce in machines:
        productCount += timePassed // dayToProduce
    return productCount

def findMinimumTimePassed(machines, minTime, maxTime, goal):
    while minTime < maxTime:
        time = (minTime + maxTime) // 2
        productCount = getProductCountByTimePassed(machines, time)
        if productCount < goal:
            minTime = time + 1
        else:
            maxTime = time

    return maxTime

def findMinimumTime(machines, goal):
    minDays = min(machines)    
    maxDays = max(machines)
    
    # passedTime / minDays = goal
    # that means goal * minDays = passedTime
    potentialMinTimeRequired = goal * minDays // len(machines)
    potentialMaxTimeRequired = goal * maxDays // len(machines)
    
    return findMinimumTimePassed(machines, potentialMinTimeRequired, potentialMaxTimeRequired, goal)

goal = int(input().split()[1])
machines = list(map(int, input().split()))
minTime = findMinimumTime(machines, goal)
print(minTime)
