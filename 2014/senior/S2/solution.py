import sys


data = sys.stdin.read().split()
n = int(data[0])
partners = dict(zip(data[1:n + 1], data[n + 1:]))
good = all(name != partner and partners[partner] == name for name, partner in partners.items())
print("good" if good else "bad")
