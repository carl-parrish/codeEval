#! /usr/bin/python

"""
Sum of Integers from File

Description:

Print out the sum of integers read from a file. 

"""

from sys import argv

answer = 0

fileName = argv[1]

test_cases = open(fileName)

for i in test_cases.readlines():
   answer += int(i)
   
test_cases.close()
print "%s" % answer