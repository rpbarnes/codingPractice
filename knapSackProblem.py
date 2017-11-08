"""
Given a total amount and a list of denomenations give me every possible combination of denomentations that returns the total amount.

"""

listOfDenoms = [5,10,25]
total = 100

def makeDenoms(currVal, denoms, currList):
    """
    currVal - (int) value to make
    denoms - (list) values you have available
    currList - (list) values you have used so far

    returns set of tuple solutions
    """

    currentSolutions = set()

    for val in denoms:
        newList = list(currList) # this is super memory intensive...
        remainder = currVal - val
        newList.append(val)
        if remainder > 0:
            currentSolutions.update(makeDenoms(remainder, denoms, newList))

        elif remainder == 0:
            newList.sort()
            currentSolutions.add(tuple(newList)) # you have to fix the memory size and use immutable element before it can be hashed.
            del newList
        else: # try and do some memory clean up
            del newList

    return currentSolutions

solutions = makeDenoms(total, listOfDenoms, [])

