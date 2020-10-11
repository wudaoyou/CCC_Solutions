n = int(input())
r = 0
a = 5 if n > 5 else n
b = n - a
while a >= b:
    r += 1
    a -= 1
    b += 1
print(r)