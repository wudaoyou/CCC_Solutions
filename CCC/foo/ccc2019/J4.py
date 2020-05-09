if __name__ == '__main__':
    s = input()
    a = 1
    b = 2
    c = 3
    d = 4
    for ch in s:
        if ch == 'H':

            a, c = c, a
            b, d = d, b

        elif ch == 'V':

            a, b = b, a
            c, d = d, c

    print(a, b)
    print(c, d)
