from linecache import getlines
from c_MarkovTool import word_tokenizer
SRCPATH = 'LanguageTextRepertory/'

def f_Articles_Tokenizer(list_FileName):
	list_ArticleList = getlines(list_FileName)
	for FileName in list_ArticleList:
		FileName = SRCPATH+FileName.strip()
		fw = open(FileName+'_tokenized.txt','w')
		article = getlines(FileName)
		for line in article:
			linetoken = word_tokenizer(line)
			if linetoken == []:
				continue
			for word in linetoken:
				word = word.lower()
				fw.write(word+'\n')
		fw.close()

def f_MySQLSourceCreater(list_FileName):
	list_ArticleList = getlines(list_FileName)
	fw = open(SRCPATH+'MySQL_Import.txt','w')
	for FileName in list_ArticleList:
		FileName = SRCPATH+FileName.strip() 
		article = getlines(FileName+'_tokenized.txt')
		len_Article = len(article)
		article.append('\n')
		article.append('\n')
		word1 = article[0][0:-1]
		word2 = article[1][0:-1]
		for i in range(2,len_Article):
			word3 = article[i][0:-1]
			fw.write(word1+'\t'+word2+'\t'+word3+'\n')
			word1 = word2
			word2 = word3

	fw.close()

str_ListName = 'ImportList.txt'
import cProfile
import pstats
pf = cProfile.Profile()
pf.enable()
f_Articles_Tokenizer(str_ListName)
f_MySQLSourceCreater(str_ListName)
pf.disable()
ps = pstats.Stats(pf).sort_stats("cumulative")
ps.print_stats()