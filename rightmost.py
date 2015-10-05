#! /usr/bin/python

"""
Rightmost Char

Description:

You are given a string 'S' and a character 't'. Print out the position of the rightmost
occurrence of 't'(case matters) in 'S' or -1 if there is none. The position to be printed
out is zero based. 

"""

from sys import argv 

fileName = argv[1]

input = open(fileName)

for line in input.readlines():
	haystack, needle = line.split(",")
	position = haystack.rfind(needle.strip())
	
	print "%s" % position
	
input.close() 