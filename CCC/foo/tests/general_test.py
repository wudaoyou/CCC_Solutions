str = input()
count = 0
while str != "0":
    lst = list(map(int, str.split(" ")))
    len = lst[0]
    lst = lst[1:]
    for i in range(len-1):
        lst[i] = lst[i] - lst[i + 1]
    lst.pop(-1)
    for i in range(len-1):
        s = lst.pop(0)
        if s in lst:
            lst = list(map(lambda x: x != s, lst))
            count += 1
    print(count)
    count = 0
    str = input()
