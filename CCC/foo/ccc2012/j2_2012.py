depth_list = []
for _ in range(4):
    depth_list.append(int(input()))

sec_list = set(depth_list)

asc_list = sorted(depth_list, reverse=False)
dsc_list = sorted(depth_list, reverse=True)
rev_list = depth_list[::-1]
if depth_list == rev_list:
    print('Fish At Constant Depth')
elif depth_list == asc_list and len(sec_list) == len(depth_list):
    print('Fish Rising')
elif depth_list == dsc_list and len(sec_list) == len(depth_list):
    print('Fish Diving')
else:
    print('No Fish')