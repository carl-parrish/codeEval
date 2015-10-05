#! /usr/bin/python

"""
Self Describing Numbers

Description:

A number is a self-describing number when (assuming digit positions are labeled
0 to N-1), the digit in each position is equal to the number of times that that
digit appears in the number. 

"""

from sys import argv

def isDescribing(num):

	for i in xrange(len(num)):
		count = num.count(str(i))
		
		if(int(count) != int(num[i])):
			return 0
	return 1

fileName = argv[1]

input = open(fileName)

for line in input.readlines():
	answer = isDescribing(line.strip())
	print "%s" % answer    		

input.close()