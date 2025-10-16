from reader import getInput
from checker import getWordList
from checker import getWrongWords
from writer import printStringColored

def __main__():
    inString = getInput()
    wordList = getWordList(inString)
    wrongWords = getWrongWords(wordList)
    printStringColored(inString, wrongWords)

if __name__ == "__main__":
    __main__()
