"""Run with: python3 tools/test_checkers.py"""

from checkers import check_output


def test_checkers():
    prime = "2019/senior/S2"
    assert check_output(prime, b"1\n4\n", b"3 5\n", b"5 3\n")
    assert not check_output(prime, b"1\n4\n", b"4 4\n", b"3 5\n")
    assert not check_output(prime, b"1\n4\n", b"3 5 7\n", b"3 5\n")
    assert not check_output(prime, b"1\n4\n", b"1000000000000000000007 -999999999999999999999", b"3 5")
    rule = "2019/junior/J5"
    data = b"A AB\nB AA\nAA B\n2 A ABA\n"
    assert check_output(rule, data, b"1 1 AB\n2 2 AAA\n", b"") is False
    assert check_output(rule, b"A AB\nB AA\nAA B\n1 A AB\n", b"1 1 AB\n", b"")
    assert not check_output(rule, b"A AB\nB AA\nAA B\n1 A AB\n", b"1 0 AB\n", b"")
    assert not check_output(rule, b"A AB\nB AA\nAA B\n1 A AB\n", b"4 1 AB\n", b"")
    assert not check_output(rule, data, b"garbage\n", b"")
    floating = "2020/senior/S1"
    assert check_output(floating, b"", b"1.000001", b"1")
    assert not check_output(floating, b"", b"nan", b"1")
    assert not check_output(floating, b"", b"1 2", b"1")
    assert check_output("2010/junior/J1", b"", b"2\n", b"2")
    assert not check_output("2010/junior/J1", b"", b"3", b"2")


if __name__ == "__main__":
    test_checkers()
    print("Answer checker checks passed.")
