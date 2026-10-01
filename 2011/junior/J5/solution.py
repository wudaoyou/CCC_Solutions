from math import prod
import sys


def ways(person, children):
    return 1 + prod(ways(child, children) for child in children[person])


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    children = [[] for _ in range(n + 1)]
    for person, parent in enumerate(data[1:], 1):
        children[parent].append(person)

    print(prod(ways(child, children) for child in children[n]))


if __name__ == "__main__":
    main()
