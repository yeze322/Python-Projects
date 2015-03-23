import linecache
import nltk
import os
import random
from c_MarkovTool import *
from c_DictSorter import *

class c_MarkovCreater:
	SRCPATH = 'LanguaeTextRepertory/'

	def __init__(self,str_ListFileName):
		lines_Filename = linecache.getlines(str_ListFileName)
		for i in lines_Filename:
			print i
		self.list_AsciiHash = [ { } for i in range(256) ] #this dicion costs 3.5s, I decide to use a two stage HASH
		#self.dict_KeyFreq = { } #useless	#self.dict_KeyFreq[str_Key] = 1 #useless	#self.dict_KeyFreq[str_Key] += 1#useless		
		self.list_KeyFreq_Dict_asciihash =  [ { }  for i in range (256) ] #this diction costs 1.2s

		for FileName in lines_Filename:
			FileName = self.SRCPATH + FileName[:-1]+'_tokenized.txt'
			lines_Word = linecache.getlines(FileName)
			lines_Word.append('EOF')# EOF
			D_Ascii = { } #this will save time about 0.1s
			D_Freq = { } #avoid create&destroy a pointer in for loop 
			for index_Word in range(len(lines_Word)-2):
				index_AsciiHash = ord(lines_Word[index_Word][0])  #this one costs 1.4 s
				str_Key = lines_Word[index_Word][0:-1] + str_const_GLUE + lines_Word[index_Word+1][0:-1] #costs 1.4s
				#str_Key = f_glue_word(lines_Word[index_Word][:-1],lines_Word[index_Word+1][:-1]) #costs  2.5s
				str_NextWord = lines_Word[index_Word+2][:-1] #costs 0.5s
				D_Ascii = self.list_AsciiHash[index_AsciiHash] #datatype -- dict_AciiHash_Dict
				D_Freq = self.list_KeyFreq_Dict_asciihash[index_AsciiHash] #costs 0.5s

				if str_Key not in D_Ascii: #put "not in" in front of "in",save 0.4s, because in will cause extra judge
					D_Ascii[str_Key] = { str_NextWord : 1 }#costs 1.4s
					D_Freq[str_Key] = 1#555
					
				else:
					if str_NextWord in D_Ascii[str_Key]:#666
						D_Ascii[str_Key][str_NextWord]+=1#666
					else:#666
						D_Ascii[str_Key][str_NextWord]=1#666
					D_Freq[str_Key] += 1#555

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
			list_AB = f_cut_glue(str_Key)
			fp1_K_A.write(list_AB[0]+'\n')#yezetst
			fp2_K_B.write(list_AB[1]+'\n')#yezetst
			fp3_K_AB.write(str_Key+'\n')#yezetst
			int_AB_Freq = dict_KeyFreq_thisAcii[str_Key]
			fp4_K_AB_Freq.write(str(int_AB_Freq)+'\n')#yezetst
			fp5_K_AND_Freq.write(str_Key+'\t'+str(int_AB_Freq)+'\n')#yezetst
			fp9_Whole.write(str_Key+'|'+str(int_AB_Freq)+'|')#yezetst
			dict_NextWord = dict_AsciiHash_DICT[str_Key]
			

			if len(dict_NextWord) < 80:
				list_NextWord_sorted = c_DictSorter(dict_NextWord).insertsort()
			else:
				list_NextWord_sorted = c_DictSorter(dict_NextWord).qsort()

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

	c_Markov = c_MarkovCreater(str_ListFileName)
	pr = cProfile.Profile() #123
	pr.enable() #123
	f_AsciiHash_to_File_Sorted_Splited(c_Markov)
	pr.disable() #123
	ps = pstats.Stats(pr).sort_stats("cumulative") #123
	ps.print_stats() #123
	print 3