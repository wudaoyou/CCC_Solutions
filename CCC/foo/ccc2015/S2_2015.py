j = int(input())
a = int(input())

size = {'S': 1, 'M': 2, 'L': 3}
jersey = [0]

for i in range(j):
    jersey.append(size[input()])

athletes = [9 for _ in range(j+1)]
for i in range(a):
    s, n = input().split()
    n = int(n)
    athletes[n] = min(size[s], athletes[n])

count = 0
for i in range(1, j+1):
    if i <= len(jersey):
        if jersey[i] >= athletes[i]:
            count += 1
print(count)