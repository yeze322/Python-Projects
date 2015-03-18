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
		self.qsort_list = [  ]
		self.qsort_stack = [  ]
	def __quicksort__(self,top,end):
		if top > end:
			return
		flag = self.qsort_list[top] ; i = top ; j = end
		while(i<j):
			while(i<j and self.diction[self.qsort_list[j]]<=self.diction[flag]):
				j-=1
			self.qsort_list[i] = self.qsort_list[j]
			while(i<j and self.diction[self.qsort_list[i]]>=self.diction[flag]):
				i+=1
			self.qsort_list[j] = self.qsort_list[i]
		self.qsort_list[i] = flag
		self.qsort_stack.append( [ top, i-1 ] )
		self.qsort_stack.append( [ i+1, end ] )
	def qsort(self):
		self.qsort_list = self.keylist
		self.qsort_stack.append([0,len(self.keylist)-1])
		#count = 0
		while ( self.qsort_stack != [ ] ):
			top_end = self.qsort_stack.pop()
			top = top_end[0]
			end = top_end[1]
			self.__quicksort__( top , end )
			#count+=1
			#if count%5000==0:
			#	print count
		return self.qsort_list
	
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
			towrite = i+'\t'+str(alpha_hash[loop][i])
			fw.write(towrite+'\n')
		fw.close()

if __name__ == '__main__':
	filename = "The_Holy_Bible.txt"
	EOF = '\n'
	article = getlines(filename)
	print 'article created!'
	alpha_hash = article_to_hash(article)
	print "alpha_hash finish"
	hash_to_file(alpha_hash)
