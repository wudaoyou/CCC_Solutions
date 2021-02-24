data = {}


def give_pizza(n, k, min):
    time = 0
    if (n, k, min) in data:
        time = data[(n, k, min)]
    else:
        if n < min:
            time = 0
        elif n == k:
            time = 1
        elif k == 1:
            time = 1
        else:
            for i in range(min, n//k+1):
                time += give_pizza(n - i, k - 1, i)
        data[(n, k, min)] = time
    return time


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    result = give_pizza(n, k, 1)
    print(result)
