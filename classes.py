"""Defines the main classes used here"""

class RPSgame:
	"Objects consist of the elements of the game ['ROCK', 'PAPER', 'SCISSORS'], what the winning combinations are, and possibly extra text"

	def __init__(self, name, elements, winners):
		self.name = name
		self.elements = elements
		self.winners = winners #of 

		self.rules = "You already know how to play this game." 

		self.test()

	def test(self):

		# make sure everything is the proper type
		if(type(self.elements) != list):
			print('elements are not in list form')
		if(type(self.winners) != list):
			print('winners are not in list form')
		if(type(self.winners[0]) != tuple):
			print('winners is not a list of tuples')

		# make sure there are no contradictions in the rules of the game



#Test Game
RPS = RPSgame('Rock, paper, scissors', ['ROCK', 'PAPER', 'SCISSORS'], [('ROCK', 'SCISSORS'), ('SCISSORS', 'PAPER'), ('PAPER', 'ROCK')] )
RPS.rules += " PAPER covers ROCK, SCISSORS cuts PAPER, and ROCK crushes SCISSORS."

class Player:
	"The player is his/her own class"

	def __init__(self, name = 'Player_1'): #I guess the default name thing never happens anymore

		self.name = name

		self.wlt = [0,0,0]

		self.history  = []

		self.streak = []

class Human_Player(Player):
	"A subclass exclussively for Human Players"

	def __init__(self, name):
		super().__init__()
		self.name = name
		self.record = True

	def choice(self): #this will make the AI's and the players more similar
		return input()



import random  #  for the current 'AI' to work

class AI(Player):
	"the AI that will make a choice"

	def __init__(self):
		super().__init__()
		self.record = False

	#This is the default choice. We can override this choice with a more sophisticated AI
	def choice(self):
		return random.choice(self.game.elements)

Default_AI = AI()
Default_AI.game = RPS

#Test player
gamer = Player('Jordan')

