class DisjointSet:

    def __init__(self, numberOfSets):
        self.parent = [i for i in range(numberOfSets)]
        self.rank = [1 for _ in range(numberOfSets)]

    def union(self, firstChild, secondChild):
        firstParent = self._find(firstChild)
        secondParent = self._find(secondChild)

        if firstParent == secondParent:
            return

        if self.rank[firstParent] > self.rank[secondParent]:
            self.parent[secondParent] = firstParent
            self.rank[firstParent] += self.rank[secondParent]
        else:
            self.parent[firstParent] = secondParent
            self.rank[secondParent] += self.rank[firstParent]

    def getSize(self, child):
        parent = self._find(child)
        return self.rank[parent]

    def _find(self, x):
        if self.parent[x] == x:
            return x
        return self._find(self.parent[x])

numberOfPeople, numberOfQueries = map(int, input().split())
queries = []

for _ in range(numberOfQueries):
    queries.append(input().split())

dj = DisjointSet(numberOfPeople)

for query in queries:
    queryType = query[0]
    if queryType == 'M':
        i, j = int(query[1]), int(query[2])
        dj.union(i-1, j-1)
    else:
        i = int(query[1])
        size = dj.getSize(i-1)
        print(size)


