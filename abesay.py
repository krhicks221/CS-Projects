print("Abe can be shy sometimes...")
print("Maybe you could help him figure out what to say?")
text = input("What should he say? ")

def boxtext(text):
	print('<', text, '>')

abesay = open('ART.txt')
boxtext(text)
for line in abesay:
	print(line, end='')
