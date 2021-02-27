import sys
sys.setrecursionlimit(2097152) 
class Solution:
    
    def _build(self, data, edges):
        self._graph = {i:[] for i in range(len(data))}
        for u,v in edges:
            self._graph[u-1].append(v-1)
            self._graph[v-1].append(u-1)

    def _mincut(self):
        nodes = [0]
        while len(nodes) > 0:
            curr = nodes.pop()
            for child in self._graph[curr]:
                if not self._visited[child]:
                    self._visited[child] = True
                    nodes.append(child)
                    print(self._data[child])
                    
                
        return self._data[curr]
    
    def __mincut(self, curr=0):
        self._visited[curr] = True
        below = self._data[curr]
        for node in self._graph[curr]:
            if not self._visited[node]:
                below += self.__mincut(node)
        self._mini = min(self._mini, abs(self._total - 2*below ))
        return below
        
    def mincut(self, data, edges):
        self._mini = float('inf')
        self._visited = [False for _ in range(len(data))]
        self._data = data
        self._total = sum(data)
        self._build(data, edges)
        self.__mincut()
        return self._mini
        
nodeCount = int(input())
data = list(map(int, input().split()))
edges = []
for _ in range(nodeCount-1):
    edges.append(list(map(int, input().split())))
    
solution = Solution()
res = solution.mincut(data, edges)
print(res)
