import sys


def buildGraph(lst):
    graph = {}
    endPages = []
    for node, children in enumerate(lst, 1):
        del children[0]
        if not children:
            endPages.append(node)
        graph[node] = children
    return graph, endPages


if __name__ == '__main__':
    line = int(input())
    allPages = [n for n in range(1, line + 1)]
    lst = []
    for _ in range(line):
        lst.append(list(map(int, (input()).split())))

    gp, ends = buildGraph(lst)

    visited = []  # List to keep track of visited nodes.


    # Initialize a queue

    def bfs(visited, graph, node):
        queue = []
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            # print(s, end=" ")
            v = graph[s]

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        return 'Y' if sorted(visited) == allPages else 'N'


    def bfs_shortest_path(graph, start, goal):
        explored = []
        queue = [[start]]

        if start == goal:
            return start

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in explored:
                neighbours = graph[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == goal:
                        return new_path

                explored.append(node)
        return False


    print(bfs(visited, gp, 1))
    # print(sorted(visited))
    min = len(allPages)
    for p in ends:
        # print((bfs_shortest_path(gp, 1, p)))
        n = 1000000 if bfs_shortest_path(gp, 1, p) is False else len((bfs_shortest_path(gp, 1, p)))
        if n < min:
            min = n
    print(min)
