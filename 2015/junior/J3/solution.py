word = input().strip()
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
translated = []

for letter in word:
    if letter in vowels:
        translated.append(letter)
        continue

    closest = vowels[0]
    for vowel in vowels[1:]:
        if abs(ord(letter) - ord(vowel)) < abs(ord(letter) - ord(closest)):
            closest = vowel

    if letter == "z":
        next_consonant = "z"
    else:
        next_consonant = consonants[consonants.index(letter) + 1]
    translated.extend((letter, closest, next_consonant))

print("".join(translated))
