"""

This script finds the corresponding closing parenthesis given an opening one in the string.

given this string

"Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

and 10

you should return 79.

Go through the string and put opening parenthesis in a list and as you encounter closing parenthesis pop items out of the end of the list. If an item poped out of the list coresponds to the position you were given return the position of the current closed parenthesis.

"""

string = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
openPos = 10

def returnClosingParen(string, openPos):
# check that the position given corresponds to a parenthesis
    if string[openPos] != '(':
        print "position given does not correspond to an open parenthesis"
        return False

    openedList = []
    for pos, char in enumerate(string):
        if char == '(':
            openedList.append(pos)
        elif char == ')': # this closes the last opened parenthesis we encountered. Lets see if it corresponds to the position we care about.
            if openedList.pop() == openPos:
                return pos

closing = returnClosingParen(string, openPos)
print closing


