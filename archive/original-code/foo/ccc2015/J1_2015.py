if __name__ == '__main__':
    mon = int(input())
    day = int(input())
    if mon < 2:
        print('Before')
    elif mon > 2:
        print('After')
    else:
        if day < 18:
            print('Before')
        elif day > 18:
            print('After')
        else:
            print('Special')
