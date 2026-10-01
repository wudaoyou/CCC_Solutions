import sys


first, second = map(int, sys.stdin.read().split())
length = 2

while first >= second:
    next_term = first - second
    first, second = second, next_term
    length += 1

print(length)
