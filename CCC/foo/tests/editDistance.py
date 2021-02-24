op = list(input())
s = list(input())
lst = []


def delete(s, i):
    s_copy = s[::]
    del s_copy[i]
    lst.append(''.join(s_copy))


def replace(s, i, c):
    s_copy = s[::]
    if (c != s_copy[i]):
        s_copy[i] = c
        lst.append(''.join(s_copy))


def adding(s, i, c):
    s_copy = s[::]
    s_copy.insert(i, c)
    lst.append(''.join(s_copy))


if __name__ == '__main__':
    for i in range(len(s)):
        delete(s, i)
        for c in op:
            replace(s, i, c)
            adding(s, i, c)
            adding(s, len(s), c)

    lst = sorted(set(lst))
    for item in lst:
        print(item)

    lst = ['aaa', '-67', 'ccc']
    lst = list(filter(lambda a: a.isdecimal(), lst))
    print(lst)