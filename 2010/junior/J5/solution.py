from collections import deque
import sys


MOVES = ((-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1))


def minimum_moves(start_x, start_y, goal_x, goal_y):
    start = (start_x - 1, start_y - 1)
    goal = (goal_x - 1, goal_y - 1)
    distance = [[-1] * 8 for _ in range(8)]
    distance[start[0]][start[1]] = 0
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            return distance[x][y]

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))


def main():
    start_x, start_y, goal_x, goal_y = map(int, sys.stdin.buffer.read().split())
    print(minimum_moves(start_x, start_y, goal_x, goal_y))


if __name__ == "__main__":
    main()
