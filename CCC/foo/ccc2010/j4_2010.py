def verify(a, b):
    count = 0
    if a == b:
        return True
    for i in b:
        if i == a[0]:
            count += 1
        else:
            return False
    return True


def findShortest(a, b):
    if verify(a, b):
        return len(a)
    elif len(b) == 0:
        return len(a)
    else:
        return findShortest(a + [b[0]], b[1:])


def processSeq(seq, idx):
    a = seq[:idx]
    b = seq[idx:]
    if len(a) >= len(b):
        return findShortest(a, b)
    else:
        b, c = b[:len(a)], b[len(a):]
        templen1 = findShortest(a, b)
        result = processSeq(seq[:templen1])


if __name__ == '__main__':
    while True:
        seq = list(map(int, input().split()))
        if seq[0] == 0:
            break
        n = seq[0]
        seq = seq[1:]
        for i in range(n - 1):
            seq[i] = int(seq[i + 1]) - int(seq[i])
        seq.pop(-1)

        firstNum = seq[0]
        nextNum = seq[1:].index(firstNum)
        len = n if nextNum == -1 else processSeq(seq, nextNum + 1)
        print(len)
