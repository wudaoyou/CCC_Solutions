import sys


def main():
    values = list(map(int, sys.stdin.read().split()))
    time_limit, count = values[:2]
    chores = sorted(values[2:2 + count])

    spent = completed = 0
    for duration in chores:
        if spent + duration > time_limit:
            break
        spent += duration
        completed += 1

    print(completed)


if __name__ == "__main__":
    main()
