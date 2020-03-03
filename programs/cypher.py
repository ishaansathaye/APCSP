from pip._vendor.idna import unichr

maxUnicode = 126
minUnicode = 32


def encodeCharacter(passcharacter):
    temp = ord(passcharacter) + int(shift)
    if temp > maxUnicode:
        restShift = temp - maxUnicode
        temp = (restShift - 1) + minUnicode
    return unichr(temp)


def decodeCharacter(passcharacter):
    temp = ord(passcharacter) - int(shift)
    if temp < minUnicode:
        restShift = temp - minUnicode
        temp = (restShift + 1) + maxUnicode
    return unichr(temp)


def encodePhrase(passphrase):
    length = len(passphrase)
    for i in range(0, length):
        temp = ord(passphrase[i]) + int(shift)
        if temp > maxUnicode:
            restShift = temp - maxUnicode
            temp = (restShift - 1) + minUnicode
        print(unichr(temp), end="")


def decodePhrase(passphrase):
    length = len(passphrase)
    for i in range(0, length):
        temp = ord(passphrase[i]) - int(shift)
        if temp < minUnicode:
            restShift = temp - minUnicode
            temp = (restShift + 1) + maxUnicode
        print(unichr(temp), end="")


encodingDecoding = input("Are you encoding or decoding? (e/d): ")
phraseCharacter = input("Are you inputting a character or phrase? (c/p): ")
shift = input("What is the shift? (number): ")
print()
if phraseCharacter == "c":
    if encodingDecoding == "e":
        character = input("What character are you encoding?: ")
        print()
        print("Cypher Encoded:", encodeCharacter(character))
    elif encodingDecoding == "d":
        character = input("What character are you decoding?: ")
        print()
        print("Cypher Decoded:", decodeCharacter(character))
    else:
        print("NOT VALID input!")
elif phraseCharacter == "p":
    if encodingDecoding == "e":
        phrase = input("What phrase are you encoding?: ")
        print()
        encodePhrase(phrase)
        print()
    elif encodingDecoding == "d":
        phrase = input("What phrase are you decoding?: ")
        print()
        decodePhrase(phrase)
        print()
    else:
        print("NOT VALID input!")
else:
    print("NOT VALID input!")

