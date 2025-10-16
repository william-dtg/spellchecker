from checker import cleanWord
from colorama import Back
from colorama import Style

def colorWord(rawWord: str, wrongSet: set[str]) -> str:
    isWrong = cleanWord(rawWord) in wrongSet
    if isWrong:
        return Back.RED + rawWord + Style.RESET_ALL
    else:
        return rawWord

def printStringColored(string: str, wrongSet: set[str]) -> None:
    for rawWord in (word for word in string.split(' ') if word != ''):
        print(colorWord(rawWord, wrongSet), end=' ')
    print('')
