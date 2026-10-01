if __name__ == '__main__':
    num = int(input())
    s = input()
    count_a = 0
    count_b = 0

    for c in s:
        if c == 'A':
            count_a += 1
        elif c == 'B':
            count_b += 1

    if count_b > count_a:
        print('B')
    elif count_b < count_a:
        print('A')
    else:
        print('Tie')