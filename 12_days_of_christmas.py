i=0
while i<12:
	print(f'On the {'First Second Third Fourth Fifth Sixth Seventh Eighth Ninth Tenth Eleventh Twelfth'.split()[i]} day of Christmas','My true love sent to me',*'Twelve Drummers Drumming,|Eleven Pipers Piping,|Ten Lords-a-Leaping,|Nine Ladies Dancing,|Eight Maids-a-Milking,|Seven Swans-a-Swimming,|Six Geese-a-Laying,|Five Gold Rings,|Four Calling Birds,|Three French Hens,|Two Turtle Doves, and|A Partridge in a Pear Tree'.split('|')[11-i:],sep='\n',end='.\n\n')
	i+=1