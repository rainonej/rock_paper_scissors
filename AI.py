import classes
from classes import *

Default_AI = AI()
Default_AI.game = RPS


#Here's the first not completely random 'AI'. It's really a test AI since it should come from recorded human data
from types import MethodType

PizzaExpert = AI()
PizzaExpert.game = RPS
PizzaExpert.count = 6

with open("data.txt", "r") as f:
    datum = f.readlines()

def translate(letter):
	if (letter == 'p'):
		return 'PAPER'
	elif (letter == 'x'):
		return 'SCISSORS'
	elif (letter == 's'):
		return 'ROCK'

def eat_pizza(self):
	while ((datum[self.count][0] != 'p') and  (datum[self.count][0] != 'x') and (datum[self.count][0] != 's')):
		self.count += 1

	output = translate(datum[self.count][0])
	self.count += 1
	return output

PizzaExpert.choice = MethodType(eat_pizza, PizzaExpert)



