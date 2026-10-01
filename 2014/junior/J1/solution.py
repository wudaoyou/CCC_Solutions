import sys

a, b, c = map(int, sys.stdin.read().split())
total = a + b + c

if total != 180:
    print("Error")
elif a == b == c:
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Scalene")
