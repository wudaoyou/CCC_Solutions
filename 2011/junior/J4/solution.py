import sys

DIRECTIONS = {"d": (0, -1), "u": (0, 1), "l": (-1, 0), "r": (1, 0)}
BASE_COMMANDS = (("d", 2), ("r", 3), ("d", 2), ("r", 2), ("u", 2),
                 ("r", 2), ("d", 4), ("l", 8), ("u", 2))


def main():
    data = sys.stdin.read().split()
    x, y = 0, -1
    visited = {(x, y)}

    for direction, length in BASE_COMMANDS:
        dx, dy = DIRECTIONS[direction]
        for _ in range(length):
            x += dx
            y += dy
            visited.add((x, y))

    for i in range(0, len(data), 2):
        direction = data[i]
        length = int(data[i + 1])
        if direction == "q":
            break

        dx, dy = DIRECTIONS[direction]
        danger = False
        for _ in range(length):
            x += dx
            y += dy
            point = (x, y)
            if point in visited:
                danger = True
            visited.add(point)

        print(x, y, "DANGER" if danger else "safe")
        if danger:
            break


if __name__ == "__main__":
    main()
