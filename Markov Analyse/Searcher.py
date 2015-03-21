import MarkovLibCreater_Multi
from linecache import  getlines,getline

str_LibPath_Markov = "./Markov_AsciiHash/"
str_WordLIst_Path = './WordList/'

def f_GetAsciiStr(word):
	num = ord(word[0])
	return str(num)

def f_WordSearch_Single(word,bool_IfNeedFreq = False):
	str_ListName = f_GetAsciiStr(word)
	lines_WordList = getlines(str_WordLIst_Path+str_ListName + '.txt')
	try:
		index_WordInList = lines_WordList.index(word+'\n')
	except:
		return False
	if bool_IfNeedFreq:
		line_WordFreq = getline(str_WordLIst_Path + str_ListName + '_Freq.txt',index_WordInList+1)
		return int(line_WordFreq.strip())
	else:
		return True
from MarkovLibCreater_Multi import c_MarkovTool

def f_MarkovNextWord(word1,word2):
	str_WordKey = c_MarkovTool().f_glue_word(word1,word2)
	str_MarkovLibDir = f_GetAsciiStr(str_WordKey)
	str_SearchPath = str_LibPath_Markov + str_MarkovLibDir + '/'

	lines_Keys_AplusB = getlines(str_SearchPath+'A+B.txt')
	try:
		index_WordKey = lines_Keys_AplusB.index(str_WordKey+'\n')
	except:
		return [ ]
	line_TailsMixFreq = getline(str_SearchPath + 'NextWord.txt',index_WordKey+1)
	list_TailWords = c_MarkovTool().word_tokenizer(line_TailsMixFreq)

	return list_TailWords

def f_WordCorrector(word):
	if f_WordSearch_Single(word):
		return word
	else:#unfinished
		print word+"is auto correct to"+'[word2]'
		return word

def f_SingleWordPredictor(word1):
	word1 = f_WordCorrector(word1)
	str_MarkovLibDir = f_GetAsciiStr(word1)
	str_SearchPath = str_LibPath_Markov + str_MarkovLibDir + '/'

	lines_Keys_A = getlines(str_SearchPath+'A.txt')
	try:
		index_WordKey = lines_Keys_A.index(word1+'\n')	
	except:
		print 'predict FAIL!'
		return False
	line_B = getline(str_SearchPath + 'B.txt',index_WordKey+1)
	if line_B == "" :
		return False
	return line_B.strip()

from random import randint


class c_SentencePredictor:
	def __init__(self):
		self.str_LibPath_Markov = "./Markov_AsciiHash/"
		self.str_WordLIst_Path = './WordList/'
	def f_WordPreTreat(self,list_WordList):
		size = len(list_WordList)
		if size == 0:
			print "NO INPUT!"
			return
		if size > 2:
			print "TOO MORE WORDS!"
			return
		word1 = f_WordCorrector(list_WordList[0])
		if size == 1:		
			word2 = f_SingleWordPredictor(word1)
		else:
			word2 = f_WordCorrector(list_WordList[1])
		return [word1,word2]
	def f_SentencePredictor(self,list_WordList,int_MaxLenth = 20):
		list_WordList = self.f_WordPreTreat(list_WordList)
		word1 = list_WordList[0]
		word2 = list_WordList[1]
		print word1,
		list_AlreadyGot = [word1]
		while(int_MaxLenth):
			print word2,
			list_AlreadyGot.append(word2)
			list_TailWords = f_MarkovNextWord(word1,word2)
			if list_TailWords == []:
				return
			int_IndexAdjust = 0
			while True:
				try:
					str_NextWord = list_TailWords[int_IndexAdjust]
				except:
					index_RandWord = randint(0,len(list_TailWords)-1)
					str_NextWord = list_TailWords[index_RandWord]
					break
				if str_NextWord not in list_AlreadyGot:
					break
				int_IndexAdjust += 1
			word1 = word2
			word2 = str_NextWord
			int_MaxLenth -= 1
	def f_SentencePredictor_Rand(self,list_WordList,int_MaxLenth = 20):
		list_WordList = self.f_WordPreTreat(list_WordList)
		word1 = list_WordList[0]
		word2 = list_WordList[1]

		print word1,
		list_AlreadyGot = [word1]
		while(int_MaxLenth):
			print word2,
			list_AlreadyGot.append(word2)
			list_TailWords = f_MarkovNextWord(word1,word2)
			if list_TailWords == []:
				return
			int_IndexAdjust = randint(0,len(list_TailWords)-1)
			while True:
				try:
					str_NextWord = list_TailWords[int_IndexAdjust]
				except:
					index_RandWord = randint(0,len(list_TailWords)-1)
					str_NextWord = list_TailWords[index_RandWord]
					break
				if str_NextWord not in list_AlreadyGot:
					break
				int_IndexAdjust += 1
			word1 = word2
			word2 = str_NextWord
			int_MaxLenth -= 1
	
	def f_RandALine(self,lines):
		num = len(lines)
		return lines[randint(0,num-1)]

	def f_RandAWord(self):
		num = randint(97,122)
		path_1 = self.str_LibPath_Markov # "./Markov_AsciiHash/"
		path_2 = self.str_WordLIst_Path # './WordList/'
		lines_WordList = getlines(path_2 + str(num) + '.txt')
		int_RandWordLine = self.f_RandALine(lines_WordList)
		return int_RandWordLine[:-1]

if __name__ == "__main__":
	Pdt = c_SentencePredictor()
	word_Rand = Pdt.f_RandAWord()

	Pdt.f_SentencePredictor_Rand([word_Rand],1000)
