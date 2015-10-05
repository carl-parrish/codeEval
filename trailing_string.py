#! /usr/bin/python

"""
Trailing String
Description:

You are given two strings 'A' and 'B'. Print out a 1 if string 'B' occurs at
the end of string 'A'. Else a zero. 

"""
from sys import argv

fileName = argv[1]

input = open(fileName)

for line in input.readlines():
	if len(line) <=1:
		continue

	haystack, needle = line.split(',')
	
	if haystack.strip().endswith(needle.strip()):
		print 1
	else:
		print 0
		
		
input.close()