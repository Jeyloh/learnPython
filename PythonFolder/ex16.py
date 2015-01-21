# -*- coding: UTF-8 -*-''
from sys import argv

# Lagrer argument variabler kaldt script og filename
script, filename = argv

# bruker filnavn som en midlertidig erstatter 
print "We're going to erease %r" % (filename)
# skrift i 2 linjer

print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') # lagrer "åpne filnavnet" i en variabel

#print "Truncating the file. Goodbye!"
#target.truncate() # sletter innholdet

print "Now I'm going to ask you for three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()








