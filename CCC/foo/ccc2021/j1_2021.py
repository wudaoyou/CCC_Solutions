def eval(p):
    return 5*p-400
if __name__ == '__main__':
    kpa = eval(int(input()))
    print(kpa)
    if kpa <100:
        print(1)
    elif kpa > 100:
        print(-1)
    else:
        print(0)