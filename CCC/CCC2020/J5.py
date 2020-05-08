graph = {}
def isInRange(current, matrix):
    if current in graph:
        return graph[current]
    res = []
    val = matrix[current[0]][current[1]]
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[1])):
            if row * col == val:
                res.append((row, col))
    return res


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    lst = []
    lst.append([-1, -1, -1])
    for _ in range(m):
        lst.append(list(map(int, ('-1 ' + input()).split())))

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            graph[(i, j)] = isInRange((i, j), lst)
    # print(graph)

    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue

    def bfs(visited, graph, node):
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            # print(s, end=" ")
            if (m, n) == s:
                return 'yes'

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return 'no'


    res = bfs(visited, graph, (1, 1))
    print(res)
