import sys

k = int(sys.stdin.read())
icon = ("*x*", " xx", "* *")

for row in icon:
    scaled = "".join(char * k for char in row)
    for _ in range(k):
        print(scaled)
