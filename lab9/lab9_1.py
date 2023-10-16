class BipartiteGraph:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.match = {}
        self.match_r = {}

    def max_matching(self):
        for u in self.graph:
            self.visited.clear()
            self._dfs(u)
        return len(self.match), list(self.match.items())

    def _dfs(self, u):
        for v in self.graph[u]:
            if v not in self.visited:
                self.visited.add(v)
                if v not in self.match_r or self._dfs(self.match_r[v]):
                    self.match[u] = v
                    self.match_r[v] = u
                    return True
        return False


def main():
    edges = [(11, 2), (3, 10), (6, 2), (8, 1), (7, 5), (6, 10), (12, 2), (14, 1), (14, 15), (5, 4),
             (2, 3), (8, 5), (6, 5), (12, 15), (9, 7), (4, 9), (15, 6), (1, 12), (5, 14), (2, 13),
             (13, 15), (13, 9), (8, 10), (15, 7), (9, 14), (1, 11), (15, 4), (13, 1), (9, 6), (10, 14)]

    # Построение двудольного графа на основе ребер
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)

    bipartite_graph = BipartiteGraph(graph)
    max_matching_size, max_matching = bipartite_graph.max_matching()
    print("Размер наибольшего паросочетания:", max_matching_size)
    print("Наибольшее паросочетание:")
    for u, v in max_matching:
        print(f"{u} , {v}")


if __name__ == "__main__":
    main()
