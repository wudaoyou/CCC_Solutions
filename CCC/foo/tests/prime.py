from math import sqrt
from itertools import count, islice
def prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True


def nextPrime(a):
    k = 0
    result = False
    while result is False:
        k = k + 1
        result = prime(a + k)
    return a + k


num = int(input())
values = []
answers = []

for i in range(num):
    N = int(input())
    values.append(N)

for i in range(len(values)):
    found = 0
    integer = values[i] * 2
    varA = 2
    while True:
        varB = integer - varA
        if prime(varB) is True:
            print(str(varA) + " " + str(varB))
            break
        else:
            varA = nextPrime(varA)
