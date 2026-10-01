import sys


def position(forward, backward, steps):
    cycle_length = forward + backward
    complete_cycles, remaining = divmod(steps, cycle_length)
    distance = complete_cycles * (forward - backward)
    distance += min(remaining, forward)
    distance -= max(0, remaining - forward)
    return distance


a, b, c, d, steps = map(int, sys.stdin.buffer.read().split())
nikky = position(a, b, steps)
byron = position(c, d, steps)

if nikky > byron:
    print("Nikky")
elif byron > nikky:
    print("Byron")
else:
    print("Tied")
