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

	def outcome(self, pair):
		'beats("ROCK", "SCISSORS") = ">"  '
		#I should probably eventually have an integer version of this.

		opposite_pair = (pair[1], pair[0])
		if (pair in self.winners):
			return ">"
		elif (opposite_pair in self.winners):
			return "<"
		else:
			return "="


		

#Test Game
RPS = RPSgame('Rock, paper, scissors', ['ROCK', 'PAPER', 'SCISSORS'], [('ROCK', 'SCISSORS'), ('SCISSORS', 'PAPER'), ('PAPER', 'ROCK')] )
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
		return random.choice(self.game.elements)

Default_AI = AI()
Default_AI.game = RPS

#Test player
gamer = Player('Jordan')

import pickle

class Interface:
	"Objects of this class will be the different skins and versions on the UI."
	def __init__(self):
		self.name = None
		self.version = 0
		self.message = "Hello!"

		#self.load_lists()

	def load_lists(self):
		with open('players.pkl', 'rb') as input:
			list_of_players = pickle.load(input)
		with open('list_of_games.pkl', 'rb') as input:
			list_of_games = pickle.load(input)
		with open('list_of_AI.pkl', 'rb') as input:
			list_of_AI = pickle.load(input)

		self.list_of_players = list_of_players
		self.list_of_AI = AI
		self.list_of_games = list_of_games



	def welcome(self):
		"Loads the list of Players, Games, and AI's. It presents the most recent option, then give you new options"
		self.load_lists()
		print('how do you do?')




#This is going to cause a problem with being defined in two places at once
def collect_input(options):
	"options should be given in all caps."
	#list off the options
	#num_options = list(enumerate(options))
	numbers = []
	for i in range(0,len(options)):
		print("[", i, "]", options[i])
		numbers.append(str(i))

	#collect the answer
	choosing = True
	while (choosing == True):
		print("you select:")
		answer = new_input()
		answer = answer.upper()
		if (answer in options):
			return options.index(answer)
			choosing = False
		elif(answer in numbers):
			return int(answer)
			choosing = False
		else:
			print('not a valid option')

