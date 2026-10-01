if __name__ == '__main__':
    s = input()
    happy_count = 0
    sad_count = 0
    happy = ':-)'
    sad = ':-('

    # s = 'How are you :-) doing :-( today :-)?'

    while len(s) > 0:
        if s.find(happy) == 0:
            happy_count += 1
            s = s[3:]
        elif s.find(sad) == 0:
            sad_count += 1
            s = s[3:]
        else:
            s = s[1:]

    if happy_count == 0 and sad_count == 0:
        print('none')
    elif happy_count == sad_count:
        print('unsure')
    else:
        print('happy') if happy_count > sad_count else print('sad')
