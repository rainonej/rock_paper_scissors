'''This program will get the frequency data of nearly 500,000 rounds of rock paper scisorrs.
To process all of this data I need to use the super computer Stampede2.
I'll be parallelizing the proccess to make it run faster.
'''

from mpi4py import MPI
#import mpi4py as MPI

# process id of the current process
rank = MPI.COMM_WORLD.rank

# total number of mpi processes
size = MPI.COMM_WORLD.size

Total_length = 400000 #I don't want to run more than 10000 on each processor

width = Total_length//size

import numpy as np
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

def add_dics(dics):
	dic = {}
	for key in dics[0]:
		dic[key] = 0 
		for i in range(0, len(dics)):
			dic[key] += dics[i][key]
	return dic


start = rank*width
#end = (rank+1)*width

Raw_data = np.genfromtxt("Rock_Paper_Scissors_Raw.txt", dtype = int, comments = '#', delimiter = ',', skip_header = start, usecols = (0,2), max_rows = width)
Raw_data = Raw_data.tolist()

max_game_length = 4
(A,B) = get_multi_frequency(Raw_data, max_game_length)
#print(A)
#print(B)

if (rank != 0):
	MPI.COMM_WORLD.send(B, dest=0, tag=10)


#the output of each process is a list of dictionaries of different size
#I want a list of dictionaries all of the same size

if (rank == 0):
	multi_frequency = []
	for j in range(0,max_game_length):
		multi_frequency.append([])
	for i in range(1,size):
		ifrequency = MPI.COMM_WORLD.recv(source=i,tag=10)
		for j in range(0,max_game_length):
			multi_frequency[j] += [ifrequency[j]]

	for j in range(0,max_game_length):
		multi_frequency[j] = add_dics(multi_frequency[j])

	print(multi_frequency)

	import pickle

	with open('multi_frequency.pkl', 'wb') as output:
		pickle.dump(multi_frequency, output, pickle.HIGHEST_PROTOCOL)

	print('Done!')

	'''To read it enter the following code
	import pickle
	with open('multi_frequency.pkl', 'rb') as input:
		multi_frequency = pickle.load(input)
	'''

'''There's a problem here. Somehow the multi_frequency is getting more numbers than possible. 
There's probably a problem in the data either not splitting properly, 
or the numbers aren't adding properly'''
