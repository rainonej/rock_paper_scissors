"""Defines the main classes used here"""

class RPSgame:
	"Objects consist of the elements of the game ['ROCK', 'PAPER', 'SCISSORS'], what the winning combinations are, and possibly extra text"

	def __init__(self, name, elements):
		self.name = name
		self.elements = elements #List of ['ROCK', 'PAPER', 'SCISSORS']
		self.key = list(range(1,len(elements)+1)) #just so that the AI can choose easier
		self.return_values = self.key #these are the actual parts that get recorded and can be valid inputs in the self.outcome function

		self.rules = "You already know how to play this game." 

		self.test()

	def test(self):

		# make sure everything is the proper type
		if(type(self.elements) != list):
			print('elements are not in list form')
		#if(type(self.winners) != list):
		#	print('winners are not in list form')
		#if(type(self.winners[0]) != tuple):
		#	print('winners is not a list of tuples')

		# make sure there are no contradictions in the rules of the game

	def outcome(self, pair): #This is how each game determines the winners.s
		'beats("ROCK", "SCISSORS") = ">"  '
		#I should probably eventually have an integer version of this.

		a = pair[0]
		b = pair[1]
		c = (a - b) % 3

		if (c==1):
			return ">"
		elif(c==2):
			return "<"
		elif (c==0):
			return "="

		

#Test Game
#RPS = RPSgame('Rock, paper, scissors', ['ROCK', 'PAPER', 'SCISSORS'], [('ROCK', 'SCISSORS'), ('SCISSORS', 'PAPER'), ('PAPER', 'ROCK')] )
RPS = RPSgame('Rock, paper, scissors', ['ROCK', 'PAPER', 'SCISSORS'])
RPS.rules += " PAPER covers ROCK, SCISSORS cuts PAPER, and ROCK crushes SCISSORS."

class Player:
	"The player is his/her own class"

	def __init__(self, name = 'Player_1'): #I guess the default name thing never happens anymore

		self.name = name

		self.wlt = {'Win': 0, 'Lose': 0, 'Tie':0}

		self.history  = []

		self.streak = []

		self.winning_streak = 0

		self.high_score = 0

	def record_round(self, result, pair):
		"Records the rusults of a round"


		self.history.append(pair)
		self.wlt[result] += 1

		if (result == 'Win'):
			self.winning_streak += 1
			self.streak.append(0)

			if (self.winning_streak>self.high_score):
				self.high_score = self.winning_streak

		elif(result == 'Lose'):
			self.winning_streak =0
			self.streak.append(1)

		else:
			self.streak.append(2)

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
		return random.choice(self.game.return_values)

Default_AI = AI()
Default_AI.game = RPS

#ONLY WHEN WE NEED TO RUN THIS
import pickle
with open('list_of_games.pkl', 'wb') as output:
	pickle.dump([RPS], output, pickle.HIGHEST_PROTOCOL)

with open('list_of_AI.pkl', 'wb') as output:
	pickle.dump([Default_AI], output, pickle.HIGHEST_PROTOCOL)

#Test player
gamer = Player('Jordan')