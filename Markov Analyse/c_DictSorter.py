class c_DictSorter:
	def __init__(self,diction):
		self.diction = diction
		self.list_DictKeys = diction.keys()
		self.qsort_stack = [  ]
	def unsorted(self):
		return self.list_DictKeys
	def __quicksort__(self,top,end):
		#dictst1 = {'e1':12,'e2':12,'e3':12,'a':12,'b':7,'asd':7,'c':55,'d':7,'e':23}
		if top > end:
			return
		index_rand = top #norandom random.randint(top,end)
		flag = self.list_DictKeys[index_rand] ;
		#norandom self.list_DictKeys[index_rand] = self.list_DictKeys[top]
		#norandom self.list_DictKeys[top] = flag
		i = top ; j = end
		write_top = top ; write_end = end
		list_Equal = []
		list_Equal.append(flag)

		while(i<j):
			while(i<j):
				if self.diction[self.list_DictKeys[j]] < self.diction[flag]:
					self.list_DictKeys[write_end] = self.list_DictKeys[j]
					j -= 1
					write_end-=1
				elif self.diction[self.list_DictKeys[j]] == self.diction[flag]:
					list_Equal.append(self.list_DictKeys[j])
					j-=1
				else:
					break
			self.list_DictKeys[write_top] = self.list_DictKeys[j]
			self.list_DictKeys[i] = self.list_DictKeys[j]

			while(i<j):
				if self.diction[self.list_DictKeys[i]]>self.diction[flag]:
					self.list_DictKeys[write_top] = self.list_DictKeys[i]
					i+=1
					write_top += 1	
				elif self.diction[self.list_DictKeys[i]] == self.diction[flag]:
					list_Equal.append(self.list_DictKeys[i])
					i += 1
				else:
					break
			self.list_DictKeys[write_end] = self.list_DictKeys[i]
			self.list_DictKeys[j] =  self.list_DictKeys[i]

		len_list_Equal = len(list_Equal)
		for index_Equal in range(len_list_Equal):
			self.list_DictKeys[index_Equal + write_top] = list_Equal[index_Equal]
		self.qsort_stack.append( [ top, write_top-1 ] )
		self.qsort_stack.append( [ write_end+1, end ] )

	def qsort(self):
		self.qsort_stack.append([0,len(self.list_DictKeys)-1])
		while ( self.qsort_stack != [ ] ):
			top_end = self.qsort_stack.pop()
			top = top_end[0]
			end = top_end[1]
			self.__quicksort__( top , end )
		return self.list_DictKeys

	def insertsort(self):
		if self.list_DictKeys == []:
			return []
		newlist = [self.list_DictKeys[0]]
		for i in self.list_DictKeys[1:] :
			judge = 0
			for flag in newlist:
				if self.diction[i] > self.diction[flag]:
					newlist.insert(newlist.index(flag),i)
					judge = 1
					break
			if judge == 0:
				newlist.append(i)			
		return newlist
	def __merge__(self,top,end):
		pass
	def mergesort(self):
		if self.list_DictKeys == []:
			return []
		newlist = self.list_DictKeys
	def bubblesort(self):
		if self.list_DictKeys == []:
			return []
		for i in range(len(self.list_DictKeys)-1,-1,-1):
			for j in range(0,i):
				if self.diction[self.list_DictKeys[j]] < self.diction[self.list_DictKeys[j+1]]:
					temp = self.list_DictKeys[j]
					self.list_DictKeys[j] = self.list_DictKeys[j+1]
					self.list_DictKeys[j+1] = temp
		return self.list_DictKeys
