a = int(input())
b = int(input())

count = 2

while a >= b:
    count += 1
    c = a - b
    a, b = b, c

print(count)