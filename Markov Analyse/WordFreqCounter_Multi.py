#!/usr/bin/env python
# coding=utf-8
import nltk
from linecache import getlines,getline
from MarkovLibCreater_Multi import c_DictSorter
# = [[] for i in range(26)]
SRCPATH = 'LanguageTextRepertory/'
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

def f_Articles_to_hash(list_FileName):
	alpha_hash =  [ { } for i in range(255) ]
	list_ArticleList = getlines(list_FileName)
	for FileName in list_ArticleList:
		FileName = SRCPATH+FileName.strip()
		fw = open(FileName+'_tokenized.txt','w')
		article = getlines(FileName)
		for line in article:
			#linetoken = nltk.word_tokenize(line)
			linetoken = word_tokenizer(line)
			if linetoken == []:
				continue
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
	save_dir = './WordList/'
	if not os.path.exists(save_dir):
		os.mkdir(save_dir)
	for loop in range(255):
		if alpha_hash[loop] == { }:
			continue
		newlist = c_DictSorter(alpha_hash[loop]).qsort()
		filename = save_dir + str(loop)+'.txt'
		str_FreqName = save_dir + str(loop)+'_Freq.txt'
		fw_Word = open(filename,'w')
		fw_Freq = open(str_FreqName,'w')
		for i in newlist:
			fw_Word.write(i+'\n')
			fw_Freq.write(str(alpha_hash[loop][i])+'\n')
		fw_Word.close()
		fw_Freq.close()

import cProfile
import pstats

if __name__ == '__main__':
	FileName_ImportList = 'ImportList.txt'
	#alpha_hash = f_Articles_to_hash(FileName_ImportList)
	cProfile.run('alpha_hash = f_Articles_to_hash(FileName_ImportList)','result')
	ps = pstats.Stats('result')
	ps.strip_dirs().sort_stats("cumulative",'time').print_stats()
	hash_to_file(alpha_hash)