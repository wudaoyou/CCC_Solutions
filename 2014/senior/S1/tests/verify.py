"""Check small removal sequences using deletion from right to left."""

from itertools import product
from pathlib import Path
import subprocess
import sys


solution = Path(__file__).resolve().parents[1] / "solution.py"
cases = 0
for k in range(1, 9):
    for length in range(1, 4):
        for rounds in product(range(2, 5), repeat=length):
            expected = list(range(1, k + 1))
            for r in rounds:
                for position in range(len(expected) // r * r, 0, -r):
                    del expected[position - 1]
            data = "\n".join(map(str, (k, length, *rounds))) + "\n"
            result = subprocess.run([sys.executable, "-I", str(solution)], input=data,
                                    text=True, capture_output=True, check=True)
            actual = list(map(int, result.stdout.split()))
            assert actual == expected, (k, rounds, expected, actual)
            cases += 1
print(f"S1: {cases} independent small cases passed")
