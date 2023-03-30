import random

def chain_tronc(n):
	word = ""
	for i in range(n):
		word+="*"
	return word
	
def chain(n):
	word = ""
	for i in range(n):
		rnd = random.random()
		if (rnd<=0.2):
			word+="0"
		else:
			word+="*"
	return word
	
def chain2_tronc(spaces,n):
	word=""
	for i in range(spaces):
		word+=" "
	word+=chain_tronc(n)
	return word

def chain2(spaces,n):
	word=""
	for i in range(spaces):
		word+=" "
	word+=chain(n)
	return word

def column(n):
	for i in range(10):
		print(chain(n))
	return None

def diagonal1(n):
	word=""
	for i in range(n):
		word+=chain(i+1)
		print(word)
		word=""
	return None
			
def diagonal2(n):
	word=""
	for i in range(n):
		word+=chain(n-i-1,i+1)
		print(word)
		word=""
	return None

def christmas_tree(n):
	word=""
	for i in range(n):
		word+=chain2(n-i-1,i+1)
		word+=chain(i)
		print(word)
		word=""
	print(chain2_tronc(n-2,3))
	return None

christmas_tree(10)

