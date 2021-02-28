from collections import deque 

class Solution:

    def isLimitedPathExist(self,n, edgeList, queries):
        graph = {i:[] for i in range(n)}
        for u,v,dist in edgeList:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
            
        def findLimitedPath(curr, dest, limit, visited):
            if curr == dest:
                return True
            visited[curr] = True 
            isExist = False
            for node,dist in graph[curr]:
                if not visited[node] and dist < limit:
                    isExist = isExist or findLimitedPath(node, dest, limit)

            return isExist
        
        results = []
        for start,end,limit in queries:
            visited = [False for i in range(n)]
            result = findLimitedPath(start, end, limit, visited)
            results.append(result)

        return results

    def union(self, u, v):
        self.graph[self.find(u)] = self.find(v)

    def find(self, x):
        if self.graph[x] != x:
            self.graph[x] = self.find(self.graph[x])
        return self.graph[x]

    def isConnected(self, u, v):
        return self.find(u) == self.find(v)

    def optimizedIsLimitedPathsExist(self, n, edgeList, queries):
        results = [] 
        self.graph = list(range(n)) 
        edgeList = deque(sorted((d,u,v) for u,v,d in edgeList))
        queries.sort(key= lambda x:x[2]) # sort by weight
        for start,end,limit in queries:
            # find edges smaller than limit
            while edgeList and edgeList[0][0] < limit:
                _, u, v = edgeList.popleft()
                self.union(u,v)

            results.append(self.isConnected(start, end))

        return results

    def distanceLimitedPathsExist(self, n, edgeList, queries):
        # Time Limit Exceed Solution: return self.isLimitedPathExist(n, edgeList, queries)
        return self.optimizedIsLimitedPathsExist(n, edgeList, queries)

solve = Solution()
result = solve.distanceLimitedPathsExist(3, [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], [[0,1,2],[0,2,5]])
print('Case #1: %s' % result)

