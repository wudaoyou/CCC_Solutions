if __name__ == '__main__':
    end = '99999'
    while True:
        num = input()
        if num != end:
            ins, num = sum((map(int, list(num[0:2])))), num[2:]
            if ins % 2 == 1:
                direction, num = 'left', num
            elif ins == 0:
                direction, num = direction, num
            else:
                direction, num = 'right', num
            print(direction, num)
        else:
            break
