import string

tune, l, s = input(), [], ""
alph = list(string.ascii_uppercase)

for i,j in enumerate(tune[:-1]):
    if j not in alph and tune[i+1] in alph:
        s += j
        l.append(s)
        s = ""
    else:
        s += j

s += tune[-1]
l.append(s)
for i in l:
    if "+" in i:
        i = i.split("+")
        print(i[0], "tighten", i[1])
    elif "-" in i:
        i = i.split("-")
        print(i[0], "loosen", i[1])