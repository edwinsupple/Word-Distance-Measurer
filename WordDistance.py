import time
wordListFileName = "C:\Python27\Word Distance Measurer\corncob_lowercase.txt"

wordList = open(wordListFileName)

dictionary = {}

for line in wordList:
    line = line.strip()
    dictionary[line] = len(line)
    

def reduceLength(word):
    candidates = []
    for i in range(len(word)):
        newword = str.replace(word, word[i], '', 1)
        candidates.append(newword)
    return candidates

def addLetter(word, letter):
    candidates = []
    if len(letter) != 1 or letter.isalpha() == False:
        raise ValueError
    for i in range(len(word)+1):
        newword = word[:i] + letter + word[i:]
        candidates.append(newword)
    return candidates

def replaceLetter(word, letter):
    candidates = []
    if len(letter) != 1 or letter.isalpha() == False:
        raise ValueError
    for i in range(len(word)):
        newword = word[:i] + letter + word[(i+1):]
        if newword != word:
            candidates.append(newword)
    return candidates

def allAdjacent(word):
    candidates = []
    candidates.extend(reduceLength(word))
    for i in "abcdefghijklmnopqrstuvwxyz":
        candidates.extend(addLetter(word, i))
        candidates.extend(replaceLetter(word, i))
    return candidates

def noAdjacent(word_length):
    time_now = time.time()
    words = []
    for i in dictionary:
        if len(i) == word_length:
            if spellCheck(allAdjacent(i)) == False:
                words.append(i)
    print time.time() - time_now
    return words       


def spellCheck(wordlist):
    for word in wordlist:
        if word in dictionary:
            return True
    return False

        
