import numpy as np
#import pickle

#A = np.loadtxt("Rock_Paper_Scissors_Raw.txt", dtype = list, comments = '#', delimiter = ',', usecols = (0,1,2,3))
A = np.loadtxt("Rock_Paper_Scissors_Raw.txt", dtype = int, comments = '#', delimiter = ',', usecols = (2), ndmin = 1)
B = np.loadtxt("Rock_Paper_Scissors_Raw.txt", dtype = int, comments = '#', delimiter = ',', usecols = (3), ndmin = 1)

#with open('Rock_Paper_Scissors_Raw.pkl', 'wb') as output:
#	pickle.dump(A, output, pickle.HIGHEST_PROTOCOL)

'''The data is now in a pkl file, stored as a list of lists. Each row looks like this: 
[game_id,game_round_id,player_one_throw,player_two_throw]
We don't know what 1, 2, and 3 represent. Or even which one beats which. 
But presumebly 0 means the contestant didn't enter a input, thus walks away. 
They can also both walk away at the same time.
We do know that game_rounds can't end in a tie, and a game lasts until there are 3 wins, or someone walks away.'''


def get_frequency(data, options):
	length = len(data)
	frequency = {}

	for opt in options: #labeling each option
		frequency[opt] = 0

	for j in range(0,length): #Counting each option
		frequency[data[j]] += 1

	for opt in options:
		frequency[opt] = frequency[opt]/length

	return frequency


		


C = get_frequency(A, [1,2,3, 0])
print(C)
D = get_frequency(B, [1,2,3,0])
print(D)

#This shows that Humans (or wherever this data came from) is not a uniform random distribution

