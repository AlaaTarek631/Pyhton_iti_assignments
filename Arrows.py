arrow = input ("enter the arrow number")
if arrow == '1':
	stars = 1
	Tstars = 3
	Mstars = 25
	FirstSpace = 20

	for i in range(9):
		if (i<3):
			print (" "*FirstSpace, end = " ")
			print ("*"*stars, end = " ")
			print ("\n")
			stars+=1
		elif (i>5):
			FirstSpace = 20
			print (" "*FirstSpace, end = " ")
			print ("*"*Tstars, end = " ")
			print ("\n")
			Tstars-=1		
		else:
			print ("*"*	Mstars, end = " ")
			print ("\n")
			if (Mstars==26):
				Mstars-=1
			else :
				Mstars+=1
elif (arrow == '2'):
	MFirstSpace = 7 
	Mstars = 9
	FirstSpace = 10
	stars = 3

	for i in range(15):
		if (i<10):
			print (" "*FirstSpace, end = " ")
			print ("*"*stars, end = " ")
			print ("\n")
		else:
			print (" "*	MFirstSpace, end = " ")
			print ("*"*	Mstars, end = " ")
			print ("\n")
			Mstars-=2
			MFirstSpace+=1
elif (arrow == '3'):
	stars = 1
	Space = 4
	Tstars = 24
	Mstars = 3

	for i in range(9):
		if (i<3):
			print (" "*Space, end = " ")
			print ("*"*stars, end = " ")
			print ("\n")
			stars+=1
			Space-=1
		elif (i>5):
			Space+=1
			print (" "*Space, end = " ")
			print ("*"*Mstars, end = " ")
			print ("\n")
			Mstars-=1			
		else:
			print (" "*Space, end = " ")
			print ("*"*Tstars, end = " ")
			print ("\n")
			if (Space>0):
				Space-=1
				Tstars+=1
			else :
				Space+=1
				Tstars-=1
elif (arrow == '4'):
	MFirstSpace = 9 
	Mstars = 1
	FirstSpace = 8
	stars = 3

	for i in range(15):
		if (i<3):
			print (" "*	MFirstSpace, end = " ")
			print ("*"*	Mstars, end = " ")
			print ("\n")
			Mstars+=2
			MFirstSpace-=1
		else:
			print (" "*FirstSpace, end = " ")
			print ("*"*stars, end = " ")
			print ("\n")
			
	