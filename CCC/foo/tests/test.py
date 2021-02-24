a = int(input())
for i in range(a):
    b, c, d = list(map(int, input().split()))
    if d % c == 0 or d % b == 0:
        print("YES")
    elif (d % (b + c)) % c == 0 or (d % (b + c)) % b == 0:
        print("YES")
    else:
        print("NO")
