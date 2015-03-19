import linecache
import nltk
import os
import random

def f_FileTokenizer(str_FileName,str_Save_FileName):
	lines_Article = linecache.getlines(str_FileName)
	fp_File = open(str_Save_FileName,'w')
	for line in lines_Article:
		line = nltk.word_tokenize(line)
		for str_Word in line:
			fp_File.write(str_Word.lower()+'\n')
	fp_File.close()
	return str_Save_FileName

class c_MarkovTool:
	def __init__(self):
		self.str_const_GLUE = '_+_'
	def f_glue_word(self,str_Word1,str_Word2):
		return str_Word1+self.str_const_GLUE+str_Word2
	def f_cut_glue(self,str_Word):
		int_Index = str_Word.find(self.str_const_GLUE)
		str_Word1 = str_Word[ : int_Index]
		str_Word2 = str_Word[int_Index+len(self.str_const_GLUE):]
		return [str_Word1,str_Word2]
	def word_tokenizer(self,line):
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
	def f_getASCII(self,str_Word):
		int_Index = ord(str_Word[0])
		return int_Index

class c_MarkovCreater:
	SRCPATH = 'LanguaeTextRepertory/'
	def __init__(self,str_ListFileName):
		lines_Filename = linecache.getlines(str_ListFileName)
		for i in lines_Filename:
			print i
		self.list_AsciiHash = [ { } for i in range(256) ]
		self.dict_KeyFreq = { }
		self.list_KeyFreq_Dict_asciihash =  [ { }  for i in range (256) ]
		for FileName in lines_Filename:
			FileName = self.SRCPATH + FileName.strip()+'_tokenized.txt'
			lines_Word = linecache.getlines(FileName)
			lines_Word.append('EOF')# EOF
			for index_Word in range(len(lines_Word)-2):
				index_AsciiHash = ord(lines_Word[index_Word][0])
				str_Key = c_MarkovTool().f_glue_word(lines_Word[index_Word][:-1],lines_Word[index_Word+1][:-1])
				str_NextWord = lines_Word[index_Word+2][:-1]
				if str_Key not in self.list_AsciiHash[index_AsciiHash]:
					#new one create
					self.list_AsciiHash[index_AsciiHash][str_Key] = { str_NextWord : 1 }
					self.dict_KeyFreq[str_Key] = 1
					self.list_KeyFreq_Dict_asciihash[index_AsciiHash][str_Key] = 1
				else:
					#add frequence
					if str_NextWord in self.list_AsciiHash[index_AsciiHash][str_Key]:
						self.list_AsciiHash[index_AsciiHash][str_Key][str_NextWord]+=1
					else:
						self.list_AsciiHash[index_AsciiHash][str_Key][str_NextWord]=1
					self.dict_KeyFreq[str_Key] += 1
					self.list_KeyFreq_Dict_asciihash[index_AsciiHash][str_Key] += 1

class c_DictSorter:
	def __init__(self,diction):
		self.diction = diction
		self.list_DictKeys = diction.keys()
		self.qsort_stack = [  ]
	def unsorted(self):
		return self.list_DictKeys
	def __quicksort_random__(self,top,end):
		#dictst1 = {'e1':12,'e2':12,'e3':12,'a':12,'b':7,'asd':7,'c':55,'d':7,'e':23}
		if top > end:
			return
		index_rand = random.randint(top,end)
		flag = self.list_DictKeys[index_rand] ;
		self.list_DictKeys[index_rand] = self.list_DictKeys[top]
		self.list_DictKeys[top] = flag
		i = top ; j = end
		write_top = top ; write_end = end
		list_Equal = []
		list_Equal.append(flag)

		while(i<j):
			while(i<j):
				if self.diction[self.list_DictKeys[j]] < self.diction[flag]:
					self.list_DictKeys[write_end] = self.list_DictKeys[j]
					j -= 1
					write_end-=1
				elif self.diction[self.list_DictKeys[j]] == self.diction[flag]:
					list_Equal.append(self.list_DictKeys[j])
					j-=1
				else:
					break
			self.list_DictKeys[write_top] = self.list_DictKeys[j]
			self.list_DictKeys[i] = self.list_DictKeys[j]

			while(i<j):
				if self.diction[self.list_DictKeys[i]]>self.diction[flag]:
					self.list_DictKeys[write_top] = self.list_DictKeys[i]
					i+=1
					write_top += 1	
				elif self.diction[self.list_DictKeys[i]] == self.diction[flag]:
					list_Equal.append(self.list_DictKeys[i])
					i += 1
				else:
					break
			self.list_DictKeys[write_end] = self.list_DictKeys[i]
			self.list_DictKeys[j] =  self.list_DictKeys[i]

		len_list_Equal = len(list_Equal)
		for index_Equal in range(len_list_Equal):
			self.list_DictKeys[index_Equal + write_top] = list_Equal[index_Equal]
		self.qsort_stack.append( [ top, write_top-1 ] )
		self.qsort_stack.append( [ write_end+1, end ] )

	def qsort(self):
		self.qsort_stack.append([0,len(self.list_DictKeys)-1])
		while ( self.qsort_stack != [ ] ):
			top_end = self.qsort_stack.pop()
			top = top_end[0]
			end = top_end[1]
			self.__quicksort_random__( top , end )
		return self.list_DictKeys

	def insertsort(self):
		if self.list_DictKeys == []:
			return []
		newlist = [self.list_DictKeys[0]]
		for i in self.list_DictKeys[1:] :
			judge = 0
			for flag in newlist:
				if self.diction[i] > self.diction[flag]:
					newlist.insert(newlist.index(flag),i)
					judge = 1
					break
			if judge == 0:
				newlist.append(i)			
		return newlist
	def __merge__(self,top,end):
		pass
	def mergesort(self):
		if self.list_DictKeys == []:
			return []
		newlist = self.list_DictKeys
	def bubblesort(self):
		if self.list_DictKeys == []:
			return []
		for i in range(len(self.list_DictKeys)-1,-1,-1):
			for j in range(0,i):
				if self.diction[self.list_DictKeys[j]] < self.diction[self.list_DictKeys[j+1]]:
					temp = self.list_DictKeys[j]
					self.list_DictKeys[j] = self.list_DictKeys[j+1]
					self.list_DictKeys[j+1] = temp
		return self.list_DictKeys





