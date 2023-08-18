import random as r
import os

def playRound():
	# Wurfzähler
	flip_cnt = 1
	while True:
		# Münzwurf: Kopf / Zahl
		coin = r.choice(['heads','tails'])
		# Zahl? - Ein neuer Wurf
		if coin == 'tails':
			flip_cnt += 1
		# Kopf? - Gewinn: 2^[Anzahl der Münzwürfe]
		else:
			return 2**flip_cnt

if __name__=="__main__":
	
	# Teilnahmegebühr
	BET = 100
	# Gewinnziel
	GOAL = 1_000_000
	# Startkapital
	PURSE = 0
	
	min_purse = 0
	max_win = 0
	round_count = 0
	
	while PURSE < GOAL:
		PURSE -= BET
		min_purse = min(PURSE, min_purse)
		round_count += 1
		
		# ~ if round_count%10000 == 0:
			# ~ os.system('clear')
			# ~ print('Runde:',f'{round_count:,}')
		
		win = playRound()
		PURSE += win
		max_win = max(win, max_win)
		
	# ~ os.system('clear')
	
	print('Teilnahmegebühr:       ',f'{BET: >15,}','€')
	print('Gewinnziel:            ',f'{GOAL: >15,}','€')
	print('-'*41)
	print('Runden:                ',f'{round_count: >15,}')
	print('Gewinn:                ',f'{PURSE: >15,}','€')
	print('-'*41)
	print('Beste Runde:           ',f'{max_win: >15,}','€')
	print('Niedrigster Kontostand:',f'{min_purse: >15,}','€')
