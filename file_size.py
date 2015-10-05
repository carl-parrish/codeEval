#! /usr/bin/python

"""
Print the size of a file in bytes. 
"""

from sys import argv
from os import stat

fileName = argv[1]

size = stat(fileName).st_size 

print "%d" % (size)
