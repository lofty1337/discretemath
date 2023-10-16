import random
from collections import deque


# Генерация простого связного разреженного неориентированного графа
def generate_random_graph(num_vertices, num_edges):
    graph = [[0] * num_vertices for _ in range(num_vertices)]

    vertices = list(range(num_vertices))

    while len(vertices) > 1:
        u = random.choice(vertices)
        vertices.remove(u)
        v = random.choice(vertices)

        graph[u][v] = 1
        graph[v][u] = 1

    while num_edges > 0:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)

        if u != v and graph[u][v] == 0:
            graph[u][v] = 1
            graph[v][u] = 1
            num_edges -= 1

    return graph


# Алгоритм Дейкстры для поиска кратчайших путей
def dijkstra(graph, source):
    num_vertices = len(graph)
    distances = [float("inf")] * num_vertices
    distances[source] = 0

    visited = [False] * num_vertices
    iterations = 0

    for _ in range(num_vertices):
        min_distance = float("inf")
        min_vertex = -1

        iterations += 1

        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_vertex = v

        visited[min_vertex] = True

        for v in range(num_vertices):
            if not visited[v] and graph[min_vertex][v] > 0:
                new_distance = distances[min_vertex] + graph[min_vertex][v]
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    iterations += 1

    print(f"Dijkstra iterations:{iterations}")
    return distances


# Алгоритм поиска в ширину (BFS) для поиска кратчайших путей
def bfs(graph, source):
    num_vertices = len(graph)
    distances = [float("inf")] * num_vertices
    distances[source] = 0

    queue = deque()
    queue.append(source)
    iterations = 0

    while queue:
        u = queue.popleft()

        for v in range(num_vertices):
            if graph[u][v] > 0 and distances[v] == float("inf"):
                distances[v] = distances[u] + 1
                queue.append(v)
                iterations += 1
    print(f"BFS iterations:{iterations}")
    return distances


# Пример использования
num_vertices = 32000
num_edges = 64000
graph = generate_random_graph(num_vertices, num_edges)

source_vertex = 13

# Алгоритм Дейкстры
distances_dijkstra = dijkstra(graph, source_vertex)

# Алгоритм BFS
distances_bfs = bfs(graph, source_vertex)



