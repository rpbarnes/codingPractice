"""
given a string s = 'abc' generate all permutations of this string with a recursive algorithm

Jesus this worked first try...

"""

s = 'ctsandog'

#create a list of all permutations using some recursion

def makeAllPermutations(string):
    if len(string) <= 1:
        return set(string)

    allButLastChar = string[:-1]
    lastChar = string[-1]
    allPermutations = set()

    # generate a stack that will execute once break condition is hit
    allSmallPermutations = makeAllPermutations(allButLastChar)

    # put last char in every position of each string in allSmallPermutations
    for permutation in allSmallPermutations:
        for index in range(len(permutation)+1): # +1 because we want to bound the string with lastChar
            allPermutations.add(permutation[:index] + lastChar + permutation[index:])
    
    return allPermutations


perms = makeAllPermutations(s)

