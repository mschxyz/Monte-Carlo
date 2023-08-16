import random

def throw():
	return (random.randint(1,6),random.randint(1,6))

if __name__=="__main__":
	
	iterations = 1_000_000
	
	win = 0
	lose = 0
	for i in range(0,iterations):
		initial = sum(throw())
		if initial in {7,11}:
			win += 1
		elif initial in {2,3,12}:
			lose += 1
		else:
			new = None
			while new not in {initial,7}:
				new = sum(throw())
			if new == initial:
				win += 1
			elif new == 7:
				lose += 1
	print('Total:',iterations)
	print('Win:',win/iterations)
	print('Lose:',lose/iterations)
				
