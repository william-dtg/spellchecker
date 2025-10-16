from reader import getInput
from checker import getWordList
from checker import getWrongWords

def __main__():
    inString = getInput()
    wordSet = getWordList(inString)
    print(wordSet)
    wrongWords = getWrongWords(wordSet)
    print(wrongWords)

if __name__ == "__main__":
    __main__()
