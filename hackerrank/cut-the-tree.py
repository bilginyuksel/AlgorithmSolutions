def buildGraph(nodes, edges):
    graph = {i: [] for i in range(len(nodes))}

    for u,v in edges:
        graph[u].append(v)
    
    return graph

def findMinDiff(graph, nodes, edges, total):
    # traverse the graph
    pass



def cutTheTree(nodes, edges):
    graph = buildGraph(nodes, edges)
    minDiff = findMinDiff(nodes, edges, total)
    return minDiff

     

nodeLength = int(input())
nodes = []
for _ in range(nodeLength):
    nodes.append(int(input()))

edges = []
for _ in range(nodeLength-1):
    u, v = map(int, input())
    edges.append([u, v])

absoluteMinDifference = cutTheTree(nodes, edges)
print(absoluteMinDifference)
