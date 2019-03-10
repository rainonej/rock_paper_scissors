"""This creates the functions which allow the user to interact with the game"""

import classes
from classes import *

import game_play
from game_play import *

new_input = input

#import pickle

def interface(game, AI, player):

	#with open('players.pkl', 'rb') as input:
	#	previous_player = pickle.load(input)

	print('Welcome to ', game.name, "Are you ", player.name, "? [y] or [n]")
	ans = new_input()
	#ans = 0
	if (ans == 'y'):
		print('Welcome back ', player.name)
	else:
		print("Since you don't have an account, why don't you make one. What's your name?")
		player_name = new_input()

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
	plaer_choice = new_input()

	#See who won
	AI_choice = gamePlay(game, player, plaer_choice, AI)


	#Resolution message
	if (player.streak[-1] == 0):
		print('Hurray! ', plaer_choice , ' beats ' ,  AI_choice)
	elif (player.streak[-1] == 1):
		print('Boo! ', AI_choice , ' beats ' ,  plaer_choice)
	else:
		print('its a tie')

	#with open('players.pkl', 'wb') as output:
	#	pickle.dump(player, output, pickle.HIGHEST_PROTOCOL)


	#print(player.wlt)





