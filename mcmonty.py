# A Monte-Carlo-Simulation for the Monty-Hall-Problem

import random

class MCMonty():
	
	def __init__(self,strategy = None, verbose = False):
		if strategy in ['stay','switch','random']:
			self.verbose = verbose
			self.strategy = strategy
			self.doors = self.fillDoors(3)
			self.open_door = None
			
			self.player = self.pickDoor()
			self.openDoor()
			if self.verbose:
				print('Strategy:',self.strategy)
			if self.strategy == 'random':
				self.strategy = random.choice(['stay','switch'])
			if self.strategy == 'switch':
				self.player = self.pickDoor()
			if self.doors[self.player] == 'car':
				self.win = True
			else:
				self.win = False
			if self.verbose:
				print('Win:',self.win)
		else:
			print('Choose a strategy: stay, switch or random')
		
	def fillDoors(self, number_of_doors):
		doors = {}
		for i in range(1,number_of_doors+1):
			doors[i] = 'goat'
		doors[random.choice(list(doors.keys()))] = 'car'
		
		if self.verbose:
			print('Doors:',doors)
			
		return doors
		
	def pickDoor(self):
		if not self.open_door:
			door = random.choice(list(self.doors.keys()))
		else:
			door = self.player
			while door == self.player or door == self.open_door:
				door = random.choice(list(self.doors.keys()))
		if self.verbose:
			print('Pick:',door)
			
		return door
			
	def openDoor(self):
		open_door = False
		while open_door == self.player or not open_door:
			open_door = random.choice(list(self.doors.keys()))
			if self.doors[open_door] == 'car':
				open_door = False
				
		if self.verbose:
			print('Open:',open_door)
				
		self.open_door = open_door
			

def simulate(strategy = 'random', iterations = 1000):
	foo = { 'win' : 0, 'lose' : 0}
	for i in range(0,iterations):
		m = MCMonty(strategy)
		if m.win:
			foo['win'] += 1
		else:
			foo['lose'] += 1
	foo['win'] = round(foo['win']/iterations,4)
	foo['lose'] = round(foo['lose']/iterations,4)
	return foo


if __name__=="__main__":
	iterations = 10000
	simulation = simulate(strategy = 'switch', iterations = iterations)
	print('switch x',iterations)
	print('win:',simulation['win'],sep='\t')
	print('lose:',simulation['lose'],sep='\t')
	print()
	simulation = simulate(strategy = 'stay', iterations = iterations)
	print('stay x',iterations)
	print('win:',simulation['win'],sep='\t')
	print('lose:',simulation['lose'],sep='\t')
	print()
	simulation = simulate(strategy = 'random', iterations = iterations)
	print('random x',iterations)
	print('win:',simulation['win'],sep='\t')
	print('lose:',simulation['lose'],sep='\t')
