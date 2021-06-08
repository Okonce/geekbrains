'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
 по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''

def adj_matrix_function(vertex):
    adj_matrix = {}
    for i in range(vertex):
        adj_matrix[i] = tuple(j for j in range(vertex) if j != i)
    return adj_matrix

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

vertex = int(input('Введите количество вершин: '))
node = int(input('Введите начальную вершину: '))

graph = adj_matrix_function(vertex)
visited = dfs(graph, node, [])
print(visited)
