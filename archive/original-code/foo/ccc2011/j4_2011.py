upper = -1
lower = -200
left = -1 - 200
right = -1 + 200
end = False
start = [-5, -1]
pos = start
current_tunnel = [(-1, 0), (-2, 0), (-3, 0), (-3, 1), (-3, 2), (-3, 3), (-3, 5), (-3, 6), (-3, 7), (-4, 3), (-4, 5),
                  (-4, 7), (-5, -1), (-5, 3), (-5, 4), (-5, 5), (-5, 7), (-6, -1), (-6, 7), (-7, -1), (-7, 0), (-7, 1),
                  (-7, 2), (-7, 3), (-7, 4), (-7, 5), (-7, 6), (-7, 7)]


def move(pos, direction, step, a):
    t = ' safe'
    for i in range(step):
        if direction == '+':
            pos[a] += 1
        else:
            pos[a] -= 1

        if tuple(pos) in current_tunnel:
            t = ' DANGER'
        current_tunnel.append(tuple(pos))

    if pos[0] > upper or pos[0] < lower or pos[1] > right or pos[1] < left:
        t = ' DANGER'

    return " ".join(str(x) for x in reversed(pos)) + t


if __name__ == '__main__':
    while not end:
        action, step = input().split()
        step = int(step)
        if action == 'q':
            end = True
            continue
        else:
            if action == 'l':
                text = move(pos, '-', step, 1)
            elif action == 'r':
                text = move(pos, '+', step, 1)
            elif action == 'd':
                text = move(pos, '-', step, 0)
            elif action == 'u':
                text = move(pos, '+', step, 0)

        if 'DANGER' in text:
            print(text)
            end = True
        else:
            print(text)