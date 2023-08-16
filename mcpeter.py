import random as r
import os

def play():
	pround = 1
	while pround <= 20:
		coin = r.choice(['heads','tails'])
		#~print('\t',pround,coin)
		if coin == 'heads':
			pround += 1
		else:
			return 2**pround
	return 2**20

if __name__=="__main__":
	
	BET = 25
	
	iterations = 10000000
	total_win = 0
	max_win = 0
	cnt_win = 0
	for i in range(0,iterations):
		if i%10000 == 0:
			os.system('clear')
			print(round(i/iterations,2))
		#~print('Iteration',i+1)
		win = play()
		if win > BET:
			cnt_win += 1
		max_win = max(max_win,win)
		#~print('\t\t',win)
		total_win += win
	print('Bet:',BET)
	#~print('Max win:',max_win)
	#~print('Total win:',total_win)
	#~print('Total bank:',BET*iterations-total_win)
	print('Average win:',total_win/iterations)
	print('Average bank:',(BET*iterations-total_win)/iterations)
	print('Winning rounds:',cnt_win/iterations)
