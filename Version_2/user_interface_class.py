"This is the new User Interface Class. It's so advanced that it needs it's own file."
"The idea is to have the UI have a bunch of predefined funcitons. So to create a new UI, you just instantiate the class and only edit the functions that need changing"
"In theory, having the player, game, and AI all as atributes of the UI will slow things down, but if a human is playing, then there's no way I can make it slow enough thtat a human would notice."

import pickle
new_input = input
import classes
from classes import Human_Player 

class Interface:
	"Objects of this class will be the different skins and versions on the UI."
	def __init__(self):
		self.name = "Default UI"
		self.version = 2.0

	def load_lists(self):
		"Loads the lists of things we can select from"
		with open('players.pkl', 'rb') as input:
			list_of_players = pickle.load(input)
		with open('list_of_games.pkl', 'rb') as input:
			list_of_games = pickle.load(input)
		with open('list_of_AI.pkl', 'rb') as input:
			list_of_AI = pickle.load(input)

		self.list_of_players = list_of_players
		self.list_of_AI = list_of_AI
		self.list_of_games = list_of_games

	def Welcome(self):
		"Plays the welcome message. Gives the selections of players, games, and AI. Gives the options menu."
		#Gets the list of players, games, and AI
		self.load_lists()

		#Select the Player 
		self.select_Player()
	
		#Pick the game
		self.pick_game()

		#Pick your AI (By default we'll just have the one AI)
		self.AI = self.list_of_AI[0]

		#Outro
		self.outro()

	def select_Player(self):
		"This is how we select a player"

		#Makes a list of names to select
		self.list_of_player_names = []
		num_of_players = len(self.list_of_players)
		for i in range(0,num_of_players):
			self.list_of_player_names.append(self.list_of_players[i].name)
		opts = self.list_of_player_names + ['NEW PLAYER']
		key = list(range(1,num_of_players+1)) + ['N'] #Set the precident that nonstandard options have single capital letter keys
		#returns = key

		print('Select your player:')
		ans = self.pick_option(opts, keys = key)
		
		#Pick an existing player profile
		if (type(ans)==int): 
			i = key.index(ans)
			self.player = self.list_of_players[i]
			del self.list_of_players[i]

		#New Player
		elif(ans == 'N'):
			print('Enter your name:')
			player_name = self.get_input(forbidden = ['', 'NEW PLAYER', 'OPTIONS'])
			self.player = Human_Player(player_name)

	def pick_game(self):
		"This is how we pick the game"

		#Makes the list to select from
		list_of_game_names = []
		num_of_games = len(self.list_of_games)
		for i in range(0,num_of_games):
			list_of_game_names.append(self.list_of_games[i].name)

		#Select your game
		print('Which game are you playing?')
		ans = self.pick_option(list_of_game_names)
		self.game = self.list_of_games[ans]
		del self.list_of_games[ans]

	def outro(self):
		"This is the message the plays before the game starts"
		print('Ok', self.player.name, 'have fun playing', self.game.name, '!')

	def Options(self):
		"This is the options menu where you can edit the players list"

		#Makes a list of names to select
		list_of_players = self.list_of_players + [self.player]
		list_of_player_names = []
		num_of_players = len(list_of_players)
		for i in range(0,num_of_players):
			list_of_player_names.append(list_of_players[i].name)
		
		#Select the player
		print("Here's the list of Players to select from:")
		selected = self.pick_option(list_of_player_names)
		name = list_of_players[selected].name

		#What are we doing here?
		d = 'delete' #I don't like the see DELETE in red. It's scary
		d = d.upper()
		#s = 'select'
		#s = s.upper
		options = ['SEE HIGH SCORE', 'SEE WIN/LOSE/TIE RECORD', 'RENAME', 'SELECT NEW PLAYER', d ]

		print('What do you want to do with ', name, '?')
		ans = self.pick_option(options)

		if (ans == 0):
			print(name, "'s high score was", list_of_players[selected].high_score, 'wins in a row.')

		if (ans == 1):
			wlt = list_of_players[selected].wlt 
			print(name, "'s WIN/LOSE/TIE record is", wlt['Win'], 'wins', wlt['Lose'], 'loses, and ', wlt['Tie'], 'ties.')

		if (ans == 2):
			print('What do you want to rename', name, 'to?')
			bad = list_of_player_names
			del bad[selected]
			bad += ['', 'NEW PLAYER']
			newname = self.get_input(forbidden = bad, message = "You can't choose that name.")
			
			#Changing the name
			print('Do you really want to rename', name, 'to', newname, '?')
			confirm = self.pick_option(['YES', 'NO'])
			if (confirm == 0):
				list_of_players[selected].name = newname
				if (selected == len(list_of_players-1)): #If you selected yourself
					self.player.name = newname

		if (ans == 3):
			newplayer = list_of_players[selected]
			print('Do you really want to stop playing as', self.player.name, 'and play as', newplayer.name, 'instead?')
			confirm = self.pick_option(['YES', 'NO'])
			if (confirm == 0):
				del list_of_players[selected]
				self.player = newplayer
				list_of_players.append(self.player)
				print('Ok, you are now playing as ', self.player.name)

		if (ans == 4):
			if (selected == num_of_players-1):
				print('You cannot delete a player while their active.')
			else:
				print('Do you really want to delete', name, '?')
				confirm = self.pick_option(['YES', 'NO'])

				if (confirm == 0):
					del list_of_players[selected]
					print(name, 'was deleted.')

		#Save the changes on self file
		del list_of_players[-1]
		self.list_of_players = list_of_players

		#Back to the game
		print('Back to the game now')

	def Game_intro(self):
		"Introduces the game and give the rules"
		print("here's how the game works")
		print(self.game.rules)

	def Game_play(self):
		"The way the game works or ends. Usually this is simple, but there might be some intermitent text"
		self.playing = True
		while (self.playing == True):
			self.round()

	def get_input(self, forbidden = [], message = "That's not allowed, try again."):
		"Returns a valid input in all caps."
		choosing = True
		while (choosing == True):
			choice = input()
			choice = choice.upper()
			if (choice not in forbidden):
				choosing = False
			else:
				print(message)
		return choice

	def pick_option(self, options, keys = None, return_values = None):
		"Opitions are a list of things to choose from. Keys are the list of keys the player must press. Reuturn_values is a list of things the function will return"
		"If keys are strings, they must be capitalized!"

		"Creates the keys and return_values is they don't already exist"
		if (keys == None):
			keys = range(0,len(options))

		if (return_values == None):
			return_values = keys

		"Get's the right type"
		keys = list(map(str,keys))
		return_values = list(map(return_number, return_values))


		for i in range(0,len(options)):
			print("[", keys[i], "]", options[i])

		"collect the answer"
		choosing = True
		while (choosing == True):
			print("you select:")
			answer = new_input()
			answer = answer.upper()
			if (answer in keys):
				i = keys.index(answer)
				print('You selected ', options[i],)
				return return_values[i]
				choosing = False
			else:
				print('not a valid option')

	def round(self):
		"How each round of the game works"

		print('What do you play?')
		#Collect the input
		options =  self.game.elements + ['OPTIONS', 'SAVE AND QUIT']
		key = self.game.key + ['O', 'Q']
		#returns = self.game.return_values + ['O']
		player_choice = self.pick_option(options, keys = key) #should be an int, or a string
		self.AI_choice = self.AI.choice() #Should be an int

		if (type(player_choice)!=int): #a special answer
			if (player_choice == 'O'):
				self.Options()
			elif(player_choice == 'Q'):
				self.playing = False

		else: #a standard answer
			self.player_choice = player_choice
			outcome = self.game.outcome((self.player_choice, self.AI_choice))
			i = self.game.return_values.index(self.AI_choice)
			print('Your opponent played ', self.game.elements[i]) #this is all because I have to switch between ints and strings

			if (outcome == ">"): #Player Won
				print('Yeah you Won!')
				self.player_outcome = 'Win'
				self.AI_outcome = 'Lose'

			elif (outcome == "<"): #AI Won
				print('Boo, you Lost!')
				self.player_outcome = 'Lose'
				self.AI_outcome = 'Win'

			elif (outcome == "="): #Tie
				print('Meh, its a Tie')
				self.player_outcome = 'Tie'
				self.AI_outcome = 'Tie'

			#Recording the results
			self.record_round()

	def record_round(self):
		"how we record the data for each round. This is import for players records and for the AI learning how to win"

		#Use self.round_result
		self.player.record_round(self.player_outcome, (self.player_choice, self.AI_choice))
		self.AI.record_round(self.AI_outcome, (self.AI_choice, self.player_choice))

	def Save_data(self):
		"Overriding the previous save files"
		self.list_of_players.append(self.player)
		self.list_of_games.append(self.game)

		with open('players.pkl', 'wb') as output:
			pickle.dump(self.list_of_players, output, pickle.HIGHEST_PROTOCOL)
		""" #I guess I don't really need this right now.
		with open('list_of_games.pkl', 'wb') as output:
			pickle.dump(self.list_of_games, output, pickle.HIGHEST_PROTOCOL)
		"""
			
	def Goodbye(self):
		"The ending message"
		print('Goodbye')


def return_number(s):
	try:
		int(s)
		return int(s)
	except ValueError:
		return str(s) 

#UI = Interface()
#UI.Welcome()