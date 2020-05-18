rush1 = [i for i in range(7 * 60 + 1, 10 * 60 + 1)]
rush2 = [i for i in range(15 * 60 + 1, 19 * 60 + 1)]


def getTime(t):
    distance = 120.0
    while distance > 0:
        t += 1
        if (t in rush1) or (t in rush2):
            distance -= 0.5
        else:
            distance -= 1
    return t


if __name__ == '__main__':
    hour, minute = tuple(map(int, input().split(':')))
    time = hour * 60 + minute
    time = getTime(time)
    hour = time // 60 if time // 60 < 24 else time // 60 - 24
    minute = time % 60
    print('%02d:%02d' % (hour, minute))
