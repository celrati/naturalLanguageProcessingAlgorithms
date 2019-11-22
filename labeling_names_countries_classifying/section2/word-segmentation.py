#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import *
import sys
import re
import math

def applyViterbi(model,test_file):
	# now we re gonna fill our dict lm from the model
	data1 = open(model,"r")
	model = dict()
	for i in data1:
		#print(i)
		j = i.split('\t')
		c = j[0].strip()
		p = float(j[1].strip())
		#print(c)
		#print(p)
		model[c] = p
#############################
##now we ll apply the viterbi algo
	best_score  = [0]*100
	best_edge = ['null']*100

	data2 =open(test_file,"r")
	for line in data2:
		line = line.strip()
		best_edge[0] = "null" 
		best_score[0] = 0
		for word_end in range(1,(len(line)+1)):
			best_score[word_end] = 100000
			for word_begin in  range(0,word_end):
				word = line[word_begin:word_end]
				#print(word)
				if word in model:
					#print(word)
					proba = float(model[word])
					#print(proba)
					my_score = best_score[word_begin] + ((-1)*math.log(proba))
					if my_score < best_score[word_end]:
						best_score[word_end] = my_score
						best_edge[word_end] = (word_begin,word_end)
		###backward
		##get the length of best_edge
		lenn = 0
		best_edge1 = []
		#best_edge1.append("null")
		c = 0  #we do this because we could have more than one null at the begining
		cx = 0 
		for i in range(0,len(best_edge)):
			if best_edge[i] == "null" and c == 0:
				cx += 1
			elif best_edge[i] != "null":
				c = 1
				best_edge1.append(best_edge[i])

		#best_edge1 = ["null"]*cx + best_edge
		best_edge2 = (["null"]*cx) + best_edge1
		#print(best_edge2)
		words = []
		next_edge = best_edge1[len(best_edge1) - 1]
		#print(next_edge)
		while next_edge != "null":
			word = line[next_edge[0]:next_edge[1]]
			#print(next_edge)
			#print(next_edge[1])
			words.append(word)
			if best_edge2[next_edge[0]] == "null":
				break
			next_edge = best_edge2[next_edge[0]]
		#words = words.reverse()
		w = words[::-1]
		newWrd =""
		for i in w:
			newWrd += (i+" ")
		print(newWrd)







if __name__ == '__main__':
	args = sys.argv[1:]
	model = args[0]
	test = args[1]
	applyViterbi(model,test)