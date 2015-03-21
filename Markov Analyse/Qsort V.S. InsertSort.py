from c_DictSorter import *
from Searcher import c_SentencePredictor
from random import randint
import linecache

lis = linecache.getlines("ImportList.txt")
filename = "LanguaeTextRepertory/" + lis[0].strip()
print filename
import c_MarkovTool
word = linecache.getlines(filename)
for i in range(50,80):
	liswd = c_MarkovTool.word_tokenizer(word[i])
	print liswd
if __name__ == "__1main__":
	Pdt = c_SentencePredictor()

	N = 115
	diction = {}
	for i in range(N):
		word_Rand = Pdt.f_RandAWord()
		diction[word_Rand] = randint(0,30)

	import cProfile
	import pstats


	pr = cProfile.Profile()
	pr.enable()

	for i in range(5000):
		c_DictSorter(diction).qsort()
		c_DictSorter(diction).insertsort()

	pr.disable()
	ps = pstats.Stats(pr).sort_stats("cumulative")
	ps.print_stats()
