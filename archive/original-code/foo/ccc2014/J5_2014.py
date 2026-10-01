def find_pair(l1, l2):
    for i in range(len(l1)):
        c1 = l1[i]
        c2 = l2[i]
        idx = l2.index(c1)
        c3 = l1[idx]
        if c2 != c3 or i == idx:
            return 'bad'
    return 'good'


if __name__ == "__main__":
    num = int(input())
    l1 = input().split()
    l2 = input().split()

    if num % 2 == 0:
        print(find_pair(l1, l2))

    else:
        print('bad')
