from string import ascii_letters

validChars = set(ascii_letters) | {"'"}

def getWordList(inString: str) -> list[str]:
    spaceSplit = inString.split(" ")
    for i, word in enumerate(spaceSplit):
        newWord = word
        for letter in word:
            if not letter in validChars:
                newWord = newWord.replace(letter, '')
        spaceSplit[i] = newWord
    return set(spaceSplit)
