def cheeese_and_crackers(cheeese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheeese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
        
 
print "We can just give the function numbers directly:"
cheeese_and_crackers(20,30)

print "OR,we can just give the function numbers directly:"
amount_of_cheese = 10
amount_of_crackers = 50

cheeese_and_crackers(amount_of_cheese, amount_of_crackers)

print  "We can even do match inside too:"
cheeese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and match:"
cheeese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)