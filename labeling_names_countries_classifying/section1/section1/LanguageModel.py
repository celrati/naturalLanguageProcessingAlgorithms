from collections import *
from random import random
import math

def train_char_lm(fname, order=4, add_k=1): # train a model 
# fname : the name of the file
# order : ngram 
# add_k : the smothing 
	data = open(fname).read()
	lm = defaultdict(Counter)
	empty_chars = "~" * order # the fisrt order empty char ~~~~ text here
	data = empty_chars + data

	for i in range(len(data)-order): # looping every string from the data whitout the empty_chars
		history = data[i:i+order] # hello world history = "~~~~h" ou hello
		char    = data[i+order]		# char = 'h'
		lm[history][char]+=1	 # lm[hello][o]

	def normalize(counter):
		s = float(sum(counter.values()))
		return [ (c  ,(cnt)/(s) ) for c,cnt in counter.items() ]

	outlm = { hist:normalize(chars) for hist,chars in lm.items() }
	return outlm

def generate_letter(lm, history, order):
 
  history = history[-order:]
  dist = lm[history]
  x = random()
  for c,v in dist:
    x = x - v
    if x <= 0: return c

def generate_text(lm, order, nletters=500):

  history = "~" * order
  out = []
  for i in range(nletters):
    c = generate_letter(lm, history, order)
    history = history[-order:] + c
    out.append(c)
  return "".join(out)


def perplexity(test_filename, lm, order=4):
  data = open(test_filename).read()
  pad = "~" * order
  data = pad + data
  N = len(data)
  
  listProba = []

  for i in range(len(data)-order): # looping every string from the data whitout the empty_chars
    history = data[i:i+order] # hello world history = "~~~~h" ou hello
    char    = data[i+order]   # char = 'h'
    #print(lm[history])

    y = lm.get(history,[])
    if y is None:
      listProba.append(1/(len(lm)*order))

    for x in y:
      if x[0] == char:
        listProba.append(x[1])


  perp = 1
  for i in listProba:
    perp= perp + math.log1p(1/i)
  k = perp /N
  print(math.exp(k))


def calculate_prob_with_backoff(char, history, lms, lambdas):


  p1 = lms[0].get(history,[])
  if p1 is None:
    p1 = 0 

  for x in p1:
    if x[0] == char:
      p1 = x[1]

  p2 = lms[1].get(history,[])
  if y is None:
    p2 = 0

  for x in p2:
    if x[0] == char:
      p2 = x[1]

  p3 = lms[2].get(history,[])
  if y is None:
    p3 = 0

  for x in p3:
    if x[0] == char:
      p3 = x[0]
  
  l1 = lambdas[0]
  l2 = lambdas[1]
  l3 = lambdas[2]
  pr = l1*p1 + l2*p2 + l3*p3
  return pr
 

def getProbabWords(lm,order,word):
  # kenitra i|ken
  data = ('~'*order) + word
  pr = 1
  
  for i in range(len(data)-order): # looping every string from the data whitout the empty_chars
    history = data[i:i+order] # hello world history = "~~~~h" ou hello
    char    = data[i+order]

    #print(history)
    p = lm.get(history,[])


    if p == []:
      p1 = float(1)/10000
      pr = pr * p1

    else:  
     for x in p:
        if x[0] == char:
          p1 = x[1]

          pr = pr * p1


  return pr



if __name__ == '__main__':
  print('Training language model for cities ')

  lm_af = train_char_lm("af.txt", order=4);
  lm_cn = train_char_lm("cn.txt", order=4);
  lm_de = train_char_lm("de.txt", order=4);
  lm_fi = train_char_lm("fi.txt", order=4);
  lm_fr = train_char_lm("fr.txt", order=4);
  lm_in = train_char_lm("in.txt", order=4);
  lm_ir = train_char_lm("ir.txt", order=4);
  lm_pk = train_char_lm("pk.txt", order=4);
  lm_za = train_char_lm("za.txt", order=4);

  #print(getProbabWords(lm_fr,4,"fraundorf"))

  output = open("labels.txt","w")

  data = open("cities_test.txt","r")
  
  for city in data:
    pr_fr = getProbabWords(lm_fr,4,city)
    pr_af = getProbabWords(lm_af,4,city)
    pr_cn = getProbabWords(lm_cn,4,city)
    pr_de = getProbabWords(lm_de,4,city)
    pr_fi = getProbabWords(lm_fi,4,city)
    pr_in = getProbabWords(lm_in,4,city)
    pr_ir = getProbabWords(lm_ir,4,city)
    pr_pk = getProbabWords(lm_pk,4,city)
    pr_za = getProbabWords(lm_za,4,city)
    print(city)

    max_pr = max(pr_fr,pr_af,pr_cn,pr_de,pr_fi,pr_in,pr_ir,pr_pk,pr_za)
    if max_pr == pr_fr:
      output.write("fr  " + city)
    elif max_pr == pr_af:
      output.write("af  " + city)
    elif max_pr == pr_cn:
      output.write("cn  " + city)
    elif max_pr == pr_de:
      output.write("de  " + city)
    elif max_pr == pr_fi:
      output.write("fi  " + city)
    elif max_pr == pr_in:
      output.write("in  " + city)
    elif max_pr == pr_ir:
      output.write("ir  " + city)
    elif max_pr == pr_pk:
      output.write("pk  " + city)
    else:
      output.write("za  " + city)
    



  #perplexity("hello",lm,2)

  #print( j for j in lm['he']  )
  #print(generate_text(lm, 7))