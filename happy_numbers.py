#! /usr/bin/python


"""
Happy Numbers

Description:
A happy number is defined by the following process. Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until
the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not
include 1. Those numbers for which this process ends in 1 are happy numbers, while those 
that do not end in 1 are unhappy numbers.

"""
from sys import argv

def isHappyNumber(num):
""" Verify if the number given is happy or not"""
	ans = sumOfSquares(num)
	if ans == 1:
		return True
	return isHappyNumber(ans)


def splitDigits(num):
	myString = str(num)
	myList = list(myString)
	return myList
	
	
def sumOfSquares(num):
	answer = 0
	digitList = splitDigits(num)
	
	for i in digitList:
		answer += int(i) ** 2
	
	return answer

fileName = argv[1]

input = open(fileName)

for number in input.readlines():
	try:
		 isHappyNumber(number.strip())
		 
	except RuntimeError:
		print "0"
		
	else:
		print "1"
		

		


