a = int(input())
h = []
l = []
lst = list(map(int,input().split()))
lst = sorted(lst)
if len(lst)%2 ==0 :
    n = len(lst)//2
else:
    n = len(lst)//2+1
l = lst[:n]
h = lst[n:]
l = l[::-1]
s = []
for i in range(len(h)):
    s.append(l[i])
    s.append(h[i])

if len(l) > len(h):
    s.append(l[-1])

s = list(map(str, s))
print(" ".join(s))