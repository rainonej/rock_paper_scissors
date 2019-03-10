# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 00:31:15 2019

@author: Jordan
"""

"""import the list of players (and later also games and AIs), and enter it/them into the interface."""

import classes
from classes import *

import pickle

with open('players.pkl', 'rb') as input:
	player = pickle.load(input)

import user_interface
from user_interface import *

#import AI
#from AI import *

#RPS = RPSgame('Rock, paper, scissors', ['ROCK', 'PAPER', 'SCISSORS'], [('ROCK', 'SCISSORS'), ('SCISSORS', 'PAPER'), ('PAPER', 'ROCK')] )

#write into the shell interface(RPS, t)
interface(RPS,t, player)


with open('players.pkl', 'wb') as output:
	pickle.dump(player, output, pickle.HIGHEST_PROTOCOL)
