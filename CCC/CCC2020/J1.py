def dog_treat(s, m, l):
    return 'happy' if (1 * s + 2 * m + 3 * l) >= 10 else 'sad'


if __name__ == '__main__':
    print(dog_treat(int(input()), int(input()), int(input())))
