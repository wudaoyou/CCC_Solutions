lst = []
data = {}


def cal_combination(count, pos):
    if (count, pos) in data.keys():
        return data[(count, pos)]
    else:
        if count == 3:
            result = 1
        elif pos >= len(lst):
            result = 0
        else:
            choice1 = cal_combination(count + 1, pos + 1)
            choice2 = cal_combination(count, pos + 1)
            result = choice1 + choice2
        data[count, pos] = result
        return result


if __name__ == '__main__':
    n = int(input())
    lst = [i for i in range(1, n)]
    # print(lst)
    c = cal_combination(0, 0)
    print(c)