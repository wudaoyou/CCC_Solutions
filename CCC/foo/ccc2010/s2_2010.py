h = {}
n = int(input())
for i in range(n):
    y = input().split()
    h[y[1]] = y[0]

code = ''
text = ''
in_code = input()
for c in in_code:
    code += c
    if code in h:
        text += h[code]
        code = ''
print(text)