"""This creates the functions which allow the user to interact with the game"""

import classes
from classes import *

import game_play
from game_play import *

def interface(game):
	print('Welcome to ', game.name, "! Since you don't have an account, why don't you make one. What's your name?")
	player_name = input()

	#creates a new player
	if (player_name == ''):
		player = Player()
	else:
		player = Player(player_name)

	print("Great for you to join us ", player.name, "! Let's get started")

	# Explains how the game is played and ask for an input
	print(game.rules)
	print('Your options are: ', game.elements)
	print('Your choice is:')
	plaer_choice = input()

	#See who won
	AI_choice = gamePlay(game, player, plaer_choice)


	#Resolution message
	if (player.streak[-1] == 0):
		print('Hurray! ', plaer_choice , ' beats ' ,  AI_choice)
	elif (player.streak[-1] == 1):
		print('Boo! ', AI_choice , ' beats ' ,  plaer_choice)
	else:
		print('its a tie')





