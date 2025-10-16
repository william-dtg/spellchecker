from aspell import Speller
from string import ascii_letters

validChars = set(ascii_letters) | {"'"}

def cleanWord(word: str) -> str:
    if not word[0] in validChars:
        word = word[0:]
    if not word[-1] in validChars:
        word = word[:-1]
    return word


def getWordList(inString: str) -> list[str]:
    spaceSplit = [word for word in inString.split(" ") if word != '']
    for i, word in enumerate(spaceSplit):
        spaceSplit[i] = cleanWord(word)
    return spaceSplit

def getWrongWords(words: list[str]) -> set[str]:
    s = Speller()
    wrongSet = set()
    for word in set(words):
        if not s.check(word):
            wrongSet.add(word)
    return wrongSet
