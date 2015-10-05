#! /usr/bin/python

"""
Sum of Digits

Description:

Given a positive integer, find the sum of its constituent digits. 

"""

def splitDigits(num):
	myString = str(num)
	myList = list(myString)
	return myList
	
def sumDigits(num):
	answer = 0
	digits = splitDigits(num)
	for i in digits:
		answer += int(i)
	return answer
		

from sys import argv

fileName = argv[1]

input = open(fileName)

for line in input.readlines():
	sum = sumDigits(line.strip())
	print "%s" % sum
	
input.close() 