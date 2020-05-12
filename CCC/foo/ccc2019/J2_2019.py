def printLine(code):
    print(code[1] * int(code[0]))


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        code = tuple(input().split())
        printLine(code)
