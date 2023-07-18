x, y = {}, {}

for const in (x, y):
    for _ in range(int(input())):
        s1, s2 = input().split()
        if s1 not in const:
            const[s1] = [s2]
        else:
            const[s1].append(s2)
            
v = 0
for _ in range(int(input())):
    g = set(input().split())
    for i in g:
        v += sum(1 for xi in x.get(i, []) if xi not in g) + \
            sum(1 for yi in y.get(i, []) if yi in g)
            
print(v)