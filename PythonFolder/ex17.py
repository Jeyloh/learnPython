# This script will take two input files by string names and write content of the
# first file to the other.

# Imports argument variables
from sys import argv
# Returns true if a file exists based on its name as a string in an argument
from os.path import exists 

# Makes current script + variables from_file and to_file argument variables
script, from_file, to_file = argv

# Prints the name of the variables
print "Copying from %s to %s" % (from_file, to_file)

# This can be written in 1 line with the open function open(from_file, r). r is for read
# Use previous var in_file and apply a .read() function
# Opens the from file, reads the content, finds the length of content and prints it
in_file = open(from_file)
indata = in_file.read()
print "The input file is %d bytes long" % len(indata)

# imported exists command to check if the to_file exists.
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# Opens the to_file as we now know it exists. 
out_file = open(to_file, 'w') # 'w' = write as a string.
out_file.write(indata)

print "Alright, all done."

# Close both files
out_file.close()
in_file.close()




