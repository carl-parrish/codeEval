#!/usr/bin/python

"""
Write a program which capitalizes words in a sentence. 
"""

from sys import argv

fileName = argv[1]

input = open(fileName)

for line in input.readlines():
	for word in line.split(" "):
		word = word.lstrip()
		firstLetter = str(word[0]).upper()
		substring = word[1:]
		capitalize = firstLetter + substring
		print (capitalize),		
