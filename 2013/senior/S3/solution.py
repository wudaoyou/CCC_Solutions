from itertools import combinations, product


def count_championships(favorite, games):
    points = [0] * 5
    played = set()
    for a, b, score_a, score_b in games:
        played.add((a, b))
        if score_a > score_b:
            points[a] += 3
        elif score_b > score_a:
            points[b] += 3
        else:
            points[a] += 1
            points[b] += 1
    remaining = [pair for pair in combinations(range(1, 5), 2)
                 if pair not in played]
    answer = 0
    for outcomes in product(((3, 0), (0, 3), (1, 1)), repeat=len(remaining)):
        final = points.copy()
        for (a, b), (add_a, add_b) in zip(remaining, outcomes):
            final[a] += add_a
            final[b] += add_b
        if all(final[favorite] > final[team]
               for team in range(1, 5) if team != favorite):
            answer += 1
    return answer


if __name__ == '__main__':
    favorite = int(input())
    completed = int(input())
    games = [tuple(map(int, input().split())) for _ in range(completed)]
    print(count_championships(favorite, games))
