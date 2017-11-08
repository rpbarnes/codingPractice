"""
given a string determine if it's possible to form a palindrome out of some permutation of the string.

I'm going to check for characters in the string that occur an odd number of times. If I have more than one character that occurs an odd number of times I know it is not possible to make a palindrome with the set of characters.

I will do this by keeping the characters that appear an odd number of times in a set. 

When I come accross a new character, I will add it to the set. If the character is in the set I will remove it. Thus only odd number occurances are left. Then check if the len(set) > 1 return False.

"""

string = 'aaaabbccddeef'

def determinePalindrome(string):
    oddNumChars = set()
    for char in string:
        if char in oddNumChars:
            oddNumChars.discard(char)
        else:
            oddNumChars.add(char)
    if len(oddNumChars) > 1:
        return False
    return True

print determinePalindrome(string)
