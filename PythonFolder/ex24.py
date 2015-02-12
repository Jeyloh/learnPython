print "Let's practice everything."
print 'you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world 
with logic so firmly planted
cannnot discern \n the needs of love
nor comprehend passion from intuition 
and requires an explanation
\n\t\where there is none.
"""

print "________"
print poem
print "________"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
# Define three variables to call our function with parameter from line 26
beans, jars, crates = secret_formula(start_point)

# Here we make use of 'start_point' to give our functiona parameter.
print "With a starting point of: %d" % start_point 
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)