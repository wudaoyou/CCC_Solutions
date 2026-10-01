def calcDays(p, n, r):
    count = 0;
    sum = n
    while sum <= p:
        n *= r
        sum += n
        count += 1
    return count


if __name__ == '__main__':
    print(calcDays(int(input()), int(input()), int(input())))
