<<<<<<< HEAD
#Function shifts forward by 13
=======
#For Jack, we'll call this siezure cypher for one week... He is awful...

#notes from CS Class
#written by Mr. Roaden
#no credit to me
#I am a noob

>>>>>>> ca0fecf17801d838e9b89742b2cf69c96e9d348e
def shift(num, shifted):
	#Alphabet to be used
	lower = 'abcdefghijklmnopqrstuvwxyz'
	upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	aftershift = ''
	for i in range(len(shifted)):
		didshift = False
		for j in range(len(lower)):
			if lower[j] == shifted[i]:
				aftershift += lower[(j+num)%26] #Shift by num
				didshift = True
				break
			elif upper[j] == shifted[i]: #assumed upper == lower
				aftershift += upper[(j+num)%26] #Shift by num
				didshift = True
				break
		if not didshift: #If not found. Add original back
			aftershift += shifted[j]
	return aftershift

theshift = 13 #Shift by 13 for easy cipher
print('Type quit to exit')

while(True):
	shifted = input()
	if shifted == 'quit': #Exit function
		break
	print(shift(theshift,shifted)) #Print shifted value
