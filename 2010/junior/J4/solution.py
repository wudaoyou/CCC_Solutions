import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    answers = []
    pos = 0

    while pos < len(data):
        n = data[pos]
        pos += 1
        if n == 0:
            break

        temperatures = data[pos:pos + n]
        pos += n
        changes = [b - a for a, b in zip(temperatures, temperatures[1:])]

        if not changes:
            answers.append("0")
            continue

        for period in range(1, len(changes) + 1):
            if all(changes[i] == changes[i % period] for i in range(period, len(changes))):
                answers.append(str(period))
                break

    sys.stdout.write("\n".join(answers))
    if answers:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
