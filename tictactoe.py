import random #imports the random function for the computer opponent

board = [0, 1, 2,
	 3, 4, 5,
	 6, 7, 8] #defines board as these specific integers

def draw(): #draws the board and assigns numbers to each block
	print('   |   |')
	print(board[0],' |',board[1],'|',board[2])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(board[3],' |',board[4],'|',board[5])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(board[6],' |',board[7],'|',board[8])
	print('   |   |')

def linecheck(letter, block1, block2, block3):
	if board[block1] == letter and board[block2] == letter and board[block3] == letter:
		return True

def fullcheck(letter):
	if linecheck(letter, 0, 1, 2):
		return True
	if linecheck(letter, 3, 4, 5):
		return True
	if linecheck(letter, 6, 7, 8):
		return True
	if linecheck(letter, 0, 3, 6):
		return True
	if linecheck(letter, 1, 4, 7):
		return True
	if linecheck(letter, 2, 5, 8):
		return True
	if linecheck(letter, 0, 4, 8):
		return True
	if linecheck(letter, 2, 4, 6):
		return True

while True: #The actual game starts here
	select = input("Select a block by selecting a number, 1-9: ") #Select which block you want your X in
	select = int(select)
	if board[select] != 'X' and board[select] != 'O':
		board[select] = 'X'
		if fullcheck('X') == True:
			print("You won!")
			break
		while True: #The computers' turn
			computer = random.randint(0,8)
			if board[computer] != 'O' and board[computer] != 'X':
				board[computer] = 'O'
				if fullcheck('O') == True:
					print("Sorry, the computer won...")
					break
				break
	else:
		print("Choose a different block, the one you chose is taken.")
	draw()
