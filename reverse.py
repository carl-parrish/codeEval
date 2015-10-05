#! /usr/bin/python

""" Write a program to reverse the words of an input sentence.  """

"""
Input sample:
 The frist argument will be a text file containg multiple sentences, one per line. Possible empty lines too.  
"""

from sys import argv 
 

fileName = argv[1]

input = open(fileName)

for line in input.readlines(): 
	if len(line) <= 1:
		continue
	else:
		list = line.split()
		size = len(list)
		for word in range((size-1), -1, -1):
			print list[word],
		print "\n",

input.close()
