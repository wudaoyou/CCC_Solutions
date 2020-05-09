from sys import stdin

if __name__ == '__main__':
    input = stdin.readline
    n = int(input())
    count = 0
    s1 = input()
    s2 = input()
    for i in range(len(s1)):
        if s1[i] == s2[i] and s1[i] != '\n' and s1[i] != '.':
            count += 1
    print(count)
