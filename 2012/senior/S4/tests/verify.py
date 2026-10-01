"""Independent tuple-stack BFS checks; no integer-encoding move rules."""

from collections import deque
from itertools import product
from pathlib import Path
import runpy

distances_from_goal = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / 'solution.py'))['distances_from_goal']


def neighbors(stacks):
    for position, stack in enumerate(stacks):
        if not stack:
            continue
        coin = stack[0]
        for adjacent in (position - 1, position + 1):
            if 0 <= adjacent < len(stacks):
                target = stacks[adjacent]
                if not target or coin < target[0]:
                    moved = list(stacks)
                    moved[position] = stack[1:]
                    moved[adjacent] = (coin,) + target
                    yield tuple(moved)


def oracle_distances(goal):
    distances = {goal: 0}
    queue = deque([goal])
    while queue:
        state = queue.popleft()
        for neighbor in neighbors(state):
            if neighbor not in distances:
                distances[neighbor] = distances[state] + 1
                queue.append(neighbor)
    return distances


def oracle_shortest(start, goal):
    if start == goal:
        return 0
    forward, backward = {start: 0}, {goal: 0}
    front, back = {start}, {goal}
    while front and back:
        if len(front) > len(back):
            front, back = back, front
            forward, backward = backward, forward
        following = set()
        best = None
        for state in front:
            for neighbor in neighbors(state):
                if neighbor not in forward:
                    forward[neighbor] = forward[state] + 1
                    following.add(neighbor)
                    if neighbor in backward:
                        distance = forward[neighbor] + backward[neighbor]
                        best = distance if best is None else min(best, distance)
        if best is not None:
            return best
        front = following
    return -1


for count in range(1, 6):
    goal = tuple((coin,) for coin in range(1, count + 1))
    oracle = oracle_distances(goal)
    actual = distances_from_goal(count)
    for positions in product(range(count), repeat=count):
        stacks = tuple(tuple(coin + 1 for coin, position in enumerate(positions)
                             if position == column)
                       for column in range(count))
        state = sum(position * count ** coin
                    for coin, position in enumerate(positions))
        assert actual[state] == oracle.get(stacks, -1), (count, stacks)
    print(f'n={count}: all {count ** count} arrangements match tuple-stack BFS.')

goal = tuple((coin,) for coin in range(1, 8))
start = goal[::-1]
expected = oracle_shortest(start, goal)
state = sum((6 - coin) * 7 ** coin for coin in range(7))
assert expected == 56
assert distances_from_goal(7)[state] == expected
print('n=7 reversed order: 56 moves, confirmed by tuple-stack bidirectional BFS.')
