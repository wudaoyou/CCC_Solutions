if __name__ == '__main__':
    c = int(input())
    r = int(input())
    k = int(input())
    rowCount = 0
    colCount = 0
    choices = dict()
    for _ in range(k):
        choice = tuple(input().split(' '))
        if choice not in choices:
            choices[choice] = 1
        else:
            if choices[choice] == 1:
                choices[choice] = 0
            else:
                choices[choice] = 1
    print(choices)

    for key,value in choices.items():
        if key[0] == 'R':
            rowCount += value
        elif key[0] == 'C':
            colCount += value

    num = rowCount*r + colCount*c - rowCount*colCount*2
    print(num)