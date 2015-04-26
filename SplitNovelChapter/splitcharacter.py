# -*- coding: utf-8 -*-
import linecache
import os
origin = linecache.getline("./list.txt",1)
print origin
mark1 = u"第"
mark2 = u"章"

'''fw  = open(filename,'w')
for i in word:
        i = i.decode('utf-8','ignore')
        fw.write(i)
fw.close()'''
specialset = ['|','*','?','<','>',':']
def delspecial(word):
        retval = word
        for i in word:
                if i in specialset:
                        index = retval.find(i)
                        retval = retval[0:index]+'_'+retval[index+1:]
        return retval
class sparcle:
	def __init__(self,srcname):
		self.word = linecache.getlines(srcname)
		self.mark1 = mark1
		self.mark2 = mark2
		self.srcname = "./_"+srcname+"/"+srcname
		self.srcpath = "./_"+srcname+'/'
		self.set = {}
	#judge if line is the split point, if True return head key;or return -1
	def match(self,line):
		sp1 = line.find(self.mark1)
		sp2 = line.find(self.mark2)
		if sp1==-1 or sp2 == -1:
			return -1
		return line[0:sp1]
	#bat(): create a diction of [headkey : appear times]
	def bat(self):
		for i in self.word:
			head = self.match(i)
			if head == -1:
				continue
			if head in self.set :
				self.set[head]+=1
				continue
			self.set[head] = 1
		return self.set
	#most(): find the keyword that match our split word
	def most(self):
		self.bat()
		more = 0
		record = ""
		fw = open(self.srcpath+"_Headkeys.txt",'w')
		fw.write("times  |  key \n")
		for i in self.set:
			fw.write(str(self.set[i])+'|['+i+']\n')
			if self.set[i]>more:
				more = self.set[i]
				record = i
		fw.close()
		return record
	#get():create A default txtfile to save the split result
	def get(self):
		filename = self.srcpath + '_Catalog.txt'
		fw = open(filename,'w')
		fw.write("chapter"+'|'+"chapter name"+'|'+'lines'+'\n')
		no = 1
		piece = open(self.srcpath+'chapter - 0.txt','w')
		sp = self.most()
		for i in range(len(self.word)):
			line = self.word[i]
			head = self.match(line)
			if head == -1:
				piece.write(line)
				continue
			if head == sp:
				line = line[line.find(self.mark1):-1]
				fw.write(str(no)+'|'+line+'|'+str(i)+'\n')
				piece.close()
				#print line
				piece = open(self.srcpath+'chapter - '+str(no)+'.txt','w')
				#it appear special symbol!
				piece.write(line)
				no+=1
		piece.close()
		fw.close()
		
novelname = origin[0:-1]
if not os.path.exists("./_"+novelname+'/'):
        os.mkdir('_'+novelname)
sparcle(novelname).get()
