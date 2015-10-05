#! /usr/bin/python

"""
Prime Palindrome 

Description:

Write a program to determine the biggest prime palindrome under 1000.

"""			
def isPrime(num):
	for i in xrange(3, num/2,2):
		if num % i == 0:
			return False
	return True
	
def isaPalindrome(num):
	srcString = str(num)
	srcList = list(srcString) # allows me to use pop for reverse
	testList = reverseList(srcList)
	
	if list(srcString) == testList:
		return True
	else:
		return False

def reverseList(srcList):
	reverse = []
	
	for i in xrange(len(srcList)):
		reverse.append(srcList.pop(-1))  #puts last element of list next in the reverse list
	return reverse


limit = 1000
answer = 0

for i in xrange(3,limit, 2):
	if isPrime(i) and isaPalindrome(i):
		answer = i 
		
print "%s" % answer		