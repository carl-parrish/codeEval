#!/usr/bin/python

"""
Unique Elements
You are given a sorted list of numbers with duplicates.
Print out the sorted list with duplicates removed.
"""

from sys import argv

file_name = argv[1]

file_input = open(file_name)

for line in file_input.readlines():
    sorted_list = line.rstrip().split(',')

    list_size = len(sorted_list)

    for current in xrange(0,list_size):
        #if current < list_size:

        #value = sorted_list[current]
        #print "List Size = %d: Current = %d: Value = %s" % (list_size, current, value)
        while (current < list_size and (sorted_list.count(sorted_list[current])) > 1):
            next = current + 1

            if (sorted_list[current] == sorted_list[next]):
                sorted_list.remove(sorted_list[next])
                list_size -= 1

        else:
            continue
        
            
    print ','.join(map(str, sorted_list))