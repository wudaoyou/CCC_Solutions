def encodeLine(line):
    cList = []
    nums = []
    i = 0
    cList.append(line[0])
    nums.append(0)
    for c in line:
        if c == cList[i]:
            nums[i] += 1
        else:
            i += 1
            cList.insert(i, c)
            nums.insert(i, 1)

    return cList, nums


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        line = encodeLine(input())
        for i in range(len(line[0])):
            print(line[1][i], line[0][i], sep=' ', end=' ')
        print()
