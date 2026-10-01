from array import array
from collections import deque
import sys


def distances_from_goal(count):
    powers = [count ** coin for coin in range(count)]
    goal = sum(coin * powers[coin] for coin in range(count))
    distances = array('i', [-1]) * (count ** count)
    distances[goal] = 0
    queue = deque([goal])
    while queue:
        state = queue.popleft()
        top = [count] * count
        remaining = state
        # Coin 0 is the smallest; each base-count digit stores its position.
        for coin in range(count):
            remaining, position = divmod(remaining, count)
            if top[position] == count:
                top[position] = coin
        steps = distances[state] + 1
        for position in range(count - 1):
            left, right = top[position], top[position + 1]
            if left < right:
                neighbor = state + powers[left]
            elif right < left:
                neighbor = state - powers[right]
            else:
                continue
            if distances[neighbor] == -1:
                distances[neighbor] = steps
                queue.append(neighbor)
    return distances


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    tables = {}
    for count in numbers:
        if count == 0:
            break
        order = [next(numbers) for _ in range(count)]
        if count not in tables:
            tables[count] = distances_from_goal(count)
        state = sum(position * count ** (coin - 1)
                    for position, coin in enumerate(order))
        distance = tables[count][state]
        print('IMPOSSIBLE' if distance == -1 else distance)


if __name__ == '__main__':
    main()
