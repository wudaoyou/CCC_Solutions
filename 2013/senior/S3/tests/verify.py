"""Compare every legal partial tournament with full-tournament DFS records."""

from itertools import combinations, product
from pathlib import Path
import runpy

count_championships = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / 'solution.py'))['count_championships']
pairs = list(combinations(range(1, 5), 2))
full = []


def enumerate_full(index, outcomes, points):
    if index == len(pairs):
        highest = max(points[1:])
        leaders = [team for team in range(1, 5) if points[team] == highest]
        full.append((tuple(outcomes), leaders[0] if len(leaders) == 1 else 0))
        return
    a, b = pairs[index]
    for outcome in range(3):
        if outcome == 0:
            points[a] += 3
        elif outcome == 1:
            points[b] += 3
        else:
            points[a] += 1
            points[b] += 1
        outcomes.append(outcome)
        enumerate_full(index + 1, outcomes, points)
        outcomes.pop()
        if outcome == 0:
            points[a] -= 3
        elif outcome == 1:
            points[b] -= 3
        else:
            points[a] -= 1
            points[b] -= 1


enumerate_full(0, [], [0] * 5)
assert len(full) == 729
checked = 0
for pattern in product((-1, 0, 1, 2), repeat=6):
    if -1 not in pattern:
        continue  # The statement requires at least one unplayed game.
    games = []
    for pair, result in zip(pairs, pattern):
        if result != -1:
            scores = ((5, 0), (0, 7), (2, 2))[result]
            games.append((*pair, *scores))
    expected = [0] * 5
    for outcomes, champion in full:
        if all(known == -1 or known == actual
               for known, actual in zip(pattern, outcomes)):
            expected[champion] += 1
    for favorite in range(1, 5):
        assert count_championships(favorite, games) == expected[favorite], (favorite, games)
        checked += 1
print(f'All {checked} partial-tournament/favorite combinations match full DFS enumeration.')
print('No games played:', [count_championships(team, []) for team in range(1, 5)])
