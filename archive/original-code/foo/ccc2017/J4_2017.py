import operator


def isValidTime(n):
    lst = list(map(int, [char for char in n]))
    lst = list(map(operator.sub, lst[1:], lst[:-1]))
    if len(set(lst)) == 1:
        return 1
    return 0


def getTimeString(t):
    a = str(12 if (12 + t // 60) % 12 == 0 else (12 + t // 60) % 12)
    b = str(t % 60) if t % 60 > 9 else ('0' + str(t % 60))
    return a + b


def getValidCount(n):
    count = 0
    for i in range(n + 1):
        time = getTimeString(i)
        count += isValidTime(time)
    return count


if __name__ == '__main__':
    t = int(input())
    all = getValidCount(720)
    f = t // 720
    t = t % 720
    print(getValidCount(t) + all * f)
