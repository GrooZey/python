import random

def guess():
	myst = random.randint(0,100)
	devine = -1
	while(devine != myst):
		print('Guess my number between 0 and 100 ?')
		devine = int(input())
		if(devine<myst):
			print('Higher !')
		elif(devine>myst):
			print('Lower!')
		else:
			print('Congratulations !')

guess()