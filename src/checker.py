from aspell import Speller
from string import ascii_letters

validChars = set(ascii_letters) | {"'"}

def getWordList(inString: str) -> list[str]:
    spaceSplit = [word for word in inString.split(" ") if word != '']
    for i, word in enumerate(spaceSplit):
        newWord = word
        if not word[0] in validChars:
            newWord = newWord[0:]
        if not word[-1] in validChars:
            newWord = newWord[:-1]
        spaceSplit[i] = newWord
    return spaceSplit

def getWrongWords(words: list[str]) -> set[str]:
    s = Speller()
    wrongSet = set()
    for word in set(words):
        if not s.check(word):
            wrongSet.add(word)
    return wrongSet
