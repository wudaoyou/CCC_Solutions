# Verification

`j4.1` through `j4.3` are the supplied official input/output pairs; they remain unchanged. From the repository root, run `python3 tools/judge.py 2015/junior/J4` to check them.

Run `python3 2015/junior/J4/tests/verify.py` for small cases with manually calculated expected output plus 100 fixed-seed generated conversations. The generated cases build legal R/S events with absolute times, encode each gap as a W record when needed, and calculate expected waits directly from those times. Together they check default and explicit one-second gaps, interleaved friends, repeated replies, and unanswered messages.
