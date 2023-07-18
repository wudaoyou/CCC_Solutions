tune, a, i = input(), "", ""

for i in tune:
    if i == "+":
        a = a + " tighten "
    elif i == "-":
        a = a + " loosen "
    elif i.isnumeric():
        a = a + i + "\n"
    else:
        a += i
        
print(a)