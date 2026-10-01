n = int(input())

graph = {}
for i in range(1, n + 1):
    graph[i] = []

while True:
    node_a, node_b = tuple(map(int, input().split()))
    if node_a == 0:
        break
    else:
        if node_a in graph:
            graph[node_a] += [node_b]

# print(graph)

visited = []


def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        visited.append(path)

    for node in graph[start]:
        dfs(graph, node, end, path)


dfs(graph, 1, n)
print(len(visited))
