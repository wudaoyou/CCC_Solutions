import sys

passedPath = []


def isInRange(current, matrix):
    res = []
    val = matrix[current[0]][current[1]]
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[1])):
            if row * col == val:
                res.append((row, col))
    return res


def findPath(current, target, matrix):
    passedPath.append(current)
    if matrix[current[0]][current[1]] == target[0] * target[1]:
        return True
    else:
        currentPath = isInRange(current, matrix)
        if not currentPath:
            return False
        else:
            for a, b in currentPath:
                passedPath.append((a, b))
                if (a, b) in passedPath:
                    return findPath((a, b), target, matrix)


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    lst = []
    lst.append([-1, -1, -1])
    for _ in range(m):
        lst.append(list(map(int, ('-1 ' + input()).split())))

    # print(lst)
    result = findPath((1, 1), (m, n), lst)
    print("yes" if result else "no")
