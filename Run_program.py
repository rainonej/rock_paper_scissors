# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 00:31:15 2019

@author: Jordan
"""

"""import the list of players (and later also games and AIs), and enter it/them into the interface."""

#We need the classes to know what we're importing
import classes
from classes import *

import pickle

with open('players.pkl', 'rb') as input:
	list_of_players = pickle.load(input)

import user_interface
from user_interface import *


interface(RPS,t, list_of_players)


with open('players.pkl', 'wb') as output:
	pickle.dump(list_of_players, output, pickle.HIGHEST_PROTOCOL)
