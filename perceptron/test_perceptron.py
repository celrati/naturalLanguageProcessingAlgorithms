import re
import sys
from collections import *


def test_model(file):
	model = open("perceptron_model")
	w = defaultdict(int)
	for line in model:
		name,value = line.split(" ")
		w[name] = int(value)

	input_file = open(file)
	for line in input_file:
		phi = create_features(line)
		y_1 = predict_one(w,phi)
		print(str(y_1)+"\n")



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



if __name__ == '__main__':
	args = sys.argv[1:]
	file = args[0]
	test_model(file)