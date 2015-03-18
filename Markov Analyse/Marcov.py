import linecache
import nltk

def file_tokenize(filename,savefilename):
	word = linecache.getlines(filename)
	fw = open(savefilename,'w')
	for line in word:
		line = nltk.word_tokenize(line)
		for i in line:
			fw.write(i+'\n')
	fw.close()
	return savefilename

class glue:
	def __init__(self):
		self.GLUE = '_+_'
	def glue_word(self,word1,word2):
		return word1+self.GLUE+word2

	def cut_glue(self,word):
		index = word.find(self.GLUE)
		word1 = word[:index]
		word2 = word[index+len(self.GLUE):]
		return [word1,word2]

class marcov_create:
	def __init__(self,filename):
		words = linecache.getlines(filename)
		self.HASH = { }
		self.HASH_key_freq_dict = { }
		words.append('EOF')#'/n' as EOF
		for i in range(len(words)-2):
			key = glue().glue_word(words[i][:-1],words[i+1][:-1])
			next_word = words[i+2][:-1]
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
		self.qsort_list = [  ]
		self.qsort_stack = [  ]
	def quicksort(self,top,end):
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
		#self.quicksort(top,i-1)
		#self.quicksort(i+1,end)
	def qsort(self):
		self.qsort_list = self.keylist
		self.qsort_stack.append([0,len(self.keylist)-1])
		count = 0
		while ( self.qsort_stack != [ ] ):
			top_end = self.qsort_stack.pop()
			top = top_end[0]
			end = top_end[1]
			self.quicksort( top , end )
			count+=1
			if count%5000==0:
				print count
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

def HASH_Freq_Filter(HASH_key_freq_dict,threshould_val=5):
	del_list = [ ]
	for i in HASH_key_freq_dict:
		if HASH_key_freq_dict[i] <= threshould_val:
			del_list.append(i)
	for i in del_list:
		del(HASH_key_freq_dict[i])
	return HASH_key_freq_dict

def HASH_list_to_file_sort(HASH_list,HASH_key_freq_dict,threshould_val = 5):
	filename = 'Marcov_HASH.txt'
	HASH_key_freq_dict = HASH_Freq_Filter(HASH_key_freq_dict,threshould_val)
	#I must del it first
	sorted_key_list = dicsort(HASH_key_freq_dict).qsort()
	fw = open(filename,'w')
	for key in sorted_key_list:
		key_freq = HASH_key_freq_dict[key]
		if key_freq < threshould_val:
			continue
		fw.write(key+'|'+str(key_freq)+'|')
		for word in HASH_list[key]:
			fw.write(str(word)+'|')
		fw.write('\n')
	print len(HASH_key_freq_dict)
	fw.close()

#dictst1 = {'a':12,'b':7,'c':55,'d':7,'e':23}
#print dicsort(dictst1).qsort()

if __name__ == '__main__':
	filename = 'The_Holy_Bible.txt'
	savefilename = 'The_Holy_Bible_tokenize.txt'
	#savefilename = file_tokenize(filename,savefilename)
	print 1
	marcov = marcov_create(savefilename)
	HASH = marcov.HASH
	print 2
	HASH_key_freq_dict = marcov.HASH_key_freq_dict
	print 3
	HASH_list = HASH_to_HASH_list(HASH)
	print 4
	for i in range(100,150):
		print i,len(HASH_Freq_Filter(HASH_key_freq_dict,i))
	#HASH_list_to_file_sort(HASH_list,HASH_key_freq_dict,9)
