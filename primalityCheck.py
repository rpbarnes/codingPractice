"""
Check to see if a given number is prime.

I'm going to be as fancy as possible because that's good practice.

Here I'm going to generate a list of primes that I can hold on to and then check to see if my number given is divisible by any prime numbers in the list.

"""

import numpy as np

def listOfPrimes(maxNumber):
    "This generates a list of primes up to the number maxNumber using the eratosthenes sieve"
    primes = []
    for i in range(2,maxNumber+1):
        primes.append(i)

    i = 0
    while i < len(primes):
        num = primes[i]
        numerator = i+1
        while numerator < len(primes):
            if primes[numerator] % primes[i] == 0: # numerator is divisible by i
                primes.pop(numerator)
            else:
                numerator+=1
        i+=1
    return primes

def isPrime(number):
    maxNum = int(np.sqrt(number)) + 1 # only need to go up to. The +1 is to ensure we don't suffer because of rounding error
    primes = listOfPrimes(maxNum)
    for prime in primes:
        if number % prime == 0:
            return False
    return True
   
print isPrime(199)


