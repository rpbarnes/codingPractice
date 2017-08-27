"""
this calculates all the solutions to a**3 + b**3 = c**3 + d**3 for a, b, c, d = 1 to N

calculate the upper traingle of 2d matrix ab with elements a**3 + b**3 and set the resutls as key to dictionary with indecies as the value 

"""
import time
import pylab as pl


def calcSolutions(N):# {{{
    """
    N - int - number of values to test for possible solution
    """
    if type(N) != int:
        N = int(N)
    print "Calculating for %i solutions"%N
    solutions = {} # put solutions as key and list of indecies as value.
    for a in range(N):
        for b in range(a,N):
            result = a**3 + b**3
            indecies = solutions.get(result)
            if indecies is None:
                indecies = [(a,b), (b,a)] # they are both valid solutions.
            else:
                indecies.append((a,b))
                indecies.append((b,a))
            solutions.update({result:indecies})

    print "The following lists contain all possible pairs of solutions for a^3 + b^3 = c^3 + d^3"
    for value in solutions.values():
        if len(value) > 3:
            print value
    return solutions
# }}}

N = [1e1,1e2,1e3,2e3]
times = []
for n in N:
    start = time.time()
    solutions = calcSolutions(n)
    times.append(time.time()-start)

pl.figure()
pl.plot(N,times)
pl.show()