#dictst1 = {'12_1':12,'12_2':12,'12_3':12,'12_4':12,'b7':7,'asd7':7,'c55':55,'d7':7,'e23':23}
#print c_DictSorter(dictst1).bubblesort()


def f_KeyFreq_Filter(dict_KeyFreq,int_ThreshouldVal):
	if int_ThreshouldVal == 0:
		return dict_KeyFreq
	list_KeyVal_Delete = [ ]
	for i in dict_KeyFreq:
		if dict_KeyFreq[i] <= int_ThreshouldVal:
			list_KeyVal_Delete.append(i)
	for i in list_KeyVal_Delete:
		del(dict_KeyFreq[i])
	return dict_KeyFreq

def f_AsciiHash_to_File(list_AsciiHash,dict_KeyFreq,int_ThreshouldVal = 0):
	str_FileName = 'Markov_HASH.txt'
	fp_File = open(str_FileName,'w')
	dict_KeyFreqDic_Flited = f_KeyFreq_Filter(dict_KeyFreq,int_ThreshouldVal)
	for str_Key in dict_KeyFreqDic_Flited:
		int_key_Freq = dict_KeyFreq[str_Key]
		fp_File.write(str_Key+'\t')
		fp_File.write(str(int_key_Freq)+'\t')
		for str_Word in list_AsciiHash[ord(str_Key[0])][str_Key]:
			fp_File.write(str_Word+'\t')
			fp_File.write(str(list_AsciiHash[ord(str_Key[0])][str_Key][str_Word])+'\t')
		fp_File.write('\n')
	fp_File.close()

def f_AsciiHash_to_File_Sorted(list_AsciiHash,dict_KeyFreq,int_ThreshouldVal = 0):
	str_FileName = 'Markov_HASH_keynotsorted.txt'
	fp_File = open(str_FileName,'w')
	dict_KeyFreqDic_Flited = f_KeyFreq_Filter(dict_KeyFreq,int_ThreshouldVal)
	list_SortedKey_list = c_DictSorter(dict_KeyFreqDic_Flited).qsort()
	
	for str_Key in dict_KeyFreqDic_Flited:
		int_key_Freq = dict_KeyFreq[str_Key]
		fp_File.write(str_Key+'\t')
		fp_File.write(str(int_key_Freq)+'\t')
		for str_Word in list_AsciiHash[ord(str_Key[0])][str_Key]:
			fp_File.write(str_Word+'\t')
			fp_File.write(str(list_AsciiHash[ord(str_Key[0])][str_Key][str_Word])+'\t')
		fp_File.write('\n')
	fp_File.close()

