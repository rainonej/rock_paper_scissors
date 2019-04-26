import numpy as np
#import pickle

#A = np.loadtxt("Rock_Paper_Scissors_Raw.txt", dtype = list, comments = '#', delimiter = ',', usecols = (0,1,2,3))
#A = np.loadtxt("Rock_Paper_Scissors_Raw.txt", dtype = int, comments = '#', delimiter = ',', usecols = (2), ndmin = 1)
#B = np.loadtxt("Rock_Paper_Scissors_Raw.txt", dtype = int, comments = '#', delimiter = ',', usecols = (3), ndmin = 1)
#A = np.genfromtxt("Rock_Paper_Scissors_Raw.txt", dtype = int, comments = '#', delimiter = ',', usecols = (2), ndmin = 1)

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


def process_data(data, n):
	'''input a 2-dim list of numbers. First collum is gameID, second is the outputs for each round. 
	returns a list of all singles, pairs, tripples, quadupples, etc... up to n. '''
	
	processed_data =[] #creates the empty data
	for i in range(0,n):
		processed_data.append([])
	
	options = [1,2,3] #the valid outputs not to skip\


	skip = 0 #the only value to skip
	L = len(data) #don't want to calculate this a lot

	#Setting up how the counters work
	game_id = 0 #should reflect the actual game_id
	round = 0 #should not be the actual round
	for i in range(0,L):
		if (data[i][0] != game_id):
			game_id += 1
			round = 0
		if (data[i][1] != skip):
			round += 1

			#does the singleton first
			processed_data[0].append(data[i][1])

			for j in range(2,n+1):
				if (round >= j):
					#print(processed_data)
					#print('j =', j) 
					processed_data[j-1].append(processed_data[0][-j:-1] + [processed_data[0][-1]])

	return processed_data

from itertools import product

def prod(set,k):
	'''takes in a list of n elements. Returns a list of all possible permutations of k elements out of the set.'''
	return list(product(set, repeat = k))
	#return list(map(list, list(product(set, repeat = k))))

def get_multi_frequency(data, n):
	'''input a 2-dim list of numbers. First collum is gameID, second is the outputs for each round. 
	returns a the frequency of evey singles, pairs, tripples, quadupples, etc... up to n. '''
	
	processed_data =[] #creates the empty data
	for i in range(0,n):
		processed_data.append([])


	options = [1,2,3] #the possible options
	multi_options = []
	for i in range(1,n+1):
		multi_options += [prod(options, i)]


	#creat the frequency table
	frequency = []
	for i in range(0,n):
		frequency.append({})
		for opt in multi_options[i]:
			#print(frequency)
			#print(multi_options[i])
			frequency[-1][opt] = 0
		frequency[-1]['total'] = 0
	#print(frequency)



	skip = 0 #the only value to skip
	L = len(data) #don't want to calculate this a lot

	#Setting up how the counters work
	game_id = 0 #should reflect the actual game_id
	round = 0 #should not be the actual round
	for i in range(0,L):
		if (data[i][0] != game_id):
			game_id = data[i][0]
			round = 0
		if (data[i][1] != skip):
			round += 1

			#do the singleton first
			#print(frequency)
			frequency[0][tuple([data[i][1]])] += 1
			frequency[0]['total'] += 1
			processed_data[0].append(data[i][1])

			for j in range(2,n+1):
				if (round >= j):
					#print(processed_data)
					#print('j =', j) 
					#print(processed_data[0][-j:-1] + [processed_data[0][-1]])
					#print(tuple([processed_data[0][-j:-1] + [processed_data[0][-1]]]))
					frequency[j-1][ tuple(processed_data[0][-j:-1] + [processed_data[0][-1]]) ] += 1
					frequency[j-1]['total'] +=1
					#processed_data[j-1].append(processed_data[0][-j:-1] + [processed_data[0][-1]])

	return (processed_data,frequency)

#An = np.loadtxt("Rock_Paper_Scissors_Raw.txt", dtype = int, comments = '#', delimiter = ',', usecols = (0,2), ndmin = 2)
An = np.genfromtxt("Rock_Paper_Scissors_Raw.txt", dtype = int, comments = '#', delimiter = ',', usecols = (0,2), max_rows = 5000)

#Am = An[0:100]
An = An.tolist()
#new_data = process_data(Am, 2)
#print(new_data)

(A,B) = get_multi_frequency(An, 4)
#print(A)
print(B)






'''
C = get_frequency(A, [1,2,3, 0])
print(C)
D = get_frequency(B, [1,2,3,0])
print(D)
'''
#This shows that Humans (or wherever this data came from) is not a uniform random distribution

