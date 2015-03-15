import urllib2
import os
#from multiprocessing import Process
# 0 - urlopen
class crawler:
	def __init__(self,url):
		self.url = url
	def request(self):
		self.request = urllib2.urlopen(self.url)
		self.word = self.request.read().decode('gbk').encode('utf-8')
		return self.word
	def request_uncode(self):
		self.request = urllib2.urlopen(self.url)
		self.word = self.request.read()
		return self.word

website = 'http://www.xbiquge.com/'
book = '0_36'

word = crawler(website+book+'/').request()
print 0

# 3 - create folder
if not os.path.exists(book):
	os.mkdir(book)
book_path = './'+book+'/'
print 1

# 2 - save root page --> save as 'bookfile'
book_file = book+'.txt'
book_page = open(book_path+book_file,'w')
book_page.write(word)
book_page.close()
print 2

# 3 - get the file after split, saved in bool_path dir
import splitcharacter
splitcharacter.sparcle(book_path+book_file,'<dd>','href=').get()
splitcharacter.sparcle(book_path+book_file,book,'.html').get()
result_catafile = book_path+book_file+splitcharacter.CATALOG
result_headile = book_path+book_file+splitcharacter.HEADKEYS
print 3
#print result_headile
#print result_catafile

# 4 - now getout the useful urls
splitcharacter.sparcle(result_catafile,'">','</a></dd>').get()
result_head2 = result_catafile+splitcharacter.HEADKEYS
print 4

# 5 - put htmls in vector
import linecache
urltail = linecache.getlines(result_head2)
urltailset = []
for i in urltail:
	sp1 = i.find('/')
	sp2 = i.find('|')
	i = i[sp1+1:sp2]
	if i not in urltailset:
		urltailset.append(i)
print 5
# 6 - now we get complete urls, just download them
#urltailset = urltailset.sort()

class savechapter:
	def __init__(self,website,book,tailset,savepath):
		if not os.path.exists(savepath):
			os.mkdir(savepath)
		self.website = website
		self.tailset = tailset
		self.savepath = savepath
		self.bookname = book

	def download(self,i):
		print i,
		word = crawler(self.website+self.bookname+'/'+i).request_uncode()#.decode('utf-8').encode('gbk')
		fr = open(self.savepath+i,'w')
		fr.write(word)
		fr.close()
		sucfile = open(self.bookname+"/success.txt",'a+')
		sucfile.write(i+'\n')
		sucfile.close()
		print '[finish]'#,writenow+finishnum,'/',totoalnum

	def save(self):
		word = ""
		#sucset = linecache.getlines(self.bookname+"/success.txt")
		#totoalnum = len(self.tailset)
		#finishnum = len(sucset)
		#writenow = 0
		for i in self.tailset:
			if os.path.exists(self.savepath+i):
				print i,'[skip]'
				#sucfile = open(self.bookname+"/success.txt",'a+')
				#sucfile.write(i+'\n')
				#sucfile.close()
				continue
			#pid = os.fork()
			#if pid == 0:
			else:
				self.download(i)
#print website,urltailset
urltailset.sort()
savechapter(website,book,urltailset,book_path+'download_chapter/').save()