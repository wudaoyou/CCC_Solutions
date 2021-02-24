if __name__ == '__main__':
    vowel = 'aeiou'
    consonant = 'bcdfghjklmnpqrstvwxyz'
    vow_dict = {}
    vow_dict['a'] = 'bc'
    vow_dict['e'] = 'dfg'
    vow_dict['i'] = 'hjkl'
    vow_dict['o'] = 'mnpqr'
    vow_dict['u'] = 'stvwxyz'
    s = input()
    s_out = ''
    for c in s:
        if c in vowel:
            s_out += c
        else:
            s_out += c
            for k, v in vow_dict.items():
                if c in v:
                    s_out += k
            if c != 'z':
                s_out += consonant[consonant.find(c) + 1]
            else:
                s_out += 'z'
    print(s_out)