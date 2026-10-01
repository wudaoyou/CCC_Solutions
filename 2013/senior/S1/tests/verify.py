"""Check every allowed year against a list built using arithmetic digits."""

from bisect import bisect_right
from pathlib import Path
import runpy

next_distinct_year = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / 'solution.py'))['next_distinct_year']


def has_distinct_digits(year):
    seen = [False] * 10
    while year:
        year, digit = divmod(year, 10)
        if seen[digit]:
            return False
        seen[digit] = True
    return True


valid = [year for year in range(1, 10235) if has_distinct_digits(year)]
assert valid[-1] == 10234
for year in range(10001):
    expected = valid[bisect_right(valid, year)]
    assert next_distinct_year(year) == expected, year
print('All 10001 allowed starting years match arithmetic digit enumeration.')
