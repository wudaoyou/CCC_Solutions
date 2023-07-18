n, i, p = int(input()), 0, 0

while i < n:
    a = int(input())
    b = int(input())
    rate = a * 5 - b * 3
    if rate > 40:
        p += 1
    i += 1
    
if p == n:
    print(str(p) + "+")
else:
    print(p)

    