def f_AsciiHash_to_File_Sorted_Splited(c_Markov): # don't want to filter
	list_AsciiHash = c_Markov.list_AsciiHash
	list_KeyFreq_Dict_asciihash = c_Markov.list_KeyFreq_Dict_asciihash
	str_SavePath_Father = './Markov_AsciiHash/'
	if not os.path.exists(str_SavePath_Father):
		os.mkdir(str_SavePath_Father)
	for index_Ascii in range(256):
		if list_AsciiHash[index_Ascii] == { }:
			continue
		str_SavePath = str_SavePath_Father + str(index_Ascii)+'/'
		if not os.path.exists(str_SavePath):
			os.mkdir(str_SavePath)
		dict_AsciiHash_DICT = list_AsciiHash[index_Ascii]
		dict_KeyFreq_thisAcii = list_KeyFreq_Dict_asciihash[index_Ascii]

		str_Fname1_Key_A = str_SavePath+'A.txt'
		str_Fname2_Key_B = str_SavePath+'B.txt'
		str_Fname3_Key_AB = str_SavePath+'A+B.txt'
		str_Fname4_Key_Freq = str_SavePath + 'A+B_Freq.txt'
		str_Fname5_Key_AND_Freq = str_SavePath + 'A+B+Freq.txt'

		str_Fname6_NextWord = str_SavePath + 'NextWord.txt'
		str_Fname7_NextWord_Freq = str_SavePath + 'NextWord_Freq.txt'
		str_Fname8_NW_AND_Freq = str_SavePath + 'NextWord+Freq.txt'
		str_Fname9_Whole = str_SavePath + 'Whole.txt'

		fp1_K_A = open(str_Fname1_Key_A,'w')#yezetst
		fp2_K_B = open(str_Fname2_Key_B,'w')#yezetst
		fp3_K_AB = open(str_Fname3_Key_AB,'w')#yezetst
		fp4_K_AB_Freq = open(str_Fname4_Key_Freq,'w')#yezetst
		fp5_K_AND_Freq = open(str_Fname5_Key_AND_Freq,'w')#yezetst

		fp6_NW = open(str_Fname6_NextWord,'w')#yezetst
		fp7_NW_Freq = open(str_Fname7_NextWord_Freq,'w')#yezetst
		fp8_NW_AND_Freq = open(str_Fname8_NW_AND_Freq,'w')#yezetst
		fp9_Whole = open(str_Fname9_Whole,'w')#yezetst

		list_Key_Sorted = c_DictSorter(dict_KeyFreq_thisAcii).qsort() 
		#this one use qsort is write.
		for str_Key in list_Key_Sorted:
			list_AB = c_MarkovTool().f_cut_glue(str_Key)
			fp1_K_A.write(list_AB[0]+'\n')#yezetst
			fp2_K_B.write(list_AB[1]+'\n')#yezetst
			fp3_K_AB.write(str_Key+'\n')#yezetst
			int_AB_Freq = dict_KeyFreq_thisAcii[str_Key]
			fp4_K_AB_Freq.write(str(int_AB_Freq)+'\n')#yezetst
			fp5_K_AND_Freq.write(str_Key+'\t'+str(int_AB_Freq)+'\n')#yezetst
			fp9_Whole.write(str_Key+'|'+str(int_AB_Freq)+'|')#yezetst
			dict_NextWord = dict_AsciiHash_DICT[str_Key]
			list_NextWord_sorted = c_DictSorter(dict_NextWord).unsorted()
			#here puzzled me. which sort to use? this one is small!

			for tail in list_NextWord_sorted:
				fp6_NW.write(tail+'\t')#yezetst
				int_tail_Freq = dict_NextWord[tail]
				fp7_NW_Freq.write(str(int_tail_Freq)+'\t')#yezetst
				fp8_NW_AND_Freq.write(tail+'\t'+str(int_tail_Freq)+'\t')#yezetst
				fp9_Whole.write(tail+'|'+str(int_tail_Freq)+"|")#yezetst
			fp6_NW.write('\n')#yezetst
			fp7_NW_Freq.write('\n')#yezetst
			fp8_NW_AND_Freq.write('\n')#yezetst
			fp9_Whole.write('\n')#yezetst
		fp1_K_A.close()#yezetst
		fp2_K_B.close()#yezetst
		fp3_K_AB.close()#yezetst
		fp4_K_AB_Freq.close()#yezetst
		fp5_K_AND_Freq.close()#yezetst
		fp6_NW.close()#yezetst
		fp7_NW_Freq.close()#yezetst
		fp8_NW_AND_Freq.close()#yezetst
		fp9_Whole.close()#yezetst



import cProfile
import pstats


if __name__ == '__main__' :
	str_ListFileName = 'ImportList.txt'
	#str_FileName = 'The_Holy_Bible.txt'
	#savefilename = 'The_Holy_Bible_tokenize.txt'
	#savefilename = f_FileTokenizer(str_FileName,savefilename)
	#c_Markov = c_MarkovCreater(savefilename)

	c_Markov = c_MarkovCreater(str_ListFileName)
	list_AsciiHash = c_Markov.list_AsciiHash
	dict_KeyFreq = c_Markov.dict_KeyFreq
	#f_AsciiHash_to_File_Sorted_Splited(c_Markov)

	pr = cProfile.Profile()
	pr.enable()

	f_AsciiHash_to_File_Sorted_Splited(c_Markov)

	pr.disable()
	ps = pstats.Stats(pr).sort_stats("cumulative")
	ps.print_stats()
	print 3