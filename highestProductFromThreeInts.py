"""
Given a list of integers find the largest product you can get from any three of the integers

The largest value will result from multiplication of the three largest values. Find the three maximum values and multipl them together
"""

import random
def highestProductOfThree(list_of_ints):
    highest = list_of_ints[0]
    highest_prod_3 = list_of_ints[0]
    highest_prod_2 = list_of_ints[0]
    lowest = list_of_ints[0]
    lowest_prod_2 =list_of_ints[0]
    for i,val in enumerate(list_of_ints):
        if i == 0:
            continue
# look at the highest product of three ints. Need at least three independent values to calculate this
        if i >= 2:
            potentialH3H = highest_prod_2 * val
            potentialH3L = lowest_prod_2 * val

            potentialHighest3 = max(potentialH3H,potentialH3L)
            highest_prod_3 = max(potentialHighest3,highest_prod_3)

# find the largets product of two
        if i >= 1:
            potentialH2H = highest * val
            potentialH2L = lowest * val

            highest_prod_2Pot = max(potentialH2H,potentialH2L)
            lowest_prod_2Pot = min(potentialH2H,potentialH2L)
            highest_prod_2 = max(highest_prod_2,highest_prod_2Pot)
            lowest_prod_2 = min(lowest_prod_2,lowest_prod_2Pot)

        highest = max(val,highest)
        lowest = min(val,lowest)
    return highest_prod_3

size = [1e3,1e4,1e5,1e6,1e7]
times = [None]*len(size)
for count,val in enumerate(size):
    list_of_ints = []
    for i in range(int(val)):
        list_of_ints.append(random.randint(-100,100))

    start = time.time()
    highestProd3 = highestProductOfThree(list_of_ints)
    duration = time.time() - start
    times[count] = duration
    print highestProd3
    print "This took ",(duration)

plot(time,size)
show()
