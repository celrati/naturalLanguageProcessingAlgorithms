#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import *
import sys
import re
##################################################################"""
# generate a file : new_model_unigram that contains the model
###############################################################""#

def train_unigram(file_to_train):
	data = open(file_to_train).read()
	lm = defaultdict(int)
	#print(data)
	lenn = 0
	for i in range(len(data) - 1 ): # to delete the end_of_file
		if data[i] != '\n' and data[i] != ' ':
			w = data[i]
			lm[w] += 1
			lenn += 1

	model = dict()	
	for i in lm.items():
		print(str(i[0])+"  "+str(i[1]))
		model[i[0]] = (float)(i[1]) / (float)(lenn)
	#print(model)
	output = open("new_model_unigram","w")
	print(lenn)
	for i in model.items():
		output.write(str(i[0])+" : "+str(i[1])+"\n")



if __name__ == '__main__':
	args = sys.argv[1:]
	file = args[0]
	train_unigram(file)
