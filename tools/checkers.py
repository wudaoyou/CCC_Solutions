"""Answer rules shared by the local runner and the real DMOJ judge."""

from math import isclose, isfinite, isqrt


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def check_output(problem, input_data, output, expected):
    """Return False for malformed or incorrect contestant output."""
    try:
        if problem == "2012/junior/J3":
            return output.decode().splitlines() == expected.decode().splitlines()
        if problem == "2019/senior/S2":
            values = list(map(int, input_data.split()))
            pairs = list(map(int, output.split()))
            if len(values) != values[0] + 1 or len(pairs) != 2 * values[0]:
                return False
            return all(
                2 <= a <= 2 * n and 2 <= b <= 2 * n
                and a + b == 2 * n and is_prime(a) and is_prime(b)
                for n, a, b in zip(values[1:], pairs[::2], pairs[1::2])
            )
        if problem == "2019/junior/J5":
            lines = input_data.decode().splitlines()
            rules = [line.split() for line in lines[:3]]
            steps, word, target = lines[3].split()
            moves = output.decode().splitlines()
            if len(moves) != int(steps):
                return False
            for line in moves:
                rule, position, result = line.split()
                rule, position = int(rule), int(position) - 1
                if not 1 <= rule <= 3 or position < 0:
                    return False
                old, new = rules[rule - 1]
                if word[position:position + len(old)] != old:
                    return False
                word = word[:position] + new + word[position + len(old):]
                if word != result:
                    return False
            return word == target
        if problem in {"2018/senior/S1", "2020/senior/S1", "2021/senior/S1"}:
            actual, wanted = output.split(), expected.split()
            return len(actual) == len(wanted) and all(
                isfinite(float(a)) and isclose(float(a), float(b), rel_tol=1e-5, abs_tol=1e-6)
                for a, b in zip(actual, wanted)
            )
        return output.split() == expected.split()
    except (ValueError, IndexError, UnicodeError):
        return False
