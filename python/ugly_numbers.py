'''

	Inputs: 
	1
	9
	011
	12345

	Outputs:
	0
	1
	6
	64
'''

from itertools import combinations_with_replacement

def is_ugly(number): 
	return 0 in [number % i for i in [2,3,5,7]]

def make_combos(number):
	''' result can be +, -, space/ nothing 
		Should return a list of length 3^(D-1)
		Not completed as of yet
	'''
	
	return list(combinations_with_replacement(['+', '-', 's'], number-1))
