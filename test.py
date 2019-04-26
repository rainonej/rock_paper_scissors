"Testing some stuff"
#NOT DONE YET!!! THERE WILL BE A LOT OF ERRORS IF I TRY TO RUN THE CODE NOW! DON'T DO IT UNTIL THIS IS FIXED
#NEED TO FIGURE OUT THE ARCHETECTURE OF THIS NEW DESIGN

import pickle
import classes 
from classes import *

from types import MethodType

new_input = input

def welcomen(self):
	"This is the new welcome script"
	
	self.load_lists()

	#recent_player = self.list_of_players[-1]
	print(self.message)
	print('Are you', self.list_of_players[-1].name, '?')

	ans = new_input()
	if (ans == 'y'):
		player = self.list_of_players[-1]
		del list_of_players[-1]
		print('Welcome back ', player.name)
	else: 
		#select the player from a list

		#Create list of player names for the input function
		list_of_player_names = []
		for i in range(0,len(self.list_of_players)):
			list_of_player_names.append(self.list_of_players[i].name)


		#select your save file
		print('Select your file from the list or select NEW PLAYER.')
		ans = collect_input(list_of_player_names + ['NEW PLAYER'] + ['OPTIONS'])

		if ans in range(0, len(list_of_player_names)):
			player = self.list_of_players[ans]
			del self.list_of_players[ans]

		elif(ans == len(list_of_player_names):
			print('Enter your name:')

			#Make sure they pick a valid name
			choosing = True
			while (choosing == True):
				player_name = new_input()
				player_name = player_name.upper()
				if (player_name in list_of_player_names + ['NEW PLAYER', '']):
					print("You can't pick that name, try again.")
				else:
					player = Human_Player(player_name)
					choosing = False
#NOT DONE YET!!! THERE WILL BE A LOT OF ERRORS IF I TRY TO RUN THE CODE NOW! DON'T DO IT UNTIL THIS IS FIXED
		elif(ans == len(list_of_player_names)+1): #Opens the options menu
			'''The options should be to clear the player list, view scores, change games and AI's, etc...
			But it doesn't exist yet'''
			print("The OPTIONS menu doesn't exist yet")
UI = Interface()
UI.welcome = MethodType(welcomen, UI)

list_of_games = [RPS] 
with open('list_of_games.pkl', 'wb') as output:
	pickle.dump(list_of_games, output, pickle.HIGHEST_PROTOCOL)

list_of_AI = [Default_AI] 
with open('list_of_AI.pkl', 'wb') as output:
	pickle.dump(list_of_AI, output, pickle.HIGHEST_PROTOCOL)

A = UI.welcome()