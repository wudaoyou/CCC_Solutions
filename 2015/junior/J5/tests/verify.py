from pathlib import Path
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solution import count_ways


def enumerate_allocations(total, people, smallest=1):
    if people == 0:
        return int(total == 0)
    return sum(
        enumerate_allocations(total - first, people - 1, first)
        for first in range(smallest, total // people + 1)
    )


for total in range(1, 19):
    for people in range(1, total + 1):
        assert count_ways(total, people) == enumerate_allocations(total, people)


solution = Path(__file__).resolve().parents[1] / "solution.py"
for data, expected in [("8\n4\n", "5\n"), ("6\n2\n", "3\n"), ("9\n9\n", "1\n")]:
    result = subprocess.run(
        [sys.executable, str(solution)], input=data.encode(), capture_output=True, check=True
    )
    assert result.stdout.decode() == expected

print("J5 small allocation oracle and samples passed")
