#! /usr/bin/python

""" Given a string write a program to convert it into lowercase. """

"""
Input sample:
 The frist argument will be a text file containg sentences, one per line. You can assume all characters are from the english language
"""

from sys import argv 
 

fileName = argv[1]

input = open(fileName)

for line in input.readlines(): 
	if len(line) <= 1:
		continue
	else:
		print line.lower(), 
input.close()
