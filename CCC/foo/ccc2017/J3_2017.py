from sys import stdin

if __name__ == '__main__':
    input = stdin.readline
    (a, b) = tuple(map(int, input().split()))
    (c, d) = tuple(map(int, input().split()))
    t = int(input())
    dis = abs(a - c) + abs(b - d)
    if dis <= t and not (t - dis) % 2:
        print('Y')
    else:
        print('N')
