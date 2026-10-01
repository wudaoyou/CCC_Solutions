import sys


read = sys.stdin.buffer.readline
j = int(read())
a = int(read())
sizes = {b"S": 1, b"M": 2, b"L": 3}
jerseys = bytearray(j + 1)
for number in range(1, j + 1):
    jerseys[number] = sizes[read().strip()]

satisfied = 0
for _ in range(a):
    size, number = read().split()
    number = int(number)
    if jerseys[number] >= sizes[size]:
        satisfied += 1
        jerseys[number] = 0
print(satisfied)
