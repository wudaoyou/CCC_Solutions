def rotate(lst):
    # this will rotate 90 degree clockwise
    n = len(lst)
    line = [None] * n
    new_lst = []
    for i in range(n):
        new_lst.append(line[:])
    col = 0
    for i in range(n - 1, -1, -1):
        x = lst[i]
        for row in range(n):
            new_lst[row][col] = x[row]
        col += 1

    # print(new_lst)
    return new_lst


if __name__ == '__main__':
    n = int(input())
    lst = []
    lst_max = []
    for i in range(n):
        line = [int(i) for i in input().split()]
        lst.append(line[:])
        lst_max.append(max(line))

    max_value = max(lst_max)
    current_row = lst_max.index(max_value)
    current_col = lst[current_row].index(max_value)
    # print(current_row)
    # print(current_col)

    while not (current_row == current_col == n - 1):
        lst = rotate(lst)
        for i in range(n):
            for j in range(n):
                if lst[i][j] == max_value:
                    current_row = i
                    current_col = j

    for row in lst:
        for c in row:
            print(c, end=' ')
        print()
