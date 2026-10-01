"""Check every allowed jersey number by directly enumerating triples."""

from itertools import combinations
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).resolve().parents[1] / 'solution.py'
for jersey in range(1, 100):
    expected = sum(1 for _ in combinations(range(1, jersey), 3))
    result = subprocess.run([sys.executable, '-I', str(solution)],
                            input=f'{jersey}\n', text=True,
                            capture_output=True, check=True)
    assert result.stdout.strip() == str(expected), jersey
print('All 99 jersey numbers match direct triple enumeration.')
