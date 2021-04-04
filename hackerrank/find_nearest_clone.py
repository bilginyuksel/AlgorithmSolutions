import collections

class Graph:

    def __init__(self) -> None:
        self.graph = collections.defaultdict(list)
        self.is_graph_built = False

    def _find_first_clone_path(self, node, clone_color, current_path):
        self.visited[node] = True 

        for curr_node in self.graph[node]:
            if not self.visited[curr_node]:
                if self.colors[curr_node] == clone_color:
                    print("(debug): current path=", current_path + 1)
                    self.potential_shortest_path = current_path + 1
                    return
                else:
                    self._find_first_clone_path(curr_node, clone_color, current_path + 1)

    def _build_graph(self, node_count, connections, colors):
        for start, dest in connections:
            self.graph[start-1].append(dest-1)
            self.graph[dest-1].append(start-1)

        self.colors = colors.copy()
        self.visited = [False for _ in range(node_count)]

        self.is_graph_built = True

    def find_shortest(self, node_count, connections, colors, clone_color):
        if not self.is_graph_built:
            self._build_graph(node_count, connections, colors)

        shortest_path = float('inf')
        for node in range(node_count):
            if not self.visited[node] and self.colors[node] == clone_color:
                self.potential_shortest_path = float('inf')
                self._find_first_clone_path(node, clone_color, 0)
                print("(debug): potential shortest path=", self.potential_shortest_path)
                shortest_path = min(shortest_path, self.potential_shortest_path)
        
        return -1 if shortest_path == float('inf') else shortest_path

    def clear(self):
        self.graph.clear()
        self.visited.clear()
        self.colors.clear()
        self.is_graph_built = False


#node_count, conn_count = map(int, input().split())
#connections = [list(map(int, input().split())) for _ in range(conn_count)]
#colors = list(map(int, input().split()))
#requested_color = int(input())

def test_find_shortest():
    def test1():
        assert_find_shortest(4, [[1,2], [1,3], [4,2]], [1,2,3,4], 2, -1)

    def test2():
        assert_find_shortest(5, [[1,2], [1,3], [2,4], [3,5]], [1,2,3,3,2], 2, 3)

    def test3():
        assert_find_shortest(4, [[1,2], [1,3], [4,2]], [1,2,1,1], 1, 1)

    def assert_find_shortest(node_count, connections, colors, requested_color, expected_output):
        print("test is running")
        graph = Graph()
        assert expected_output == graph.find_shortest(node_count, connections, colors, requested_color)
        print("test is successfull")
    
    test1()
    test2()
    test3()


test_find_shortest()

#graph = Graph()
#shortest_path = graph.find_shortest(node_count, connections, colors, requested_color)
#print(shortest_path)
