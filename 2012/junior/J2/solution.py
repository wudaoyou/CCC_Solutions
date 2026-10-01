import sys

a, b, c, d = map(int, sys.stdin.read().split())

if a < b < c < d:
    print("Fish Rising")
elif a > b > c > d:
    print("Fish Diving")
elif a == b == c == d:
    print("Fish At Constant Depth")
else:
    print("No Fish")
