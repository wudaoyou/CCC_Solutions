p, c, f = int(input()), int(input()), 0

if p >= 0 and c >= 0:
    f = 50 * p - 10 * c
    if p > c:
        f += 500

print(f)