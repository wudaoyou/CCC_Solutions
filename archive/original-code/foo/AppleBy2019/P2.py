alphabets = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
L = int(input())
s = input()

if __name__ == '__main__':
    print(" ".join(list(
        map(lambda word: ''.join(list(map(lambda c: alphabets[(alphabets.index(c) + L) % 26], word))), s.split()))))
