"""This is the file where we define how the game is played"""

import random  #  for the current 'AI' to work



def gamePlay(game, player, player_choice):
	"A function which takes in a game, a player, and a player input and determines who wins and updates the 'score cards' "

	#Where the future AT will go
	AI_choice = random.choice(game.elements)


	#where we determins who won
	outcome = 'TIE'
	if ((player_choice, AI_choice) in game.winners):
		outcome = 'player_wins'
	elif ((AI_choice, player_choice) in game.winners):
		outcome = 'AI_wins'
	else:
		outcome = 'TIE'


	#where ths 'score cards' get updated
	if (outcome == 'player_wins'):
		player.wlt[0] += 1
		player.streak.append(0)
	elif (outcome == 'AI_wins'):
		player.wlt[1] += 1
		player.streak.append(1)
	else:
		player.wlt[2] += 1
		player.streak.append(2)


	#Updating the records
	player.history.append((player_choice, AI_choice))
	#this should probably be a list pairs of numbers, to make the AI's life easier in the future.


	#returns the choice
	return AI_choice

