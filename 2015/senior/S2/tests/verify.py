"""Compare the greedy count against all subsets of small request lists."""

from itertools import combinations, product
from pathlib import Path
from random import Random
import subprocess
import sys


def optimum(jerseys, requests):
    acceptable = {"S": "SML", "M": "ML", "L": "L"}
    for count in range(len(requests), -1, -1):
        for chosen in combinations(requests, count):
            numbers = {number for size, number in chosen}
            if len(numbers) == count and all(
                jerseys[number - 1] in acceptable[size] for size, number in chosen
            ):
                return count


solution = Path(__file__).resolve().parents[1] / "solution.py"
cases = []
for jersey in "SML":
    for length in range(1, 4):
        for sizes in product("SML", repeat=length):
            cases.append(([jersey], [(size, 1) for size in sizes]))

rng = Random(2015)
for _ in range(100):
    jerseys = [rng.choice("SML") for _ in range(rng.randint(2, 5))]
    requests = [(rng.choice("SML"), rng.randint(1, len(jerseys)))
                for _ in range(rng.randint(1, 7))]
    cases.append((jerseys, requests))

for jerseys, requests in cases:
    lines = [str(len(jerseys)), str(len(requests)), *jerseys]
    lines.extend(f"{size} {number}" for size, number in requests)
    result = subprocess.run([sys.executable, "-I", str(solution)],
                            input="\n".join(lines) + "\n", text=True,
                            capture_output=True, check=True)
    expected = optimum(jerseys, requests)
    assert int(result.stdout) == expected, (jerseys, requests, expected, result.stdout)
print(f"S2: {len(cases)} independent small cases passed")
