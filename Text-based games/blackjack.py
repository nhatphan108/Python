money = 100000
values = {}
for i in range (2,11):
	values[str(i)] = i
values.update({'A':10,'J':10,'Q':10,'K':10})
randomlist = ['A','J','Q','K','2','3','4','5','6','7','8','9','10']
dealercard = []
playercard = []
print('Welcome to the BlackJack Game')
name = input('May I have your name please')
import random
def sumlist(list):
	global values
	t = 0
	
	for i in list:
		something = values.get(i)
		if i != 'A':
			t += something
		else:
			if len(list) < 3:
				t+= 10
			else: t+= 1
	return t
def dealcard(list):
	global values
	m = random.choice(randomlist)
	list.append(m)
def replay():
	answer = input('Do you wanna replay the game again? (Y/N):')
	answer = answer.upper()	
	if answer == 'Y':
		main()
	elif answer == 'N':
		pass
def check_blackjack(list):
	if list[0] in ['J','Q','K','10'] and list[1] == 'A':
		return True
	elif list[0] == 'A' and list[1] in ['J','Q','K','10']:
		return True
	else: return False
def check_win(player,dealer,x):
	global money
	global name
	if sumlist(player) == sumlist(dealer):
		print('This game was a draw')
	elif sumlist(player) > 21 and sumlist(dealer) > 21:
		print('This game was a draw')
	elif sumlist(player) > 21 and sumlist(dealer) < 21:
		print(name, 'loses the game and' ,x,'just went out of their bank')
		money -= x
		print(name, ' has',money,' dollars left')
	elif sumlist(player) < 21 and sumlist(dealer) > 21:
		print(name, 'wins the game and' ,x,'just went into their bank')
		money += x
		print(name, ' has',money,' dollars left')
	elif  sumlist(player) > sumlist(dealer):
		print(name, 'wins the game and' ,x,'just went into their bank')
		money += x
		print(name, ' has',money,' dollars left') 
	elif sumlist(dealer) > sumlist(player):
		print(name, 'loses the game and' ,x,'just went out of their bank')
		money -= x
		print(name, ' has',money,' dollars left')

def main():
	global money
	global name
	dealercard = []
	playercard = []
	contin = True
	print('You currently have',money,' in your bank account')
	x = input('Please put in the amount of money you would like to bet')
	x = int(x)
	dealcard(dealercard)
	dealcard(dealercard)
	dealcard(playercard)
	dealcard(playercard)
	print('You are dealt with' ,playercard[0],' and',playercard[1])
	print('The cocky dealer shows his first card:',dealercard[0])
	if check_blackjack(dealercard) and check_blackjack(playercard):
		print('That was really close. Both the player and dealer have blackjacks. The game is over')
		contin = False
	elif check_blackjack(dealercard):
		print('The dealer wins by blackjack')
		print('The dealer cards are',dealercard[0], ' and',dealercard[1])
		contin = False
		money -= x
	elif check_blackjack(playercard):
		print('Player ',name,'wins by Blackjack')
		contin = False
		money += x
	contin2 = True
	while contin2:
		response = input('Would you like to hit or stand ?')
		if response == 'hit':
			dealcard(playercard)
			print('You are dealt with', playercard[-1])
			print('The cards you have right now are',' '.join(playercard))
			if len(playercard) == 5:
				contin2 = False
		elif response == 'stand':
			print(' The total of your card values are',sumlist(playercard))
			contin2 = False
	if contin == True:	
		while sumlist(dealercard) < 17:
			dealcard(dealercard)
	if contin == True:
		print('The card the dealer have are', ' '.join(dealercard))
		print('The total value of dealers\' cards are',sumlist(dealercard))
		check_win(playercard,dealercard,x)
	print('Player',name,'has',money,'dollars left in your account')
	replay()
if __name__ == "__main__":
	main()

