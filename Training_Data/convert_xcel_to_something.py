import numpy as np
import pickle

#A = np.loadtxt("Rock_Paper_Scissors_Raw.txt", dtype = list, comments = '#', delimiter = ',', usecols = (0,1,2,3))
A = np.loadtxt("Rock_Paper_Scissors_Raw.txt", dtype = int, comments = '#', delimiter = ',', usecols = (0,1,2,3), ndmin = 2)

with open('Rock_Paper_Scissors_Raw.pkl', 'wb') as output:
	pickle.dump(A, output, pickle.HIGHEST_PROTOCOL)

'''The data is now in a pkl file, stored as a list of lists. Each row looks like this: 
[game_id,game_round_id,player_one_throw,player_two_throw]
We don't know what 1, 2, and 3 represent. Or even which one beats which.
We do know that game_rounds can't end in a tie, and a game lasts until there are 3 wins, or someone walks away.'''