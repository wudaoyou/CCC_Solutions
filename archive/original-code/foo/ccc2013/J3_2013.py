def max_chore(target, data, i):
    if target == 0:
        result = 0
    elif target < 0:
        result = 0
    elif i < 0:
        result = 0
    elif data[i] > target:
        result = max_chore(target, data, i - 1)
    else:
        num1 = 1+max_chore(target - data[i], data, i - 1)
        num2 = max_chore(target, data, i - 1)
        result = max(num1, num2)
    return result


if __name__ == "__main__":
    target = int(input())
    num = int(input())
    lst = []
    for i in range(num):
        lst.append(int(input()))

    n = max_chore(target, lst, len(lst) - 1)
    print(n)