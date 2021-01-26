#An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.
#
#Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .
#
#Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

class Graph:

    def buildGraph(self, n, edgeList):
        self.n = n
        self.nodes = {i: [] for i in range(n)}
        
        for edge in edgeList:
            conn = GraphConn(edge[0], edge[1], edge[2])
            connReversed = GraphConn(edge[1], edge[0], edge[2])
            self.nodes[edge[0]].append(conn)
            self.nodes[edge[1]].append(connReversed)

    def checkPath(self, start, end, limit):
        self.visited = set() 
        self.dfs(start, end, None, [])
        return True

    def reverse(self, conn):
        return GraphConn(conn.n2, conn.n1, conn.weight)

    def dfs(self, curr, dest, conn, path):
        if conn:
            self.visited.add(conn)
            self.visited.add(self.reverse(conn))
            path.append(conn.weight)

        if curr == dest:
            print(path)
            return True

        for idx, connections in self.nodes.items():
            for conn in connections:
                if not conn in self.visited:
                    self.dfs(conn.n2, dest, conn, path)
        
                    path.pop()


class GraphConn:

    def __init__(self, node1, node2, w):
        self.n1 = node1
        self.n2 = node2
        self.weight = w

class Solution:

    def distanceLimitedPathsExist(self, n, edgeList, queries):
        # check for the each edge between 2 nodes.
        # create a graph data structure first.
        graph = Graph()
        graph.buildGraph(n, edgeList)
        result = []
        # for query in queries:
        #     result.append(graph.checkPath(query[0], query[1], query[2]))
        #     continue
        result.append(graph.checkPath(queries[0][0], queries[0][1], queries[0][2]))

        return result


sol = Solution()
res = sol.distanceLimitedPathsExist(3, [[0,1,2], [1,2,4], [2,0,8], [1,0,16]], [[0,1,2], [0,2,5]])
print(res)
