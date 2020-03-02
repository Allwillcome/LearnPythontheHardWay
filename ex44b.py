class Parent(object):

    def override(self):
        print "PARENT override()"
        
class Child(Parent):

    def override(self):
        print "CHILD override()"
        
# define variables but not call functions 
PARENT = Parent()
CHILD = Child()

PARENT.override()
CHILD.override()
