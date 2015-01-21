print "How old are you?", # Komma brukes for at neste linje skal fortsette
age = raw_input()			# på samme linje. Her vil input skje på samme 
print "How tall are you?",	# linje som print "How old are you?"
height = raw_input()
print "How much do you weight?" 
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." %(age, height, weight)