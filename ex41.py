class TheThing(object):

    def __init__(self):
        self.number = 0
        
    def some_function(self):
        print "I got called."
        
    def add_me_up(self, more):
        self.number += more
        return self.number
        
# two different things
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print b.add_me_up(30)

print a.number
print b.number

# Study this. This is how you pass a variable
# from one classs to another. You will need this.
class TheMultiplier(object):

    def __init__(self,base):
        self.base = base
        
    def do_it(self,m):
        return m * self.base
        
x = TheMultiplier(a.number)
print x.do_it(b.number)


## Animal is-a object (yes, sort of confusing) look at the extra credit 
class Animal(object):
    pass
    
## ??
class Dog(Animal):

    def __init__(self,name):
        ## ??
        self.name = name 
        
## ??
class Cat(Animal):

    def __init__(self,name):
        ## ??
        self.name = name
        
## ??
class Pearson(object):

        def __init__(self, name):
            ## ??
            self.name = name
            
            ## Person has_a pet of some kind
            self.pet = None
            
## ??
class Employee(Pearson):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass
    
## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

##??
mary = Pearson("Mary")

## ?? 