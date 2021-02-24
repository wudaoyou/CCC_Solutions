if __name__ == '__main__':
    rows = ['*x*', ' xx', '* *']

    factor = int(input())
    for row in rows:
        for _ in range(factor):
            for c in row:
                s = c * factor
                print(s, end='')
            print()