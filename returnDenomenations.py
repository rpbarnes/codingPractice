"""
Given a total number and denomenations, this returns all the ways in which the denomenations can be added to get the number.

Given these
n = 4
denoms = [1, 2, 3]

it should return 
[1, 1, 2]
[1, 1, 1, 1]
[1, 3] 
[2, 2]

"""

n = 4
denoms = [1, 2, 3]

# How do I want to do this? Go through the list of denomenations and see if, I add them together I get the final value... This will only get me the ones where there are no duplicate values... How do you effectively check for duplicates without running calculations to infinity? You can say that the smallest denomentation is 1, thus the total number of loops that I need to do is  the number that I want to make.
