from reader import getInput
from checker import getWordList
from checker import getWrongWords

def __main__():
    inString = getInput()
    wordList = getWordList(inString)
    print(wordList)
    wrongWords = getWrongWords(wordList)
    print(wrongWords)

if __name__ == "__main__":
    __main__()
