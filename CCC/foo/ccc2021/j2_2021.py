if __name__ == '__main__':
    n = input()
    name = ''
    bit = 0
    for i in n:
        n = input()
        d = int(input())
        if d > bit:
            name = n
            bit = d
    print(name)
