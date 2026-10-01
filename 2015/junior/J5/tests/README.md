# Verification

`j5.1` through `j5.10` are the supplied official input/output pairs; they remain unchanged. From the repository root, run `python3 tools/judge.py 2015/junior/J5` to check them.

Run `python3 2015/junior/J5/tests/verify.py` for the sample cases and a small independent oracle. The oracle enumerates non-decreasing positive allocations and compares their counts with the dynamic program for every total up to 18 and every valid number of people.
