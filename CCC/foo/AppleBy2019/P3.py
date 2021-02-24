if __name__ == '__main__':
    s = input()
    lst = s.split()
    lst = list(filter(lambda x: x != '(+', lst))
    lst = list(map(lambda x: x.strip().replace(')', ''), lst))
    lst = list(map(int, lst))
    print(sum(lst))
