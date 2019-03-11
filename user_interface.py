"""This creates the functions which allow the user to interact with the game"""

import classes
from classes import *

import game_play
from game_play import *

new_input = input

def interface(game, AI, list_of_players):

	print('Welcome to ', game.name, "Are you ", list_of_players[-1].name, "? [y] or [n]")

	ans = new_input()
	if (ans == 'y'):
		player = list_of_players[-1]
		del list_of_players[-1]
		print('Welcome back ', player.name)
	else: 
		#select the player from a list

		#Create list of player names for the input function
		list_of_player_names = []
		for i in range(0,len(list_of_players)):
			list_of_player_names.append(list_of_players[i].name)

		#select your save file
		print('Select your file from the list or select NEW PLAYER.')
		ans = collect_input(list_of_player_names + ['NEW PLAYER'])

		if ans in range(0, len(list_of_player_names)):
			player = list_of_players[ans]
			del list_of_players[ans]

		else:
			print('Enter your name:')

			#Make sure they pick a valid name
			choosing = True
			while (choosing == True):
				player_name = new_input()
				player_name = player_name.upper()
				if (player_name in list_of_player_names + ['NEW PLAYER', '']):
					print("You can't pick that name, try again.")
				else:
					player = Player(player_name)
					choosing = False


	print("Great for you to join us ", player.name, "! Let's get started")

	# Explains how the game is played 
	print(game.rules)
	
	#theis is the actual game part

	playing = True #setting up a condition to exit the loop
	while(playing == True):

		print("Type 'quit' to quit")
		temp = game.elements + ['QUIT']
		player_choice = collect_input(temp)
		player_choice = temp[player_choice]


		#If the player decided to quit the game
		if (player_choice == 'QUIT'):
			playing = False
		
		#If they made a valid choice, then we see who won.
		else:
			#player_choice = game.elements[player_choice]
			AI_choice = gamePlay(game, player, player_choice, AI)

			#Resolution message
			if (player.streak[-1] == 0):
				print('Hurray! ', player_choice , ' beats ' ,  AI_choice)
			elif (player.streak[-1] == 1):
				print('Boo! ', AI_choice , ' beats ' ,  player_choice)
			else:
				print('its a tie')


	list_of_players.append(player)
	print('your record is', player.wlt)


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

