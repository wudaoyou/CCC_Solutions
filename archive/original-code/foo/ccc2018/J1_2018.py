from sys import stdin


def checkNumber(lst):
    if lst[0] == 8 or lst[0] == 9:
        if lst[1] == lst[2]:
            if lst[3] == 9 or lst[3] == 8:
                return 'ignore'
    return 'answer'


if __name__ == '__main__':
    input = stdin.readline
    lst = []
    for _ in range(4):
        lst.append(int(input()))
    print(checkNumber(lst))
