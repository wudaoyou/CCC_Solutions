
if __name__ == '__main__':
    s = input()
    length = 1
    for i in range(len(s)+1):
        for j in range(i):
            if s[j:i] == s[j:i][::-1]:
                length = max(length, i-j)

    print(length)
