#!/us/bin/python
"""
Output the multiplcation table
"""

multi_num_1 = 13
multi_num_2 = 13

#Outer loop

for outer in range(1,multi_num_1):
    for inner in range(1, multi_num_2):
        ans = inner * outer
        print "%4d" % ans ,
    
    print ""
