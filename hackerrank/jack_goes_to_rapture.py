import collections

class JackGoesToRapture:

    def __init__(self):
        self.graph = collections.defaultdict(list)

    def _build_graph(self, node_count, routes):
        self.visited = [False for _ in range(node_count)]
        self.destination = node_count - 1
    
        for start, dest, cost in routes:
            self.graph[start-1].append([dest-1, cost]) 

    def _find_min_cost(self, node, current_cost, currently_paid = 0):
        self.visited[node] = True

        if node == self.destination:
            self.min_cost = min(self.min_cost, current_cost)
            return

        for current_node, cost in self.graph[node]:
            if cost > currently_paid:
                current_cost += cost - currently_paid
                currently_paid = cost
            self._find_min_cost(current_node, current_cost, currently_paid)


    def get_min_cost(self, node_count, routes):
        self._build_graph(node_count, routes) 

        self.min_cost = float('inf')
        self._find_min_cost(0, 0)
        return self.min_cost
    
def test():
    test_get_min_cost(5, [[1,2,60],[3,5,70], [1,4,120], [4,5,150], [2,3,80]], 80)
    test_get_min_cost(5, [[1,2,30],[2,3,50], [3,4,70], [4,5,90], [1,3,70], [3,5,85]], 85)
    

def test_get_min_cost(node_count, routes, expected_result):
    print("test running")
    jgp = JackGoesToRapture()
    test_result = jgp.get_min_cost(node_count, routes)
    print("test completed")
    print("#Case X:", test_result)
    assert expected_result == test_result 

test()

#node_count, route_count = map(int, input().split())
#routes = [list(map(int, input().split())) for _ in range(route_count)]

#min_cost = get_min_cost()
#print(min_cost)
