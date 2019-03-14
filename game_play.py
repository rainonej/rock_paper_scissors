"""This is the file where we define how the game is played"""



def gamePlay(game, player, player_choice, AI):
	"A function which takes in a game, a player, and a player input and determines who wins and updates the 'score cards' "

	#Where the future AT will go
	AI_choice = AI.choice()


	#where we determins who won
	outcome = 2
	if ((player_choice, AI_choice) in game.winners):
		outcome = 0 #Player Wins!
	elif ((AI_choice, player_choice) in game.winners):
		outcome = 1 #AI wins
	else:
		outcome = 2 #It's a TIE

	#where ths 'score cards' get updated (but only if the player want's it to be updated)
	if (player.record == True):

		player.wlt[outcome] += 1
		player.streak.append(outcome)
		player.history.append((player_choice, AI_choice))

	if (AI.record == True):

		outcome = switch_outcome(outcome)
		AI.wlt[outcome] += 1
		AI.streak.append(outcome)
		AI.history.append((AI_choice, player_choice))


	#this should probably be a list pairs of numbers, to make the AI's life easier in the future.


	#returns the choice
	return AI_choice

def switch_outcome(n):
	if (n == 0):
		return 1
	elif (n == 1):
		return 0
	elif:
		return 2
