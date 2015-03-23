from linecache import getlines


class HuffmanCoding:
	def __init__(self,fname_Read):
		self.article = getlines(fname_Read)
		self.dict_AciiChar = {}
		self.list_SortedChar = []
		self.FreqList = []
		self.totalword = 0
		self.dict_HuffmanCoding = {}
	def Create(self):
		self.FileToHash()
		self.dicsort_insert()
		self.GetFreqList()
	def FileToHash(self):
		frequence = [0 for i in range(255)]
		for line in self.article:
			self.totalword += len(line)
			for char in line:
				frequence[ord(char)]+=1
		for i in range(255):
			if frequence[i] == 0:
				continue
			self.dict_AciiChar[i] = frequence[i]

	def dicsort_insert(self):
		if self.dict_AciiChar == {}:
			return []
		self.list_SortedChar = []
		for key in self.dict_AciiChar:
			if self.list_SortedChar == []:
				self.list_SortedChar.append(key)
				continue
			length = len(self.list_SortedChar)
			for i in range(length):
				if self.dict_AciiChar[key] > self.dict_AciiChar[self.list_SortedChar[i]]:
					self.list_SortedChar.insert(i,key)
					break
			if length == len(self.list_SortedChar):
				self.list_SortedChar.append(key)

	def HuffmanCodingCreate(self):
		basic = ''
		for i in self.list_SortedChar:
			self.dict_HuffmanCoding[i]= basic+'1'
			#print basic
			basic = basic+'0'
	# def LempelZiv
	def huff2(self,listpart,base):
		print listpart,base
		if len(listpart) == 0:
			return
		if len(listpart) == 1:
			self.dict_HuffmanCoding[listpart[0]] = base
			return
		'''
		if len(listpart) == 2:
			self.dict_HuffmanCoding[listpart[0]] = base+'0'
			self.dict_HuffmanCoding[listpart[1]] = base+'1'
			return 
		'''

		total = 0
		for i in listpart:
			total+=self.dict_AciiChar[i]
		bound = total/2
		print total,bound
		addfreq= 0
		stopword = 0
		for i in listpart:
			addfreq += self.dict_AciiChar[i]
			print addfreq,
			if addfreq >= bound:
				stopword = i
				break
		index = listpart.index(stopword)
		l1 = listpart[0:index+1]
		base1 = base+'0'
		l2 = listpart[index+1:]
		base2 = base + '1'
		raw_input(index)
		self.huff2(l1,base1)
		self.huff2(l2,base2)


	def GetFreqList(self):
		for i in self.list_SortedChar:
			self.FreqList.append(self.dict_AciiChar[i])
	def wirtecode(self,fname_Write):
		#self.HuffmanCodingCreate()
		self.huff2(self.list_SortedChar,"")

		fp_write = open(fname_Write,"w")
		diction = self.dict_HuffmanCoding
		float_Averlen = 0.0
		for i in range(len(self.list_SortedChar)):
			word = self.list_SortedChar[i]
			freq = self.FreqList[i]
			probability = (freq*1.0)/(self.totalword*1.0)
			coding = diction[word]
			fp_write.write("%-5d%-10d%10.8f%50s\n"%(word,freq,probability,coding))
			float_Averlen += probability*len(coding)
		fp_write.write("\n%d\t\t%f"%(self.totalword,float_Averlen))
		fp_write.close()

filename = '99.txt'

h1 = HuffmanCoding(filename)
h1.Create()
print h1.list_SortedChar
print h1.FreqList
h1.wirtecode('huffman.txt')