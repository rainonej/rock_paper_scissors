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

class Player:
	"The player is his/her own class"

	def __init__(self, name = 'Player 1'):

		self.name = name

		self.wlt = [0,0,0]

		self.history  = []

		self.streak = []


#Test player
gamer = Player('Jordan')

