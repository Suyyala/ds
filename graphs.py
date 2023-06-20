# learning graphs in python


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def get_vertices(self):
        return list(self.gdict.keys())
    
    def edges(self):
        return self.find_edges()
    
    def find_edges(self):
        edges = []
        for vertex in self.gdict:
            for neighbour in self.gdict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        
        return edges
    
    def add_vertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.gdict:
            self.gdict[vertex1].append(vertex2)
        else:
            self.gdict[vertex1] = [vertex2]

    def __str__(self):
        return str(self.gdict)
    
    def bfs(self, start_vertex):
        visited = [start_vertex]
        queue = [start_vertex]
        while queue:
            vertex = queue.pop(0)
            print(vertex)
            for neighbour in self.gdict[vertex]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    def dfs(self, start_vertex):
        visited = [start_vertex]
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            print(vertex)
            for neighbour in self.gdict[vertex]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)


g = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}

graph = Graph(g)
print(graph.get_vertices())
print(graph.edges())
graph.add_vertex("f")
print(graph.get_vertices())
graph.add_edge({"a", "e"})
graph.add_edge({"a", "c"})
print(graph.edges())
print(graph)
graph.bfs("a")
graph.dfs("a")
