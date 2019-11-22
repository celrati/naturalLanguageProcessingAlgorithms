import re
import sys
from collections import *

# we're gonna train a model using the perceptron algorithm

def train_model(file): #we re gonna output the model inside a file "perceptron_model"
	w = defaultdict(int)
	data = open(file)
	for line in data:
		y = int(line[0:2])
		x = line[2:].strip()
		phi = create_features(x)
		y_1 = predict_one(w,phi)
		if y != y_1:
			update_weights(w,phi,y)
	output = open("perceptron_model","w")
	for i in w.items():
		name = i[0]
		value = i[1]
		output.write(name+" "+str(value)+"\n")



		
def create_features(x):
	phi =  defaultdict(int)
	words = x.split(" ")
	for word in words:
		phi["UNI:"+word] += 1
	return phi

def predict_one(w,phi):
	score = 0
	for i in phi.items():
		name = i[0]
		value = i[1]
		if name in w:
			score += value * w[name]
	if score >= 0: 
		return 1
	else:
		return -1

def update_weights(w,phi,y):
	for i in phi.items():
		name = i[0]
		value = i[1]
		w[name] += value * y

if __name__ == '__main__':
	args = sys.argv[1:]
	file = args[0]
	train_model(file)

