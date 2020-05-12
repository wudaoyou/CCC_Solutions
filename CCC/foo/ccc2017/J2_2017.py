from sys import stdin

if __name__ == '__main__':
    input = stdin.readline
    n = int(input())
    k = int(input())
    sum = n
    while k > 0:
        sum += n * (10 ** k)
        k -= 1

    print(sum)
