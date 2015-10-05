#!/usr/bin/python

"""
Beautiful Strings
"""

from sys import argv

total_beauty = 0
cypher = ['B','E','A','U','T','Y']
file_name = argv[1]

file_buffer = open(file_name)

for line in file_buffer.readlines():
    #for make everything lower case
    line = line.upper()

    for character in line:
        if character.isalpha():
            if character in cypher:
                value = 26 - cypher.index(character)
            else:
                value = (26 - len(cypher)) - (ord(character)-65)
            #print "Caracter is: ", character , "Value is: ", value
            total_beauty += value

    print total_beauty#, "\t", line
    total_beauty = 0



