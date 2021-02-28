import sys

def calculate_area(a, b, h):
    return (a + b) * h / 2


if __name__ == '__main__':
    input = sys.stdin.readline
    k = int(input())
    abs = list(map(int, input().split()))
    hs = list(map(int, input().split()))
    area = 0
    for _ in range(k):
        a, b, h = abs[0], abs[1], hs[0]
        area += calculate_area(a, b, h)
        abs.pop(0)
        hs.pop(0)
    print(area)
