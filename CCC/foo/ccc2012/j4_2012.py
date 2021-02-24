alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
k = int(input())
s = input()
rs = ''
for i in range(len(s)):
    c = s[i]
    p = alphabet.index(c)
    S = 3 * (i + 1) + k
    print(alphabet[p-S], end='')