#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

def extraire_noms(nom_fichier):
	listFinal = []
	listtmp   = []
	file = open(nom_fichier,"r")

	c = 0
	str = ""
	for line in file:
		for token in re.findall("<th><h1>Popular Names in (.*?)</h1></th>",line):
			print token

		if line == "<tr align=\"right\">\n":
			c = 1
		if line == "</tr>\n":
			c = 0

		if c == 1 and line != "<tr align=\"right\">\n" and line != "</tr>\n":
			str = str + line
		if c == 0:
			listtmp.append(str)
			str = ""


	listtmp=filter(lambda x: len(x)>0, listtmp)	
	#print(listtmp)	
	#print(listtmp)
	for chaine in listtmp:
	   		rank = re.search(' <td>(.+)</td> <td>(.+)</td><td>(.+)</td>\n <td>(.+)</td>\n<td>(.+)</td>\n',chaine).group(1)
			male   = re.search(' <td>(.+)</td> <td>(.+)</td><td>(.+)</td>\n <td>(.+)</td>\n<td>(.+)</td>\n',chaine).group(2)
			female = re.search(' <td>(.+)</td> <td>(.+)</td><td>(.+)</td>\n <td>(.+)</td>\n<td>(.+)</td>\n',chaine).group(4)
			listFinal.append(male+" "+rank)
			listFinal.append(female+" "+rank)

	listFinal.sort()
	for i in listFinal:
		print(i)





















def main():

  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for i in args:
    extraire_noms(i)


if __name__ == '__main__':
  main()
