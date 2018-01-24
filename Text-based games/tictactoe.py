import os
import random
filledpos = []
board = ['X','1','2','3','4','5','6','7','8','9']
def display_board(board):
	os.system('clear')
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

def answer():
	global filledpos 
	boolean = True
	while boolean == True:
		x =int( input('What position do you want to place your move?'))
		if x in filledpos:
			print("This position has already been filled")
		elif 1 <= x <= 9:
			filledpos.append(x)
			boolean = False
		else:
			print("Please enter a number from 1 to 9")
	return x
def place_marker(board,marker,position):
	board[position] = marker
def win_check(board1,mark):
	win_check = False
	if board[1] == board[2] == board[3] == mark: 		
		win_check = True
	elif board[4]==board[5]==board[6] == mark:
		win_check = True
	elif board[7]==board[8]==board[9]== mark:
		win_check = True
	elif board[1]==board[5]==board[9] == mark:
		win_check = True
	elif board[3]==board[5]==board[7] == mark:
		win_check = True
	elif board[1]==board[4]==board[7] == mark:
		win_check = True
	elif board[2]==board[5]==board[8] == mark:	
		win_check = True
	elif board[3]==board[6]==board[9] == mark:
		win_check = True
	return win_check
def fullboard(board):
	XO =['X','O']
	if all(x in XO for x in board ):
		return True
	else: return False
def main():
	global board
	global filledpos
	print('Welcome to the game tictactoe')
	display_board(board)
	condition = True

	while True:
		firstplayer = str(input("Dear first player, what symbol would you like ?"))
		firstplayer = firstplayer.upper()
		if firstplayer in ['X','O']:
			break
		else:
			print('It has to be X or O. Invalid response')

	while condition == True:
		if firstplayer == 'X':
			print('It is X turn')
			placingposition = int(answer())
			place_marker(board,'X',placingposition)
			display_board(board)
			if fullboard(board) == True and win_check(board,'X') == False:
				condition = False
				print('That was a draw')
			elif win_check(board,'X'):
				condition = False
				print('X wins the game')
			firstplayer = 'O'
		else:
			print('It is O turn')
			placingposition =int(answer())
			place_marker(board,'O',placingposition)
			display_board(board)
			if fullboard(board) == True and win_check(board,'O') == False:
				condition = False
				print('That was a draw')
			elif win_check(board,'O'):
				condition = False
				print('O wins the game')
			firstplayer = 'X'
	
	while True:
		replay = str(input('Would like you play again ?'))
		if replay.upper() in ['Y','N']:
			break

		else:
			print('Invalid response')
	if replay.upper() == 'Y':
		board = ['X','1','2','3','4','5','6','7','8','9']
		filledpos = []
		main()
	else:
		print('Game ended')

if __name__ == '__main__':
	main()


