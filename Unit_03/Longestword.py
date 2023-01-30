# python class 11 nov 2022

# write a python program to find the longest word in a file 

import os 
path=os.path.dirname(__file__)
path=path+'/'
print(path)

def longestWordsInAFile(file):
	allwords=[]
	data=file.readlines()
	for i in data:
		words = i.split()
		allwords = allwords +words
	maxlen=0
	for i in allwords:
		if len(i)> maxlen:
			maxlen=len(i)
			
	for i in allwords:
		if len(i)== maxlen:
			print(i)		
			
'''	
file = open(path+'abc.txt','r')                  # commented to check the next file opening command in try block 
longestWordsInAFile(file)

'''

try:
	file = open(path+'abcd.txt','r')          # this line gives exception file not found

except FileNotFoundError:
	print("exception is handled ")	
	file = open(path+'abcd.txt','w+') 	



print("===========================================================")
