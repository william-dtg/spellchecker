from reader import getInput
from checker import getWordList

def __main__():
    inString = getInput()
    wordList = getWordList(inString)
    print(wordList)

if __name__ == "__main__":
    __main__()
