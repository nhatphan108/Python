import os
import random
import string
theman = ["","","","","",""]
alphabet = list(string.ascii_lowercase)
definition  = {'python':'Most Basic Programming Language','jonathan the husky':'Uconn\'s mascot','university of connecticut':'The Best University in the World','thanksgiving':'The holiday that you would gain 20 pounds before Christmas','badminton':'The fastest sports in the world','conor mcgregor':'The cockiest Irish boxer in UFC','mac donalds':'The most American fast food place you could go to','tailgate':'Best place people could go to before a footgame game','donald trump':'The \'best\' president of the US so far','stand by me':'The best song ever sung by Ben E King','hypertropy training':'The type of training in bobybuilding that emphais is placed on high volume and rep range','christmas':'Best Holiday during the year','undercut':'The popular haircut amongst male in which the sides are cleanly shaved'}
choices = list(definition.keys())
body = ['O','-','|','-','/','\\']
n = 0
def hangman(list):
	os.system('clear')
	print(' __________________________')
	print(' |			|')
	print(' |		       ',list[0])
	print(' |		     ',list[1],list[2],list[3])
	print(' |		      ',list[4],list[5])
	print(' |')
	print(' |')
	print(' |')
	print(' |')
	print('/ \\')
def fillin(line,word,mistakes):
	global theman
	global alphabet
	global body
	global n
	while True:
		response = input('What would be your guess?').lower()
		if response in alphabet:
			break
		else:
			pass
	if response not in word:
		try: 
			mistakes.append(response)
			theman[n] = body[n]
			n += 1
		except IndexError:
			pass
	else:
		for i in word:
			if i.lower() == response:
				position = word.index(i)
				line[position] = response
				word[position] =" "
	hangman(theman)
	print(" ".join(line))
	print('The mistakes you have made:',mistakes)

def replay():
	global theman
	global n
	y = input('Would you want to try again?(y/n)').lower()
	if y == 'y':
		n = 0
		theman = [ "","","","","",""]
		main()
	elif y == 'n':
		pass		


def main():
	global theman
	global definition	
	global choices
	n = 0
	contin = True
	word = random.choice(choices)
	choices.remove(word)
	parts = list(word)
	line = []
	mistakes = []
	for i in parts:
		if i.lower() in alphabet:
			line.append('_')
		else:
			line.append(' ')
	hangman(theman)
	print('Hint: ',definition.get(word))
	print(" ".join(line))
	while True:
		if len(mistakes) == 7:
			print('I\'m sorry that you have lost the game')
			break
		elif "".join(line) == word :
			print('Congratulations! You just won the game')
			break
		else:
			fillin(line,parts,mistakes)
				
	replay()
			
if __name__ == '__main__':
	main()
