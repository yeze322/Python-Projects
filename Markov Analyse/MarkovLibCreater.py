import linecache
import nltk
import os
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
	def f_getASCII(self,str_Word):
		int_Index = ord(str_Word[0])
		return int_Index

class c_MarkovCreater:
	def __init__(self,str_FileName,):
		lines_Word = linecache.getlines(str_FileName)
		self.list_AsciiHash = [ { } for i in range(256) ]
		self.dict_KeyFreq = { }
		self.list_KeyFreq_Dict_asciihash =  [ { }  for i in range (256) ]
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
		self.keylist = diction.keys()
		self.list_DictKeys = [  ]
		self.qsort_stack = [  ]
	def __quicksort__(self,top,end):
		if top > end:
			return
		flag = self.list_DictKeys[top] ; i = top ; j = end
		while(i<j):
			while(i<j and self.diction[self.list_DictKeys[j]]<=self.diction[flag]):
				j-=1
			self.list_DictKeys[i] = self.list_DictKeys[j]
			while(i<j and self.diction[self.list_DictKeys[i]]>=self.diction[flag]):
				i+=1
			self.list_DictKeys[j] = self.list_DictKeys[i]
		self.list_DictKeys[i] = flag
		self.qsort_stack.append( [ top, i-1 ] )
		self.qsort_stack.append( [ i+1, end ] )
	def qsort(self):
		self.list_DictKeys = self.keylist
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
		return self.list_DictKeys

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
	str_FileName = 'Markov_HASH.txt'
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
		str_SavePath = str_SavePath_Father + str(index_Ascii)+'_'+chr(index_Ascii)+'/'
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

		fp1_K_A = open(str_Fname1_Key_A,'w')
		fp2_K_B = open(str_Fname2_Key_B,'w')
		fp3_K_AB = open(str_Fname3_Key_AB,'w')
		fp4_K_AB_Freq = open(str_Fname4_Key_Freq,'w')
		fp5_K_AND_Freq = open(str_Fname5_Key_AND_Freq,'w')

		fp6_NW = open(str_Fname6_NextWord,'w')
		fp7_NW_Freq = open(str_Fname7_NextWord_Freq,'w')
		fp8_NW_AND_Freq = open(str_Fname8_NW_AND_Freq,'w')
		fp9_Whole = open(str_Fname9_Whole,'w')

		list_Key_Sorted = c_DictSorter(dict_KeyFreq_thisAcii).qsort() 
		for str_Key in list_Key_Sorted:
			list_AB = c_MarkovTool().f_cut_glue(str_Key)
			fp1_K_A.write(list_AB[0]+'\n')
			fp2_K_B.write(list_AB[1]+'\n')
			fp3_K_AB.write(str_Key+'\n')
			int_AB_Freq = dict_KeyFreq_thisAcii[str_Key]
			fp4_K_AB_Freq.write(str(int_AB_Freq)+'\n')
			fp5_K_AND_Freq.write(str_Key+'\t'+str(int_AB_Freq)+'\n')
			fp9_Whole.write(str_Key+'|'+str(int_AB_Freq)+'|')
			dict_NextWord = dict_AsciiHash_DICT[str_Key]
			list_NextWord_sorted = c_DictSorter(dict_NextWord).insertsort()

			for tail in list_NextWord_sorted:
				fp6_NW.write(tail+'\t')
				int_tail_Freq = dict_NextWord[tail]
				fp7_NW_Freq.write(str(int_tail_Freq)+'\t')
				fp8_NW_AND_Freq.write(tail+'\t'+str(int_tail_Freq)+'\t')
				fp9_Whole.write(tail+'|'+str(int_tail_Freq)+"|")
			fp6_NW.write('\n')
			fp7_NW_Freq.write('\n')
			fp8_NW_AND_Freq.write('\n')
			fp9_Whole.write('\n')
		fp1_K_A.close()
		fp2_K_B.close()
		fp3_K_AB.close()
		fp4_K_AB_Freq.close()
		fp5_K_AND_Freq.close()
		fp6_NW.close()
		fp7_NW_Freq.close()
		fp8_NW_AND_Freq.close()
		fp9_Whole.close()


#dictst1 = {'a':12,'b':7,'c':55,'d':7,'e':23}
#print c_DictSorter(dictst1).qsort()

if __name__ == '__main__':
	str_FileName = 'The_Holy_Bible.txt'
	savefilename = 'The_Holy_Bible_tokenize.txt'
	#savefilename = f_FileTokenizer(str_FileName,savefilename)
	print 1
	c_Markov = c_MarkovCreater(savefilename)
	print 2
	list_AsciiHash = c_Markov.list_AsciiHash
	dict_KeyFreq = c_Markov.dict_KeyFreq
	print 3
	#f_AsciiHash_to_File(list_AsciiHash,dict_KeyFreq)
	print 4
	f_AsciiHash_to_File_Sorted_Splited(c_Markov)
	print 5