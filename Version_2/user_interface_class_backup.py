"This is the new User Interface Class. It's so advanced that it needs it's own file"


class Interface:
	"Objects of this class will be the different skins and versions on the UI."
	def __init__(self):
		self.name = None
		self.version = 0
		self.message = "Hello!"

		#self.load_lists()

	def load_lists(self):
		"Loads the lists of things we can select from"
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
		"Plays the welcome message. Gives the selections of players, games, and AI. Gives the options menu."
		self.load_lists()

		#Obviously these are place holders
		print('Who are you?')
		self.player = player
		del self.list_of_players[player] 

		print('what game are we playing?')
		self.game = game
		del self.list_of_games[game] 

		print('who are you playing against?')
		self.AI = AI_choice


		if (selection == Options):
			self.Options()

	def Options(self):
		"This is the options menu where you can edit the players list"
		Edit the lists
		pickle dump the new lists

		print("Back to main menue?")
		if (yes):
			self.welcome()
		if (no):
			self.playing=False

	def Game_intro(self):
		"Introduces the game and give the rules"
		print("here's how the game works")
		print(self.game.rules)

	def Game_play(self):
		"The way the game works or ends. Usually this is simple, but there might be some intermitent text"
		self.playing = True
		while (self.playing == True):
			self.Round()

	def collect_input(self, options):
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

	def Round(self):
		"How each round of the game works"
		options = self.game.elements + ['QUIT']
		player_choice = self.collect_input(options)
		AI_choice = self.AI.choice()

		winner = self.game.winner(player_choice, AI_choice)

		self.record_round()

	def record_round(self):
		"how we record the data for each round. This is import for players records and for the AI learning how to win"
		self.player.record_round()
		self.AI.record_round()

	def Save_data(self):
		"Overriding the previous save files"
		self.list_of_players.append(self.player)
		self.list_of_games.append(self.game)

		pickle dump self.list_of_players as list_of_players.pkl

	def Goodbye(self):
		"The ending message"
		print('Goodbye')


	

