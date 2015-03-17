#!/usr/bin/env python
# coding=utf-8
import nltk
from linecache import getlines,getline
# = [[] for i in range(26)]

def gethash(word):
	index = ord(word[0])
	index -=ord('a')
	if index<0 or index>25:
		return -1
	return index
class dicsort:
	def __init__(self,diction):
		self.diction = diction
		self.keylist = diction.keys()
	def dicqsort(self,top,end):
		pass
	def insertsort_list(self): #[ 'helo',2,'word',4,..]
		pass
	def insertsort(self):
		if self.keylist == []:
			return []
		newlist = [self.keylist[0]]
		for i in self.keylist[1:] :
			judge = 0
			for flag in newlist:
				if self.diction[i] > self.diction[flag]:
					newlist.insert(newlist.index(flag),i)
					judge = 1
					break
			if judge == 0:
				newlist.append(i)			
		return newlist

#tstdic = {'lkjlj':2,"asd":34,"vxcz":5,"cxiazk":7,"qwezcx":26,'aasddasdas':5}
#newlist = dicsort(tstdic).insertsort()

def article_to_hash(article):
	alpha_hash =  [ { } for i in range(26) ]
	for line in article:
		linetoken = nltk.word_tokenize(line)
		for word in linetoken:
			word = word.lower()
			index = gethash(word)
			if index !=  -1 :
				if word in alpha_hash[index]:
					alpha_hash[index][word] += 1
				else:
					alpha_hash[index][word] = 1
	return alpha_hash

'''def article_to_hash_pro(article):
	alpha_list = [ [ ] for i in range(26) ]
	alpha_hash =  [ { } for i in range(26) ]
	for line in article:
		linetoken = nltk.word_tokenize(line)
		for word in linetoken:
			word = word.lower()
			index = gethash(word)
			if word in alpha_list[index]:
				word_index = alpha_list[index].index(word)
				word_count = alpha_list[index][word_index+1] + 1
				alpha_list[index][word_index+1] += 1
			else:
				alpha_list[index].append(word)
				alpha_list[index].append(1)
	return alpha_list'''

import os
def hash_to_file(alpha_hash):
	save_dir = './bible/'
	if not os.path.exists(save_dir):
		os.mkdir(save_dir)
	for loop in range(26):
		filename = save_dir + chr(loop+ord('a'))+'.txt'
		fw = open(filename,'w')	
		newlist = dicsort(alpha_hash[loop]).insertsort()
		for i in newlist:
			towrite = i+' '+str(alpha_hash[loop][i])
			fw.write(towrite+'\n')
		fw.close()

if __name__ == '__main__':
	filename = "The_Holy_Bible.txt"
	EOF = '\n'
	article = getlines(filename)
	print 'article created!'
	alpha_hash = article_to_hash(article)
	print "alpha_hash finish"
	#hash_to_file(alpha_hash)
