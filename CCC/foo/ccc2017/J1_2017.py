from sys import stdin


def checkQuadrant(p):
    if p[0] > 0:
        if p[1] > 0:
            return 1
        else:
            return 4
    else:
        if p[1] > 0:
            return 2
        else:
            return 3


if __name__ == '__main__':
    input = stdin.readline
    a = int(input())
    b = int(input())
    print(checkQuadrant((a, b)))
