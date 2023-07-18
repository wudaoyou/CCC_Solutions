player_list = (int(input()))*[4*[0]]
i, p = 0, 0
while i < len(player_list):
    player_list[i][1] = int(input())
    player_list[i][2] = int(input())
    player_list[i][3] = player_list[i][1] * 5 - player_list[i][2] * 3
    if player_list[i][3] > 40:
        p += 1
    i += 1
if p == len(player_list):
    print(str(p) + "+")
else:
    print(p)

    