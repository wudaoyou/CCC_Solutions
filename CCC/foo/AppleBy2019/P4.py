
def getArea(rectangle):
    if is axis aligned:
        return real are
    else
        0
def eval(rectangle, points, pos):
    if len(rectangle)==4:
        return getArea(rectangle)
    elif pos >= len(points):
        return 0
    else:
        result1 = eval(rectangle.append(points[pos]), points,pos+1)
        result2 = eval(rectangle, points,pos+1)
        return max(result1,result2)


if __name__ == '__main__':
    n = int(input())
    points= []
    for _ in range(n):
        points.append(tuple(map(int, input().split())))

    print(points)