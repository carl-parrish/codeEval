#! /usr/bin/python

"""
Remove Characters

Description:

Write a program to remove specific characters from a string. 

"""

from sys import argv
from string import maketrans

fileName = argv[1]

input = open(fileName)

for line in input.readlines():
	if len(line) <=1:
		continue
	
	srcString, scrub = line.split(",")
	intab = "#"
	outtab = "$"
	
	tranString = maketrans(intab, outtab)
	print srcString.strip().translate(tranString, scrub.strip())
	
input.close()	