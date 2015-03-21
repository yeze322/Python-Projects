from MarkovLibCreater_Multi import c_DictSorter
from Searcher import c_SentencePredictor
from random import randint

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
