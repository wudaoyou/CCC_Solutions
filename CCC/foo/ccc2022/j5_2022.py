def sort_trees(c):
    return list(sorted(c, key=lambda c: abs(c[0] - c[1]), reverse=True))

n = int(input())
trees = []

for _ in range(int(input())):
    trees.append(tuple(map(int, input().split())))
    
trees += [(0,0), (n-1, n+1)]

all_x, all_y = set(), set()
for x1,y1 in trees:
    for x2, y2 in trees:
        if x1 != x2:
            all_x.add(tuple(sorted((x1, x2))))
        if y1 != y2:
            all_y.add(tuple(sorted((y1, y2))))

trees = trees[:-2]
all_x, all_y = sort_trees(all_x), sort_trees(all_y)

total = []
for i in range(2):
    trees = sorted(trees, key=lambda x: x[i])
    for s1, e1 in all_x if i else all_y:
        s2, e2 = 0, abs(s1 - e1)
        for tree in trees:
            if i and s1 < tree[0] < e1 and s2 < tree[1] < e2:
                e2 += abs(tree[1] - s2) + 1
                s2 = tree[1] + 1
            elif not i and s1 < tree[1] < e1 and s2 < tree[0] < e2:
                e2 += abs(tree[0] - s2) + 1
                s2 = tree[0] + 1
                
            if e2 > n + 1:
                break
        else:
            total.append(abs(s1 - e1) - 1)
            break
        
print(max(total))
                
                
                
                
                
                
                
                