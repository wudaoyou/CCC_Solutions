from sys import stdin

if __name__ == '__main__':
    input = stdin.readline
    type = int(input())
    n = int(input())
    d = list(map(int, input().split()))
    p = list(map(int, input().split()))

    d.sort()
    p.sort()

    if type == 2:
        d.reverse()
    lst = [max(i, j) for i, j in zip(d, p)]
    print(sum(lst))
