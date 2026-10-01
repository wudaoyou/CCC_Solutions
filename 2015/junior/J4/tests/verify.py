from pathlib import Path
import random
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solution import solve


SOLUTION = Path(__file__).resolve().parents[1] / "solution.py"


def check(data, expected):
    result = subprocess.run(
        [sys.executable, str(SOLUTION)], input=data.encode(), capture_output=True, check=True
    )
    assert result.stdout.decode() == expected


check("3\nR 7\nW 4\nS 7\n", "7 4\n")
check("3\nR 7\nW 1\nS 7\n", "7 1\n")
check("4\nR 1\nR 2\nS 1\nS 2\n", "1 2\n2 2\n")
check("6\nR 4\nS 4\nR 4\nW 3\nS 4\nR 9\n", "4 4\n9 -1\n")


def expected_from_times(events):
    waits = {}
    pending = {}
    for kind, friend, time in events:
        if kind == "R":
            waits.setdefault(friend, 0)
            pending[friend] = time
        else:
            waits[friend] += time - pending.pop(friend)
    return "".join(
        f"{friend} {-1 if friend in pending else waits[friend]}\n"
        for friend in sorted(waits)
    )


for seed in range(100):
    rng = random.Random(seed)
    friends = rng.sample(range(1, 101), 5)
    events = []
    records = []
    pending = set()
    time = 0

    for i in range(rng.randint(4, 9)):
        explicit_one_second = i == 1 and seed % 4 == 0
        if i:
            gap = 1 if explicit_one_second else rng.randint(1, 5)
            if gap != 1 or explicit_one_second:
                records.append(("W", gap))
            time += gap

        can_receive = [friend for friend in friends if friend not in pending]
        can_reply = list(pending)
        if can_reply and (not can_receive or rng.random() < 0.45):
            friend = rng.choice(can_reply)
            records.append(("S", friend))
            pending.remove(friend)
            events.append(("S", friend, time))
        else:
            friend = rng.choice(can_receive)
            records.append(("R", friend))
            pending.add(friend)
            events.append(("R", friend, time))

    data = (str(len(records)) + "\n" + "".join(f"{kind} {value}\n" for kind, value in records)).encode()
    assert len(records) <= 20
    assert solve(data) == expected_from_times(events)

print("J4 small cases passed")
