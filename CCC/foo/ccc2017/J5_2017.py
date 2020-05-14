from sys import stdin

dp = [0] * 4002
ma = [0] * 2001


def nailedIt(lst):
    for i in lst:
        ma[i] += 1

    for x in range(1, 2001):
        for y in range(x, 2001):
            if x == y:
                dp[x + y] += ma[x] / 2
            else:
                dp[x + y] += min(ma[x], ma[y])
    mh = 0
    for i in dp:
        if i > mh:
            mh = i

    ff = 0
    for i in dp:
        if i == mh:
            ff += 1

    print(int(mh), ff)


if __name__ == '__main__':
    input = stdin.readline
    n = int(input())
    lst = list(map(int, input().split()))
    nailedIt(lst)
