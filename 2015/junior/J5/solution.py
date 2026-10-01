import sys


def count_ways(n, k):
    ways = [[0] * (k + 1) for _ in range(n + 1)]
    ways[0][0] = 1

    for total in range(1, n + 1):
        for people in range(1, min(total, k) + 1):
            ways[total][people] = ways[total - 1][people - 1] + ways[total - people][people]

    return ways[n][k]


if __name__ == "__main__":
    data = list(map(int, sys.stdin.buffer.read().split()))
    print(count_ways(*data))
