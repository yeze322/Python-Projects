#!/usr/bin/env python
# coding=utf-8
import nltk
from linecache import getlines,getline
from MarkovLibCreater import c_DictSorter
# = [[] for i in range(26)]

def gethash(word):
	index = ord(word[0])
	index -=ord('a')
	if index<0 or index>25:
		return -1
	return index

#tstdic = {'lkjlj':2,"asd":34,"vxcz":5,"cxiazk":7,"qwezcx":26,'aasddasdas':5}
#newlist = c_DictSorter(tstdic).insertsort()
def word_tokenizer(line):
	blankset = '\n\r\b\t\f\v '
	token = []
	word = ""
	for char_i in line:
		if char_i.isalpha() or char_i.isdigit():
			word = word + char_i
			continue
		if char_i in blankset:
			if word != "" :
				token.append(word)
				word = ""
			continue
		if word != "":
			token.append(word)
			word = ""
		token.append(char_i)
	return token

def article_to_hash(article):
	alpha_hash =  [ { } for i in range(255) ]
	fw = open("The_Holy_Bible_tokenize.txt",'w')
	for line in article:
		#linetoken = nltk.word_tokenize(line)
		linetoken = word_tokenizer(line)
		for word in linetoken:
			word = word.lower()
			fw.write(word+'\n')
			index = ord(word[0])
			if word in alpha_hash[index]:
				alpha_hash[index][word] += 1
			else:
				alpha_hash[index][word] = 1
	fw.close()
	return alpha_hash

import os
def hash_to_file(alpha_hash):
	save_dir = './bible/'
	if not os.path.exists(save_dir):
		os.mkdir(save_dir)
	for loop in range(255):
		if alpha_hash[loop] == { }:
			continue
		newlist = c_DictSorter(alpha_hash[loop]).qsort()
		filename = save_dir + str(loop)+'.txt'
		fw = open(filename,'w')	
		for i in newlist:
			towrite = i+'\t'+str(alpha_hash[loop][i])
			fw.write(towrite+'\n')
		fw.close()

import cProfile
import pstats

if __name__ == '__main__':
	filename = "The_Holy_Bible.txt"
	EOF = '\n'
	article = getlines(filename)
	alpha_hash = article_to_hash(article)
	cProfile.run('alpha_hash = article_to_hash(article)','result')
	ps = pstats.Stats('result')
	ps.strip_dirs().sort_stats("cumulative",'time').print_stats()
	hash_to_file(alpha_hash)



#line = "hehe this is mine, that's a shit [was]"
#print word_tokenizer(line)