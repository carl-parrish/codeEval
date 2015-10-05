#!/usr/bin/python
"""
brute force approach to decrypting
"""

for a in range(1,27):
    for b in range(1,27):
        for c in range(1,27):
            if a + 2 * b + 3 * c == 152 :
                if a != b != c:
                    print "A = %d, B= %d, C= %d" % (a,b,c)