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

		print("select your file from the list or type in a name you don't see")
		for i in range(0,len(list_of_players)):
			print("[", i, "]", list_of_players[i].name)
		#print("[", len(list_of_players)+1, "] New Player")

		ans = new_input()
		if (int(ans) in range(0, len(list_of_players))):
			player = list_of_players[int(ans)]
			del list_of_players[int(ans)]
		else:
			player = Player(ans)

	print("Great for you to join us ", player.name, "! Let's get started")

	# Explains how the game is played 
	print(game.rules)
	

	#theis is the actual game part


	playing = True #setting up a condition to exit the loop
	while(playing == True):

		print('Your options are: ', game.elements)
		print("Type 'q' to quit")
		print('Your choice is:')
		player_choice = new_input()
		player_choice = player_choice.upper() #makes it the same case

		if (player_choice != 'Q'):

			#See who won
			AI_choice = gamePlay(game, player, player_choice, AI)

			#Resolution message
			if (player.streak[-1] == 0):
				print('Hurray! ', player_choice , ' beats ' ,  AI_choice)
			elif (player.streak[-1] == 1):
				print('Boo! ', AI_choice , ' beats ' ,  player_choice)
			else:
				print('its a tie')
		else:
			playing = False


	list_of_players.append(player)
	print('your record is', player.wlt)

