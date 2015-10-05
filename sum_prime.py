#! /usr/bin/python

"""
Sum of Primes

Description:

Write a program to determine the sum of the first 1000 prime numbers.

"""

#Generate prime numbers
def generatePrimes(primes):
	for i in xrange(3,10000, 2):
		if isPrime(i):
			primes.append(i)
		if len(primes) >= 1000:
			break		
			

	
def isPrime(num):
	for i in xrange(3, num/2,2):
		if num % i == 0:
			return False
	return True
	
answer = 0
primeList = [2]
generatePrimes(primeList)

for i in primeList:
	answer += i

print "%i" % answer