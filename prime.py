#! /usr/bin/python

"""
Prime Numbers

Description:

Print out the prime numbers less than a given number N. For bonus points your 
solution should run in N*(log(N)) time or better. 
You may assume that N is always a positive integer. 

"""

from sys import argv

def isPrime(num):
	for i in xrange(3, num/2,2):
		if num % i == 0:
			return False
	return True


fileName = argv[1]
input = open(fileName)

for limit in input.readlines():
	if len(limit) <=1:
		continue
		
	limit = int(limit)
	primeList = [2]
	
	for i in xrange(3,limit,2):
		if isPrime(i):
			primeList.append(i)
	
	print '%s' % ','.join(map(str, primeList))
