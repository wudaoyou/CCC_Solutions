def rotate(word):
    lst = 'IOSHZXN'

    for c in word:
        if c not in lst:
            return 'NO'
    return 'YES'


if __name__ == "__main__":
    print(rotate(input()))
