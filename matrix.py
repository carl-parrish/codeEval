#!/usr/bin/python

"""
Write a program which takes 4 inputs, where each input consists of 2 numbers in the format x,y. 
You are required to print a two dimensional array having x rows and y columns for each input.
 The elements of the arrays should be whole numbers starting from 1 and incrementing by 1. 
"""
my_input = []
my_input.append(raw_input(">"))
my_input.append(raw_input(">")) 
my_input.append(raw_input(">"))
my_input.append(raw_input(">"))

output = []

for data in my_input:
    rows, cols = data.split(',')
    rows = int(rows)
    cols = int(cols)


    rows_list = []
    cols_list = []
    print "Rows = %d, Cols = %d" % (rows,cols)

    for row in xrange(1,rows+1):
        #print "Row = ", row
        for col in xrange(0,cols):
            #print "Col = ", col
            cols_list.append(row+col)
        print repr(cols_list) 
        rows_list.append(cols_list)
        cols_list = []
    print repr(rows_list)
    #print repr(rows_list)

