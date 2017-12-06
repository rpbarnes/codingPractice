"""
given a sorted list with many elements that has been rotated by some amount find the rotation point.

"""

def rotationIndex(wordsList):
    if wordsList[-1] > wordsList[0]:
        return 0
    firstWord = wordsList[0]
    floorIndex = 0
    ceilingIndex = len(wordsList) - 1
    while floorIndex < ceilingIndex:
        guessIndex = floorIndex + ((ceilingIndex - floorIndex)/2)
        if wordsList[guessIndex] < firstWord:
            #go left
            ceilingIndex = guessIndex
        else:
            floorIndex = guessIndex
        
        if floorIndex + 1 == ceilingIndex:
            return ceilingIndex   

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

rp = rotationIndex(words)
print rp
