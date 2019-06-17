import user_interface_class
from user_interface_class import *

Default_UI = Interface()

from types import MethodType

Fantasy_skin = Interface()

def fantasy_intro(self):
	self.game.name = 'Fantasy fighting'
	self.version = 1.0
	#self.blah = 'blahblahblah'
	self.game.elements = ['SWORD', 'SHIELD', 'MAGIC']
	self.game.rules = 'SHEILD blocks SWORD, SWORD stabs MAGIC user, MAGIC is not blocked by a SHIELD'
	print('Hello brave adventurer,', self.player.name, 'Welcome to Fantasy Land!')
	print(self.game.rules)

Fantasy_skin.Game_intro = MethodType(fantasy_intro, Fantasy_skin)



"version 1.1"

Fantasy_skin2 = Interface()

def newSetup(self):
	"We can start to reskin it from the begining"

	#Gets the list of players, games, and AI
	self.load_lists()

	#Preselects the game
	#Only works if there is only one game here
	self.game = self.list_of_games[0]
	self.game.name = 'Fantasy fighting'
	self.game.elements = ['SWORD', 'SHIELD', 'MAGIC']
	self.game.rules = 'SHEILD blocks SWORD, SWORD stabs MAGIC user, MAGIC is not blocked by a SHIELD'
	self.enemy = None
	print('I set enemy to None')
	self.list_of_games = [self.game] #so the Welcome function works correctly

	#UI info
	self.name = 'Fantasy Skins'
	self.version = 1.1

Fantasy_skin2.Setup = MethodType(newSetup, Fantasy_skin2)


def newOutro(self):
	"Defines a bunch of new values"

	if ('MaxHP' not in self.player.stats):
		self.player.stats['MaxHP'] = 10
		self.player.MaxHP = 10

	if ('HP' not in self.player.stats):
		self.player.stats['HP'] = self.player.stats['MaxHP']
	self.player.stats['HP'] = self.player.stats['MaxHP']

	if ('exp' not in self.player.stats):
		self.player.stats['exp'] = 0



	"""
	try:
		self.player.Enemy
	except AttributeError:
		self.player.Enemy = None
	""" #I just want to keep this code to remind me how AttributeError works

	if ('tracker' not in self.player.stats):
		self.player.stats['tracker'] = 1
	else:
		self.player.stats['tracker'] += 1



	self.player_name = 'Adventuerer ' + self.player.name

	print('Good luck brave',  self.player_name, '! And have fun on your quest!')
	print("You've played this", self.player.stats['tracker'], 'times')

Fantasy_skin2.outro = MethodType(newOutro, Fantasy_skin2)


def fantasy_intro2(self):
	self.game.name = 'Fantasy fighting'
	self.version = 1.1
	self.game.elements = ['SWORD', 'SHIELD', 'MAGIC']
	self.game.rules = 'SHEILD blocks SWORD, SWORD stabs MAGIC user, MAGIC is not blocked by a SHIELD'
	self.enemy = None
	print('Hello brave adventurer,', self.player.name, 'Welcome to Fantasy Land!')
	print(self.game.rules)

Fantasy_skin2.Game_intro = MethodType(fantasy_intro2, Fantasy_skin2)

import classes
from classes import *
import random
def buildEnemy(MaxHP):
	Enemy = AI()
	Enemy.name = random.choice(['Womp-Womp', "Flak'r", 'Gysiny'])
	Enemy.stats['MaxHP'] = MaxHP
	Enemy.stats['HP'] = MaxHP
	return Enemy

def newGame_play(self):
	"The way the game works or ends. Usually this is simple, but there might be some intermitent text"

	self.playing = True
	while (self.playing == True):

		#do they have a current enemey? If no, then create one
		#it's attatched to the player, because that would be too heavy. It's attached to the UI (more like an engine)
		if (self.enemy == None):
			"Build one"
			Enemy = buildEnemy(3)
			self.enemy = Enemy
			print('A new enemy', self.enemy.name, 'appeared!')


		#Show current Health
		print('Your Health (', self.player.stats['HP'], '/', self.player.stats['MaxHP'], ')')
		print('Enemy Health (', self.enemy.stats['HP'], '/', self.enemy.stats['MaxHP'], ')')

		self.round()

		#Check to see who won and update stats
		if (self.player_outcome == 'Win'):
			self.enemy.stats['HP'] -= 1
		if (self.player_outcome == 'Lose'):
			self.player.stats['HP'] -= 1

		if (self.player.stats['HP'] <= 0):
			"Game Over"
			print('The', self.enemy.name, 'killed you!')

			#I don't know how to wrap it up
			self.player.stats['HP'] = self.player.stats['MaxHP']

		if (self.enemy.stats['HP'] == 0):
			"You won"
			print('Hurray, you slayed the enemy', self.enemy.name, '!')
			self.player.stats['exp'] += 1
			self.enemy = None



Fantasy_skin2.Game_play = MethodType(newGame_play, Fantasy_skin2)
