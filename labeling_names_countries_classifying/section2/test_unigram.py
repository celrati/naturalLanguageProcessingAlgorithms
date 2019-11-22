#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import *
import sys
import re
import math

# get a model text files and test files and print the entropy and the coverage

def printEntropyAndCoverage(model_file,test_file):
	H = 0  #H is the entropy for now
	data = open(model_file,"r")
	model = dict()
	for i in data:
		j = i.split(':')
		c = j[0][0]
		p = float(j[1])
		model[c] = p
		### here the c is the word, and p it's probability
	# now we're gonna read the test file to compute the entropy and coverage..
	data = open(test_file).read()
	H = 0
	lenn = 0
	lenX = 0
	for i in range(len(data) - 1 ): # to delete the end_of_file
		if data[i] != '\n' and data[i] != ' ':
			if (data[i] in  model):
				lenX += 1
				H += (model[data[i]]*math.log(model[data[i]]))
			else:
				H += ((float(1/10000))*math.log(float(1/10000)))
			lenn += 1
	H *= -1
	print("entropy is : "+str(H)+"\n")
	print("coverage is : "+str(lenX)+"/"+str(lenn))




if __name__ == '__main__':
	args = sys.argv[1:]
	file = args[0]
	file2 = args[1]
	printEntropyAndCoverage(file,file2)
