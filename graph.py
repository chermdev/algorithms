class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def display(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(str(v)
                  for v in self.graph[vertex]))


# Create a graph
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(1, 4)
g.add_edge(4, 6)

# Display the graph
g.display()
# Output:
# 1 -> 2 -> 3
# 2 -> 3
