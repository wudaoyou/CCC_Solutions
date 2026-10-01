import sys


def main():
    key, message = sys.stdin.read().split()
    key = int(key)
    print("".join(
        chr((ord(letter) - ord("A") - (3 * position + key)) % 26 + ord("A"))
        for position, letter in enumerate(message, start=1)
    ))


if __name__ == "__main__":
    main()
