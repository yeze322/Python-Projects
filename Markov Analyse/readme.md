# Use Markov Chain To Analyze And Predict Sentece#

# UPDATE 2015/03/22 #

I come out with the sort on tail words!

calculate the length of the tail_word_diction, if it's bigger than a number ( maybe 80 ~ 120 ), then use qsort; else, use insertsort!

I'm quite saitisfied with the improvement! it costs only 30% time now!

About choosing the number, I write a test program called 'Qsort VS Insertsort.py'

It shows that when N between 80~110, the result will be best!

Considering insertsort() is unstable, I choos the lower bound 80

This example teaches me: try to use different method to solve problem!

I will try merge sort later!

What's more, about the randint() function , I delete it, and the program runs faster...

Rand() is useless, because our dicion is not very sorted ( it's a dic, you can calculate the probability of after put all words the dic is sorted... compared with the set in C++ based on binary tree, this is almost impossible)

# UPDATA 2015/03/9 #

Noe I finish most of this model!

if you execute Searcher.py, you can get a long sentence created by Markov Chain!!

I'm not very saitisfied with the speed of creating a comlete Library!

The Searcher worls mainly through file operation. If needed, I may change the code, to save all the lib in memory!

What I do recent is: 
	
	1 - improve the qsort function. The first virson costs nearly 30 or more seconds to analyse 'The Bible'. Now it's less than 1s. I learn quite much when doing this job.

	2 - Improve the tokenizer. Origin tokenizer was based on ntlk library, but I find it so slow!
	So I write a simple, lighter one (It works perfect, the result is almost the same with that in nltk, only ['s] was splited different)

	3 - Change the way we import articles. In the former version, the program only support 1 file. I make some small changes, now you can stick the filename that you want to import into the file : 'ImportList.txt'! REMEMBER TO ADD '\n' and '.txt'!!!

I found it quite intersting when pridicting what will be printed next. There are many choices, in this version I only write 2 of them. It will be better!

WHAT"S MORE:

The prdictor works quite weird when we choose The Bible to create our language lib...

It's time to use my crawler to get some ordinary texts!


# OLD VERSION #
mainly consisted by:
	
	1 - word_tokenizer use nltk.word_tokenized() function, to count the frequence of one word's appearence

	2 - Marcov Chain Lib Creater

	I use A+B as the key (two words) , And those words are saved using Hash table ( split by ASCII ).

	I want to make it better use MySQL.

	In this version, add different file will be quite hard. 

# Still Proving... #