antonia = david = 100

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < b:
        antonia -= b
    elif b < a:
        david -= a

print(antonia)
print(david)
