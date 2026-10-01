"""Enumerate small assignments; compare against disjoint two-person groups."""

from itertools import permutations
from pathlib import Path
import subprocess
import sys


solution = Path(__file__).resolve().parents[1] / "solution.py"
cases = 0
for n in range(2, 6):
    names = ["A", "a", "B", "b", "C"][:n]
    for assigned in permutations(names):
        groups = {frozenset(pair) for pair in zip(names, assigned)}
        good = all(len(group) == 2 for group in groups) and len(groups) * 2 == n
        data = f"{n}\n{' '.join(names)}\n{' '.join(assigned)}\n"
        result = subprocess.run([sys.executable, "-I", str(solution)], input=data,
                                text=True, capture_output=True, check=True)
        assert result.stdout.strip() == ("good" if good else "bad"), (names, assigned)
        cases += 1
print(f"S2: {cases} independent small cases passed")
