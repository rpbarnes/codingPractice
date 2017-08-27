"""
This is a simple example of using a recursive function to calculate N! 

"""

N = 5

def calcFactorial(N):
    if N == 1:
        return N
    else:
        return N*calcFactorial(N-1)


print calcFactorial(N)
