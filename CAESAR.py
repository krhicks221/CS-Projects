#notes from CS Class
#written by Mr. Roaden
#no credit to me
#I am a noob

def shift(num, shifted):
	lower = 'abcdefghijklmnopqrstuvwxyz'
	upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	aftershift = ''
	for i in range(len(shifted)):
		didshift = False
		for j in range(len(lower)):
			if lower[j] == shifted[i]:
				aftershift += lower[(j+num)%26]
				didshift = True
				break
			elif upper[j] == shifted[i]:
				aftershift += upper[(j+num)%26]
				didshift = True
				break
		if not didshift:
			aftershift += shifted[j]
	return aftershift

theshift = 13
print('Type quit to exit')

while(True):
	shifted = input()
	if shifted == 'quit':
		break
	print(shift(theshift,shifted))
