import sys


count = int(sys.stdin.readline())
codes = {}
for _ in range(count):
    character, code = sys.stdin.readline().split()
    codes[code] = character

message = sys.stdin.readline().strip()
current = ""
decoded = []
for bit in message:
    current += bit
    if current in codes:
        decoded.append(codes[current])
        current = ""

print("".join(decoded))
