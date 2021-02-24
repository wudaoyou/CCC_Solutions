lst = []


def cal_combination(count, pos):
    if count == 3:
        return 1
    elif pos >= len(lst):
        return 0
    else:
        choice1 = cal_combination(count + 1, pos + 1)
        choice2 = cal_combination(count, pos + 1)
        return choice1 + choice2


if __name__ == '__main__':
    n = int(input())
    lst = [i for i in range(1, n)]
    #print(lst)
    c = cal_combination(0, 0)
    print(c)
