# -*- coding: UTF-8 -*-''
#
# Her skal vi lage en ny fil med navn fra brukerinput. Vår fil skal hete
# ex15_sample.txt

# import av argv
from sys import argv 

# sette argument variabler
script, filename = argv 

# lager et fil objekt i variabelen txt
txt = open(filename)

# formaterer filnavnet i string og gir en liten beskjed
print "Here's your file %r:" % filename
# leser og returnerer inneholdet i variabelen txt
print txt.read()
txt.close()

# printer tekst
print "Type the filename again:"
# lager en ny variabel basert på input på brukeren (filnavnet)
file_again = raw_input ("> ")

# gjør klar en variabel som åpner filen fra forrige input
txt_again = open(file_again)

# leser og returnerer inneholder i den nye variabelen
print txt_again.read()
txt_again.close()
