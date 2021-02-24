if __name__ == '__main__':
    n = int(input())
    name = ''
    bid = 0
    for i in range(n):
        n, d = input(), int(input())
        if d > bid:
            name, bid = n, d
    print(name)
