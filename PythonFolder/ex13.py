# -*- coding: UTF-8 -*-''
#
# Når vi åpner en fil i command skriver vi 'python ex13.py'. ex13.py kalles
# en argumentajon.  

# Import setning: Her legger vi til funksjoner fra 'python feature set'. 
# Dette er for å holde programmet lite, og for å "dokumentere" for andre
# programmerere hva .py filen skal gjøre. Disse er kalt moduler.
from sys import argv # argv = argument variable

# Unpacks argv og gir den 4 variabler å arbeide med. Unpack =
# Ta alt i argv, pakk det ut og tildel til variablene på venstresiden
script, first, second, third = argv

# Når vi kjører filen fra command må vi gi variablene navn.
# e.g. python ex13.py first second 3rd 
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

