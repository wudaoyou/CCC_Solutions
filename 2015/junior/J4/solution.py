import sys


def solve(data):
    tokens = data.split()
    if not tokens:
        return ""

    count = int(tokens[0])
    now = 0
    have_message = False
    next_gap = 1
    waits = {}
    pending = {}

    for i in range(count):
        kind = tokens[1 + 2 * i]
        friend = int(tokens[2 + 2 * i])
        if kind == b"W":
            next_gap = friend
            continue

        if have_message:
            now += next_gap
        have_message = True
        next_gap = 1

        if kind == b"R":
            waits.setdefault(friend, 0)
            pending[friend] = now
        else:
            waits[friend] += now - pending.pop(friend)

    return "".join(
        f"{friend} {-1 if friend in pending else waits[friend]}\n"
        for friend in sorted(waits)
    )


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.buffer.read()))
