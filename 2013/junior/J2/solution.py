import sys

word = sys.stdin.readline().strip()
rotatable = set("IOSHZXN")
print("YES" if all(letter in rotatable for letter in word) else "NO")
