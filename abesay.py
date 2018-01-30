print("Abe can be shy sometimes...")
print("Maybe you could help him figure out what to say?")
print("What should he say?")
text = input()

textbox = open('textbox.txt')
abesay = open('ART.txt')
for line in textbox:
	print(line)
for line in abesay:
	print(line)





