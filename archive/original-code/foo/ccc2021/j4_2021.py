def eval_list_s(lst, left, right, time=0):
    if left >= right:
        return lst, time
    else:
        if lst[left] == 'L':
            return eval_list_s(lst, left + 1, right, time)
        elif lst[right] == 'S':
            return eval_list_s(lst, left, right - 1, time)
        elif lst[left] == 'S':
            lst[right], lst[left] = lst[left], lst[right]
            return eval_list_s(lst, left + 1, right - 1, time + 1)
        else:
            return eval_list_s(lst, left + 1, right, time)


def eval_list_m(lst, left, right, time=0):
    if left >= right:
        return lst, time
    else:
        if lst[left] == 'L':
            return eval_list_m(lst, left + 1, right, time)
        elif lst[right] == 'S':
            return eval_list_m(lst, left, right - 1, time)
        elif lst[left] == 'M':
            if lst[right] == 'L':
                lst[right], lst[left] = lst[left], lst[right]
                return eval_list_m(lst, left + 1, right - 1, time + 1)
            else:
                return eval_list_m(lst, left, right - 1, time)


if __name__ == '__main__':
    lst = list(input())
    if 'M' in lst:
        lst, t = eval_list_s(lst, 0, len(lst) - 1)
        # print(lst)
        # print(t)
        lst, t = eval_list_m(lst, 0, len(lst) - 1, t)
    else:
        lst, t = eval_list_s(lst, 0, len(lst) - 1)
    # print(lst)
    print(t)
