
if __name__ == '__main__':

    w = 0
    for _ in range(6):
        w += 1 if input() == 'W' else 0

    if w >= 5:
        print(1)
    elif w >= 3:
        print(2)
    elif w >= 1:
        print(3)
    else:
        print(-1)
