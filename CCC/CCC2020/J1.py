def dogTreat(s, m, l):
    return 'happy' if (1 * s + 2 * m + 3 * l) >= 10 else 'sad'


if __name__ == '__main__':
    print(dogTreat(int(input()), int(input()), int(input())))
