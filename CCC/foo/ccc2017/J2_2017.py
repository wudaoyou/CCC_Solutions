from sys import stdin


def shifty_sum(n, k):
    sum = n
    while k > 0:
        sum += n * (10 ** k)
        k -= 1
    return sum


if __name__ == '__main__':
    input = stdin.readline
    n = int(input())
    k = int(input())
    sum = shifty_sum(n, k)

    print(sum)
