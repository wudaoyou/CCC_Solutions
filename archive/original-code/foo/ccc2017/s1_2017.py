j = int(input())
sw = [int(x) for x in input().split()]
sp = [int(x) for x in input().split()]
swtotal, sptotal, k = 0, 0, 0
for i in range(0, j):
    swtotal += sw[i]
    sptotal += sp[i]
    if swtotal == sptotal: k = i+1
print(k)