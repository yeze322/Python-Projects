class c_DictSorter:
	def __init__(self,diction):
		self.diction = diction
		self.list_DictKeys = diction.keys()
		self.qsort_stack = [  ]

	def __quicksort_random__(self,top,end):
		#dictst1 = {'e1':12,'e2':12,'e3':12,'a':12,'b':7,'asd':7,'c':55,'d':7,'e':23}
		if top > end:
			return
		index_rand = random.randint(top,end)
		index_rand = top
		flag = self.list_DictKeys[index_rand]
		self.list_DictKeys[index_rand] = self.list_DictKeys[top]
		self.list_DictKeys[top] = flag
		i = top ; j = end
		write_top = top ; write_end = end
		list_Equal = [ ]
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
		print self.list_DictKeys
		self.qsort_stack.append([0,len(self.list_DictKeys)-1])
		while ( self.qsort_stack != [ ] ):
			top_end = self.qsort_stack.pop()
			top = top_end[0]
			end = top_end[1]
			self.__quicksort_random__( top , end )
		return self.list_DictKeys

filename_in = 'A+B_Freq.txt'
filename_out = 'output.txt'

import linecache
import random
article = linecache.getlines(filename_in)
fp_w = open(filename_out,'w')

diction = {}
count = 1
for line in article:
	num = int(line[:-1])
	diction[str(count)+'('+str(num)+')'] = num
	count+=1

newlist = c_DictSorter(diction).qsort()

for i in newlist:
	fp_w.write(str(diction[i])+'\n')
fp_w.close()