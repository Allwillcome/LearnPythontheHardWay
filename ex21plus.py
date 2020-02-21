def area(a, b):
    print "area = %d * %d" % (a, b)
    return a * b 
    
def Volume(s, h):
    print "Volume = %d * %d" % (s, h)
    return s * h 
    
print "Let's us calculate the volume of cubid"

print "We the long is 4, \nthe width is 5, \nthe height is 6."

print "First we calculate the floor area"

floor = area(4, 5)

# print "The floor is %d" % floor

print "Sencond, We calculate the volume:"

# return the value not the character
Volume0 = Volume(floor, 6)

print "The volume is %d" % Volume0

# Advanced Exercise
Len = int(raw_input("Please input the length:"))
Wid = int(raw_input("Please input the width:"))
Hei = int(raw_input("Pleasr input the height"))

Volume1 = Volume(area(Len, Wid), Hei)

print "The volume is: %d" %Volume1
