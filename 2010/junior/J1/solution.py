n = int(input())

ways = 0
for first_hand in range(1, 6):
    for second_hand in range(first_hand + 1):
        if first_hand + second_hand == n:
            ways += 1

print(ways)
