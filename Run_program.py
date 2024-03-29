# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 00:31:15 2019

@author: Jordan
"""

"""import the list of players (and later also games and AIs), and enter it/them into the interface."""

#We need the classes to know what we're importing
import classes
from classes import *

#Gives the list of all players and their records
import pickle
with open('players.pkl', 'rb') as input:
	list_of_players = pickle.load(input)

#Loads the User Interface
import user_interface
from user_interface import *

#Plays Rock Paper Scissors with the computer choosing at random.
interface(RPS, Default_AI, list_of_players)

#defines a function so I can play the game again without restarting the program
def playgame(): 
	interface(RPS, Default_AI, list_of_players)


#when the game is over, this saves the data
with open('players.pkl', 'wb') as output:
	pickle.dump(list_of_players, output, pickle.HIGHEST_PROTOCOL)

"""
with open("data.txt", "r") as f:
    datum = f.readlines()
 
for line in datum:
    words = line.split()
    print(words)
"""