# We can make functions return stuff by using the python word 'return' to set 
# variables to be a value from a function. 

# We define 4 functions to do math with input numbers. All of these functions 
# will return data so the data can be used as numbers later in the code.
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b # When we use add() we will get a + b as the return statement

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

# Here we give our functions some input numbers in the form of variables. 
# add(30, 5) will add 30 + 5
#age = add(30, 5)
#height = subtract(78, 4)
#weight = multiply(90, 2)
#iq = divide(100, 2)

# Alternative: Define own numbers
print "Lets define our own numbers in datatype float so that we can do math with them!"
print "enter age"
age = float(raw_input())
print "enter height"
height = float(raw_input())
print "enter weight"
weight = float(raw_input())
print "enter iq"
iq = float(raw_input())


# Print out the answers of our new variables
print "\nAge: %d, Height: %d Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "\nHere is a puzzle:"

# Lets break this code up by starting from the end.
# 
# age = 35
# height = 74
# weight = 180
# iq = 50
#
# divide(50, 2) = 25
# multiply(180, 25) = 4500
# subtract(74, 4500) = -4426
# add(35, -4426) = 4391
# 
# our 'ice' variable = 4391


ice = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", ice, "Can you do it by hand?"