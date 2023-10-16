import sys

def floyd_warshall(graph):
    num_vertices = len(graph)

    distances = [[sys.maxsize] * num_vertices for _ in range(num_vertices)]

    # Заполняем матрицу смежности начальными значениями
    for i in range(num_vertices):
        for j in range(num_vertices):
            distances[i][j] = graph[i][j]

    # Вычисляем кратчайшие пути
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances


def build_adjacency_matrix(edges):
    num_vertices = max(max(edge[0], edge[1]) for edge in edges) + 1

    adjacency_matrix = [[sys.maxsize] * num_vertices for _ in range(num_vertices)]

    # Инициализируем матрицу смежности бесконечностями
    for i in range(num_vertices):
        adjacency_matrix[i][i] = 0

    for edge in edges:
        start_vertex, end_vertex, weight = edge[0], edge[1], edge[2]
        adjacency_matrix[start_vertex][end_vertex] = weight
        adjacency_matrix[end_vertex][start_vertex] = weight

    return adjacency_matrix

def build_incidence_matrix(edges):
    # Находим количество вершин и ребер в графе
    num_vertices = max(max(edge[0], edge[1]) for edge in edges) + 1
    num_edges = len(edges)

    # Создаем пустую матрицу инцидентности
    incidence_matrix = [[0] * num_edges for _ in range(num_vertices)]

    # Заполняем матрицу инцидентности
    for i, edge in enumerate(edges):
        start_vertex, end_vertex, weight = edge[0], edge[1], edge[2]
        incidence_matrix[start_vertex][i] = weight
        incidence_matrix[end_vertex][i] = -weight

    return incidence_matrix

def convert_incidence_to_adjacency(incidence_matrix):
    num_vertices = len(incidence_matrix)
    num_edges = len(incidence_matrix[0])

    # Создаем пустую матрицу смежности
    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    # Проходим по каждому ребру в матрице инцидентности
    for j in range(num_edges):
        start_vertex = -1
        end_vertex = -1

        # Определяем начальную и конечную вершины для ребра
        for i in range(num_vertices):
            if incidence_matrix[i][j] > 0:
                start_vertex = i
            elif incidence_matrix[i][j] < 0:
                end_vertex = i

        # Заполняем матрицу смежности
        adjacency_matrix[start_vertex][end_vertex] = incidence_matrix[start_vertex][j]

    return adjacency_matrix


# Пример списка ребер с весами и его преобразование
edges = [(0, 1, 15), (0, 2, 12), (0, 5, 12), (1, 5, 14), (2, 0, 12), (2, 4, 13), (3, 0, 18),
         (3, 5, 11), (3, 6, 15), (3, 7, 16), (4, 3, 13), (4, 7, 13), (5, 1, 12), (5, 3, 15),
         (6, 1, 14), (6, 3, 12)]

incidence_matrix = build_incidence_matrix(edges)
adjacency_matrix = convert_incidence_to_adjacency(incidence_matrix)

# Вывод матрицы инцидентности
for row in incidence_matrix:
    print(row)
print("!!!")

num_vertices = len(adjacency_matrix)

# Вывод матрицы смежности
adjacency_matrix = build_adjacency_matrix(edges)
for row in adjacency_matrix:
    print(row)

# Находим кратчайшие пути для всех пар вершин
shortest_paths = floyd_warshall(adjacency_matrix)

# Вывод кратчайших путей
num_vertices = len(adjacency_matrix)
for i in range(num_vertices):
    print(shortest_paths[i])
