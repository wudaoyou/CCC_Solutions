line1 = list(input())
line2 = list(input())

dict1 = {}
for char in line1:
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1

dict2 = {}
for char in line2:
    if char in dict2:
        dict2[char] += 1
    else:
        dict2[char] = 1

res = ""

for key in dict2:
    if key == "*":
        continue
    else:
        if key not in dict1:
            res = "N"
            break
        elif dict1[key] < dict2[key]:
            res = "N"
            break

if res == "":
    print("A")
else:
    print("N")