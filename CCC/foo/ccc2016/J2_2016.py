def checkTotal(matrix, num):
    for l in matrix:
        if num != sum(l):
            return False
    return True


def rotate(matrix):
    rotated = [list(r) for r in zip(*matrix[::-1])]
    return rotated


if __name__ == '__main__':
    matrix = []
    for _ in range(4):
        matrix.append(list(map(int, input().split())))
    num = sum(matrix[0])
    result = checkTotal(matrix, num) and checkTotal(rotate(matrix), num)
    print('magic' if result else 'not magic')
