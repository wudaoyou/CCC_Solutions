if __name__ == '__main__':
    n = int(input())
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

    for i in range(n):
        tpl = eval(input())
        if i == 0:
            x_min = tpl[0]
            x_max = tpl[0]
            y_min = tpl[1]
            y_max = tpl[1]
        if tpl[0] > x_max:
            x_max = tpl[0]
        elif tpl[0] < x_min:
            x_min = tpl[0]

        if tpl[1] > y_max:
            y_max = tpl[1]
        elif tpl[1] < y_min:
            y_min = tpl[1]

    print('%d,%d' % (x_min - 1, y_min - 1))
    print('%d,%d' % (x_max + 1, y_max + 1))
