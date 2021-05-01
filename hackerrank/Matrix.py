class DisjointSet:

    def __init__(self, size, machines):
        self.parent = [i for i in range(size)] 
        self.rank = [1 for _ in range(size)]
        self.machines = [False for _ in range(size)]
        for machine in machines:
            self.machines[machine] = True
        self.cost = 0

    def find(self, subset):
        if self.parent[subset] != subset:
            return self.find(self.parent[subset])
        return self.parent[subset]

    def union(self, subset1, subset2, weight):
        p1 = self.find(subset1)
        p2 = self.find(subset2)

        # print(self.machines)
        if self.machines[p1] and self.machines[p2]:
            self.cost += weight
            return

        isMachine = self.machines[p2] or self.machines[p1]
        # print("p1: %d, p2: %d, isMachine: %s" % (p1, p2, isMachine))
        # print("s1: %d, s2: %d, isMachine: %s" % (subset1, subset2, isMachine))

        r1 = self.rank[p1]
        r2 = self.rank[p2]


        if r1 > r2:
            self.parent[p2] = p1
            self.rank[p1] += r2
            self.machines[p1] = isMachine
        else:
            self.parent[p1] = p2
            self.rank[p2] += r1
            self.machines[p2] = isMachine

def minTime(size, roads, machines):
    roads.sort(key= lambda x : x[2], reverse=True)

    disjointSet = DisjointSet(size, machines)
    for u, v, w in roads:
        disjointSet.union(u, v, w)

    return disjointSet.cost

roads = []
machines = []

n, m = map(int, input().split())

for _ in range(n-1):
   roads.append(list(map(int, input().split())))

for _ in range(m):
   machines.append(int(input()))

# n = 5
# roads = [[2,1,8], [1, 0, 5], [2, 4, 5], [1, 3, 4]]
# machines = [2, 4, 0]
print(minTime(n, roads, machines))

