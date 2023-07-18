r = (int(input()))
s = (int(input()))

total_num = r * 8 + s * 3
if total_num >= 28:
    print(total_num - 28)
else:
    print(0)