
def buildGraph(n, cities):
    graph = {i: [] for i in range(n)}
    for u,v in cities:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    return graph
    
def connectCities(graph, visited, city):
    visited[city] = True
    roads = 0
    for nextCity in graph[city]:
        if not visited[nextCity]:
            roads += 1 + connectCities(graph, visited, nextCity)
    return roads
    
def roadsAndLibraries(n, libraryCost, roadCost, cities):
    if libraryCost < roadCost:
        return n * libraryCost
    
    graph = buildGraph(n, cities)
    visited = [False for _ in range(n)]

    libraryCount = 0
    totalRoadCost = 0
    
    for i in range(n):
        if not visited[i]:
            roadCount = connectCities(graph, visited, i)
            totalRoadCost += roadCount * roadCost
            libraryCount += 1
            
    return (libraryCost*libraryCount ) + totalRoadCost


t = int(input())
for _ in range(t):
    n, m, libCost, roadCost = map(int, input().split())
    cities = []
    for _ in range(m):
        cities.append(list(map(int, input().split())))
    totalCost = roadsAndLibraries(n, libCost, roadCost, cities)
    print(totalCost)
