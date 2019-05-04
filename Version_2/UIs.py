import user_interface_class
from user_interface_class import *

Default_UI = Interface()

from types import MethodType

Fantasy_skin = Interface()

def fantasy_intro(self):
	self.game.name = 'Fantasy fighting'
	self.game.elements = ['SWORD', 'SHIELD', 'MAGIC']
	self.game.rules = 'SHEILD blocks SWORD, SWORD stabs MAGIC user, MAGIC is not blocked by a SHIELD'
	print('Hello brave adventurer,', self.player.name, 'Welcome to Fantasy Land!')
	print(self.game.rules)

Fantasy_skin.Game_intro = MethodType(fantasy_intro, Fantasy_skin)