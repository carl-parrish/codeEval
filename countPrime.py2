#!/usr/bin/python
"""
Counting Primes

Given two integers N and M, count the number of prime numbers 
between N and M (both inclusive)

"""
from sys import argv

def isPrime(num):
	for i in xrange(3, num/2,2):
		if num % i == 0:
			return False
	else:
		return True
	
fileName = argv[1]
input = open(fileName)

for limits in input.readlines():
	if len(limits) <=1:
		continue
		
	lower, upper = limits.split(',')
	
	lower = int(lower)
	upper = int(upper)+1
	
	if lower % 2 == 0:
		lower += 1 #even numbers can't be prime unless they are '2'

	if lower <= 3:
		primeList = [2]
	else:
		primeList = []
		
		
	for i in xrange(lower, upper, 2):
		if isPrime(i):
			primeList.append(i)
			
	print len(primeList)