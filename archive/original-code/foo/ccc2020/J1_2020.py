import sys


def dogTreat(s, m, l):
    return 'happy' if (1 * s + 2 * m + 3 * l) >= 10 else 'sad'


if __name__ == '__main__':
    s = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    l = int(sys.stdin.readline())
    print(dogTreat(s, m, l))
