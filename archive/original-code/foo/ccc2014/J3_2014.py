if __name__ == '__main__':
    num = int(input())
    David = 100
    Antonia = 100

    for i in range(num):
        lst = list(map(int, input().split()))
        if lst[0] < lst[1]:
            Antonia -= lst[1]
        elif lst[0] > lst[1]:
            David -= lst[0]
    print(Antonia)
    print(David)
