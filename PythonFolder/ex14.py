# -*- coding: UTF-8 -*-''
from sys import argv

script, user_name = argv
prompt = '> ' #Bare en variabel for å bruke som prompt igjennom spørringen.

print "Hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s ?" % user_name
likes = raw_input(prompt) #prompt kommer i tillegg til annen input.

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is. 
And you have a %r computer. Nice.
""" % (likes, lives, computer)