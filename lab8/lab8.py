import random
from collections import deque

def bfs(graph, residual_capacity, source, sink, parent):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(source)
    visited[source] = True
    all_vertices_visited = False  # Переменная для отслеживания пройденных вершин

    while queue and not all_vertices_visited:  # Условие остановки цикла
        u = queue.popleft()
        for v in range(len(graph)):
            if not visited[v] and residual_capacity[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u

                if v == sink:
                    min_cut_vertices = []
                    x = v
                    while x != source:
                        min_cut_vertices.append(x)
                        x = parent[x]
                    min_cut_vertices.append(source)
                    return min_cut_vertices

        # Проверяем, пройдены ли все доступные вершины
        all_vertices_visited = True
        for v in range(len(graph)):
            if not visited[v]:
                all_vertices_visited = False
                break

    return []

def find_min_cut(graph, residual_capacity, source, sink, parent):
    min_cut_vertices = []
    visited = [False] * len(graph)
    queue = deque()
    queue.append(source)
    visited[source] = True

    # Обход графа для нахождения вершин в минимальном разрезе
    while queue:
        u = queue.popleft()
        for v in range(len(graph)):
            # Добавляем вершину в минимальный разрез, если она не посещена и нет дополнительной пропускной способности в остаточной сети
            if not visited[v] and residual_capacity[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u

    # Формируем список вершин в минимальном разрезе
    x = sink
    while x != source:
        min_cut_vertices.append(x)
        x = parent[x]
    min_cut_vertices.append(source)

    return min_cut_vertices

def edmonds_karp(graph, source, sink):
    # Создаем остаточную сеть и заполняем ее пропускными способностями
    residual_capacity = [[0] * len(graph) for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            residual_capacity[i][j] = graph[i][j]

    max_flow = 0  # Максимальный поток

    # Инициализируем родительский массив
    parent = [-1] * len(graph)

    # Пока существует увеличивающий путь от истока к стоку
    while bfs(graph, residual_capacity, source, sink, parent):
        path_flow = float('inf')  # Минимальная пропускная способность ребер на пути

        # Находим минимальную пропускную способность ребер на пути
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_capacity[u][v])
            v = parent[v]

        # Обновляем остаточные емкости ребер и обратных ребер на пути
        v = sink
        while v != source:
            u = parent[v]
            residual_capacity[u][v] -= path_flow
            residual_capacity[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow
    min_cut_vertices = bfs(graph, residual_capacity, source, sink, parent)
    vertices_in_A = set(min_cut_vertices)
    vertices_in_B = set(range(len(graph))) - vertices_in_A

    min_cut = find_min_cut(graph, residual_capacity, source, sink, parent)
    print("Минимальный разрез:", min_cut)
    return max_flow


# Пример использования

graph = [
    [0, 5, 9, 0, 0, 0, 0, 0, 4],#A
    [0, 0, 2, 0, 0, 0, 2, 0, 2],#B
    [0, 0, 0, 0, 0, 0, 0, 0, 0],#C
    [0, 0, 2, 0, 0, 0, 0, 0, 0],#D
    [0, 0, 0, 7, 0, 0, 0, 0, 0],#E
    [0, 0, 2, 7, 7, 0, 0, 0, 0],#F
    [0, 0, 7, 3, 3, 3, 0, 0, 0],#G
    [0, 0, 7, 0, 0, 7, 7, 0, 0],#H
    [0, 0, 4, 0, 0, 0, 2, 7, 0] #I
]   #A  B  C  D  E  F  G  H  I

source = 0  # Исток
sink = 2  # Сток

max_flow = edmonds_karp(graph, source, sink)
print("Максимальный поток:", max_flow)

# Генерация случайных пропускных способностей дуг в диапазоне (100, 1000)
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] > 0:
            graph[i][j] = random.randint(100, 1000)

max_flow = edmonds_karp(graph, source, sink)
print("Максимальный поток:", max_flow)
