def getScore(team):
    return 3 * team[0] + 2 * team[1] + team[2]


def compareScore(team_a, team_b):
    a = getScore(team_a)
    b = getScore(team_b)
    if a > b:
        return 'A'
    elif b > a:
        return 'B'
    else:
        return 'T'


if __name__ == '__main__':
    team_a = []
    team_b = []
    for _ in range(3):
        team_a.append(int(input()))

    for _ in range(3):
        team_b.append(int(input()))

    print(compareScore(team_a,team_b))
