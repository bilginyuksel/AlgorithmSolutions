def getMinimumCost(k, costs):
    costs.sort(reverse=True)
    coef = 1
    person = k
    total = 0
    for cost in costs:
       total += cost * coef 
       person-=1 
       if person == 0:
           person = k
           coef += 1

    return total

flowers, person = list(map(int, input().split()))
costs = list(map(int, input().split()))
print(getMinimumCost(person, costs))

