# Here we will use functions and variables interchangeably. 

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

def user_cheese_and_crackers():
	print "How much cheese?"
	cheese = raw_input()
	print "How many crackers?"
	crackers = raw_input()
	print "Cheese: %s" % cheese
	print "Crackers: %s" % crackers


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Until now we just used our function with parameter value. Hereon, we'll 
# define variables aswell.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# 		function 		variable 		variable
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside to:"
cheese_and_crackers(10 + 20, 5 + 6)

# Here we use the function, the two variables and two numbers for math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Hjemmelaga test!
user_cheese_and_crackers()

