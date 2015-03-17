import linecache
import nltk

def lines_to_list(article):
	retlist = []
	for line in article:
		linetoken = nltk.word_tokenize(line)
		retlist += linetoken
	return retlist

GLUE = '_+_'
def glue_word(word1,word2):
	return word1+GLUE+word2

def cut_glue(word):
	index = word.find(GLUE)
	word1 = word[:index]
	word2 = word[index+len(GLUE):]
	return [word1,word2]

class marcov_create:
	def __init__(self,words):
		self.HASH = { }
		self.HASH_key_freq_dict = { }
		words.append('EOF')#'/n' as EOF
		for i in range(len(words)-2):
			key = glue_word(words[i],words[i+1])
			next_word = words[i+2]
			if key not in self.HASH:
				self.HASH_key_freq_dict[key] = 1
				self.HASH[key] = { next_word : 1 }
			else:
				if next_word in self.HASH[key]:
					self.HASH[key][next_word]+=1
				else:
					self.HASH[key][next_word]=1
				self.HASH_key_freq_dict[key]+=1

class dicsort:
	def __init__(self,diction):
		self.diction = diction
		self.keylist = diction.keys()
	def dicqsort(self,top,end):
		pass
	def quicksort(self,ls,tail):
		if tail<0:
			return []
		if tail ==0 :
			return ls
		flag = ls[0]
		i = 0 ; j = tail
		while(i<j):
			while(i<j and ls[j]>=flag):
				j-=1
			ls[i] = ls[j]
			while(i<j and ls[i]<=flag):
				i+=1
			ls[j] = ls[i]
		ls[i] = flag
		ret_left = self.quicksort(ls[0:i],i-1)
		ret_right = self.quicksort(ls[i:],tail-i)
		return ret_left+[flag]+ret_right
	def qsort(self):
		return self.quicksort(self.keylist,len(self.keylist)-1)
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

def HASH_to_HASH_list(HASH):
	for key in HASH:
		sortlist = []
		dic = HASH[key]
		newlist = dicsort(dic).insertsort()
		for word in newlist:
			sortlist.append(word)
			sortlist.append(dic[word])
		HASH[key] = sortlist
	return HASH

def HASH_list_to_file(HASH_list,HASH_key_freq_dict,threshould_val = 5):
	filename = 'Marcov_HASH.txt'
	fw = open(filename,'w')
	for key in HASH_list:
		key_freq = HASH_key_freq_dict[key]
		if key_freq < threshould_val:
			continue
		fw.write(key+'|')
		fw.write(str(key_freq)+'|')
		for word in HASH_list[key]:
			fw.write(str(word)+'|')
		fw.write('\n')
	fw.close()

def HASH_list_to_file_sort(HASH_list,HASH_key_freq_dict,threshould_val = 5):
	filename = 'Marcov_HASH.txt'
	sorted_key_list = dicsort(HASH_key_freq_dict).insertsort()
	print 'sort finish!',
	fw = open(filename,'w')
	for key in sorted_key_list:
		key_freq = HASH_key_freq_dict[key]
		if key_freq < threshould_val:
			continue
		fw.write(key+'|'+str(key_freq)+'|')
		for word in HASH_list[key]:
			fw.write(str(word)+'|')
		fw.write('\n')
	fw.close()

dictst1 = {'a':12,'b':7,'c':55,'d':7,'e':23}
dictst2 = {}

sort1 = dicsort(dictst1).qsort()
sort2 = dicsort(dictst2).qsort()

if __name__ == '__yeze__':
	filename = 'The_Holy_Bible.txt'
	article = linecache.getlines(filename)
	print 1,
	words = lines_to_list(article) #this is slowest
	print 2,
	HASH = marcov_create(words).HASH
	print 3,
	HASH_key_freq_dict = marcov_create(words).HASH_key_freq_dict
	print 4,
	HASH_list = HASH_to_HASH_list(HASH)
	print 5,
	HASH_list_to_file(HASH_list,HASH_key_freq_dict)
	print 6