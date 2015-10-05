#! /usr/bin/python

"""
Mth to last element

Description:

Write a program to determine the Mth to last element of a list.

"""
def findPosition(data):
	#pick off index
	index = data.pop(-1)
	
	#find length of data
	size = len(data)
	
	#if index is larger than the list size, ignore this input
	if (int(index) > int(size)):
		return 'ignoreData'
		
	return index

def printElement(data, position):
	index = int(position) * -1 #make negative so we can count from right side.
	print "%s" % data[index]
	 

from sys import argv

fileName = argv[1]

input = open(fileName)

for line in input.readlines():
	if len(line) <=1:
		continue

	data = line.strip().replace(' ','')
	data = list(data)
	position = findPosition(data)
	if (position == 'ignoreData'):
		continue
		
	printElement(data, position)

input.close()