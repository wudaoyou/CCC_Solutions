def check_grid(d, n):
    for k, v in d.items():
        if v == 'o' and k[0] < n:
            value_below = data[k[0] + 1, k[1]]
            if value_below == '.':
                data[k], data[k[0] + 1, k[1]] = data[k[0] + 1, k[1]], data[k]


if __name__ == '__main__':
    n, m = map(int, input().split())
    data = {}
    for i in range(1, n + 1):
        line = input()
        for j in range(1, m + 1):
            data[i, j] = line[j - 1]
    for _ in range(100):
        check_grid(data, n)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(data[i, j], end='')
        print()
