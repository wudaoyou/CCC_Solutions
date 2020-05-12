def checkCyclic(t, s):
    lst = []
    for i in range(len(s)):
        s = s[1: len(s)] + s[0]
        if s not in lst:
            lst.append(s)
            if s in t:
                return 'yes'
    return 'no'


if __name__ == '__main__':
    t = input()
    s = input()
    print(checkCyclic(t, s))
