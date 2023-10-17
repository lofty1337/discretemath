import random
import heapq
from collections import deque


class Graph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs_shortest_paths(self, start):
        distances = [float('inf')] * self.num_vertices
        distances[start] = 0
        iterations = 0

        visited = set()
        queue = deque([start])

        while queue:
            iterations += 1
            vertex = queue.popleft()

            if vertex in visited:
                continue

            visited.add(vertex)

            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    distances[neighbor] = distances[vertex] + 1
                    queue.append(neighbor)

        return distances, iterations

    def dijkstra_shortest_paths(self, start):
        distances = [float('inf')] * self.num_vertices
        distances[start] = 0
        iterations = 0

        visited = set()
        priority_queue = [(0, start)]

        while priority_queue:
            iterations += 1
            distance, vertex = heapq.heappop(priority_queue)

            if vertex in visited:
                continue

            visited.add(vertex)

            for neighbor in self.adj_list[vertex]:
                iterations += 1
                new_distance = distances[vertex] + 1

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        return distances, iterations


def create_sparse_graph(num_vertices, target_degree):
    graph = Graph(num_vertices)
    max_edges = target_degree * num_vertices // 2
    num_edges = random.randint(max_edges // 2, max_edges)

    # Create a connected subgraph K7
    k7_vertices = random.sample(range(num_vertices), 7)
    for i in k7_vertices:
        for j in k7_vertices:
            if i != j:
                graph.add_edge(i, j)
                num_edges -= 1

    # Distribute remaining edges randomly
    while num_edges > 0:
        u = random.randrange(num_vertices)
        v = random.randrange(num_vertices)
        if u != v and v not in graph.adj_list[u]:
            graph.add_edge(u, v)
            num_edges -= 1

    return graph


# Создаем разреженный граф с 12000 вершинами и средней степенью от 10 до 100
num_vertices = 500000
target_degree = random.randint(10, 100)
graph = create_sparse_graph(num_vertices, target_degree)

# Выбираем случайную стартовую вершину
start_vertex = random.randint(0, num_vertices - 1)

# Находим кратчайшие пути с помощью BFS
distances_bfs, iterations_bfs = graph.bfs_shortest_paths(start_vertex)

# Находим кратчайшие пути с помощью Dijkstra
distances_dijkstra, iterations_dijkstra = graph.dijkstra_shortest_paths(start_vertex)

#print("BFS кратчайшие пути:", distances_bfs)
print("Количество итераций BFS:", iterations_bfs)
#print("Dijkstra кратчайшие пути:", distances_dijkstra)
print("Количество итераций Dijkstra:", iterations_dijkstra)
