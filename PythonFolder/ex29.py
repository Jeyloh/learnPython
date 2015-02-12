#	What If 

people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cafts! The world is saved"

if people < dogs:
	print "The world is drooled on"

if people > dogs:
	print "The world is dry!"

dogs += 5 # == dogs = dogs + 5

if people >= dogs:
	print "People are greater than or equal to dogs!"

if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
	print "People are equal to dogs"

cat_leaders = 2
presidents = 1
world_dies = True

print "\nThere is a war brewing. A war where cats are threatening our society!"
print "Humans and dogs has to do something to stop the cats from taking over the world!"
print "\nCurrently there are %d cat leaders, %d presidents, %d dogs, %d cats and %d people left" % (cat_leaders, presidents, dogs, cats, people)



while world_dies:
	if dogs + people >= cats and cat_leaders < presidents:
		print "The war is over. There are %d dogs, %d people, %d cats and %d cat leader(s) left!" % (dogs, people, cats, cat_leaders)
		"The president is unharmed!"
		print "\nThe balance of the world is back to normal!"
		world_dies = False
	else:
		print "\nAttack the cat leaders!"

		dogs -= 3
		print "Three dogs died..."
		people -= 5 
		print "Five humans died..."
		cat_leaders -= 1 
		print "One cat leader died!"
		cats -= 10 
		print "We killed 10 cats!!"

		world_dies = True
		