import sys
import nltk

def getTypeWord(word,pos,neg):
	answer = "none"

	negg = open(neg,"r")
	poss = open(pos,"r")

	for w in negg:
		if w.strip('\n') == word:
			answer = "neg"
			#print(w)

	for w in poss:
		if w.strip('\n') == word:
			answer = "pos"
			#print(w)

	return answer


def analyse(sen,pos,neg):
	text = ""
	file = open(sen,"r")

	for line in file:
		words = nltk.word_tokenize(line)
		list_neg = []
		list_pos = []

		for w in words:
			if getTypeWord(w,pos,neg) == "neg":
				list_neg.append(w)
			elif getTypeWord(w,pos,neg) == "pos":
				list_pos.append(w)


		fq_neg = nltk.FreqDist(w.lower() for w in list_neg )
		fq_pos = nltk.FreqDist(w.lower() for w in list_pos )

		scoren = 0
		scorep = 0

		for i,j in fq_pos.most_common(500):
			scorep = scorep + j

		for i,j in fq_neg.most_common(500):
			scoren = scoren + j

		if scorep > scoren:
			print("+")
		elif scorep < scoren:
			print("-")

		print("=")




def main():
	args = sys.argv[1:]
	if not args:
		print 'usage: [--summaryfile] file [file ...]'
		sys.exit(1)

	summary = False
	if args[0] == '--summaryfile':
		summary = True
		del args[0]

	print("######### sentiment-analyser by Mohammed-Achraf Charif ##########\n the result is :")
	analyse(args[0],args[1],args[2])

if __name__ == '__main__':
	main()
