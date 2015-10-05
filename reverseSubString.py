#!/usr/bin/python

"""
Intervew Challenge
Embedded in this block of text is the password for level 2.
The password is the longest substring that is the same in reverse.

As an example, if the input was "I like racecars that go fast"
the password would be "racecar".
"""

def reverse(source):
    size = len(source)
    output = ''
    for char in xrange(size-1, -1, -1):
        output += source[char]
    return output
input_string ="FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

rev_string  = reverse(input_string)
size = len(input_string)-1

password = ""

for begin in xrange(0,size) :
    for end in xrange(begin, size):
        #print "begin is: %d, end is: %d, " % (begin, end)
        subString = input_string[begin:end]
        if rev_string.find(subString) == -1:
            break
        elif len(subString) > len(password):
            password = subString
	    #print password
        else:
            pass
print password 
