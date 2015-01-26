# Functions do 3 things
# 1: Name pieces of code as variables does with strings and numbers
# 2: Take arguments
# 3: Use 1 and 2 to make mini-scripts or tiny commands
# 
# Created by the word *def*ine

# this one is like your scripts with argv
def print_two (*args): # *args is asterisk arguments which is similar to argv parameters
	# functions has to end with ':' and content has to be indented
	arg1, arg2 = args # unpacks the arguments, ame as with scripts
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	

# ok, that *args is actually pointless, we can just do this
def print_two_again (arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this takes no arguments
def print_none():
	print "I got nothin'"

# We use our functions just like we use imported functions like open() or exists().
# That means that we can create our own small scripts and use them for a larger 
# piece of code. 
print_two("Kaja", "Monsen")
print_one ("ser")
print_two_again ("American", "Gangster")
print_none()
