import time
wordListFileName = "C:\Python27\Word Distance Measurer\corncob_lowercase.txt"

wordList = open(wordListFileName)

dictionary = {}

for line in wordList:
    line = line.strip()
    dictionary[line] = len(line)
    

def reduceLength(word):
    candidates = []
    for i in range(1, len(word)+1):
        
        newword = word[:(i-1)] + word[i:]
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

def distanceToAdjacent(word):
    distanceDict = {}
    for i in dictionary:
       distanceDict[i] = levenshteinDistance(word, i)
    del distanceDict[word]
    return min(distanceDict, key=distanceDict.get), distanceDict[min(distanceDict, key=distanceDict.get)]

    
def levenshteinDistance(word_1, word_2):
    #time_now = time.time()
    word_matrix = [[0 for x in range(len(word_2)+1)] for y in range(0,len(word_1)+1)]
    for i in range(1,len(word_1)+1):
        word_matrix[i][0] = i

    for j in range(1,len(word_2)+1):
        word_matrix[0][j] = j

    for j in range(1,len(word_2)+1):
        for i in range(1,len(word_1)+1):
            if str(list(word_1)[i-1]) == str(list(word_2)[j-1]):
                substitutionCost = 0
            else:
                substitutionCost = 1
            word_matrix[i][j] = min( (word_matrix[i-1][j] + 1),
                                     (word_matrix[i][j-1] + 1),
                                     (word_matrix[i-1][j-1] + substitutionCost) )
    #print word_matrix
    #print time.time() - time_now
    return word_matrix[len(word_1)][len(word_2)]

