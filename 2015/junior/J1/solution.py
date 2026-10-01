import sys

month, day = map(int, sys.stdin.read().split())

if month < 2 or (month == 2 and day < 18):
    print("Before")
elif month == 2 and day == 18:
    print("Special")
else:
    print("After")
