from urllib2 import urlopen, Request,HTTPError,URLError
from urllib import urlencode
from time import sleep
import os

class EDcode:
	def __init__(self,word,code1='utf-8',code2='utf-8'):
		self.ec = code1
		self.dc = code2
		self.word = word
	def get(self):
		if self.ec != self.dc:
			try:
				word = self.word.decode(self.ec,'ignore').encode(self.dc)
			except:
				print 'in EDcode, ',self.ec,'to ',self.dc,'failed!'
			else:
				self.word = word
		return self.word
class toolFunction:
	braceset = ['?','/','\\','*','|',':','<','>','"']
	replace = '_'
	def __init__(self):
		pass
	def delspecial(self,word):
		for i in word:
			if i in self.braceset:
				word = word.replace(i,self.replace)
		return word

class downloadURL:
	arglist = ['website','savepath','filename','downloadpath']
	data = urlencode({'name':'jimmy3222'})
	headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)'}
	#headers = {}
	def __init__(self,website,savepath='get/'):
		self.website = website
		if not os.path.exists(savepath):
			os.mkdir(savepath)
			fp = open(savepath+'finish_list.txt','w');
			fp.close()
		if '.html' in website:
			suffix = ''
		else:
			suffix = '.html'
		self.savepath = savepath
		if website[-1] == '/':
			website = website[0:-1]
		website = website[website.rfind('/')+1:]
		website = toolFunction().delspecial(website)
		self.downloadpath = savepath + website + '/'
		#if not os.path.exists(self.downloadpath):
			#os.mkdir(self.downloadpath)
		self.filename = website+suffix
		print 'will download ',self.website,'as ',self.filename,'to ',self.savepath

	def save(self,code1='utf-8',code2='utf-8'):
		req = Request(self.website)#,self.data,self.headers)
		ffinish = getlines(self.savepath+'finish_list.txt')
		if self.website+'\n' in ffinish:
			print '[skip] ',self.website
			return self.savepath+self.filename
		try:
			html = urlopen(req)
		except HTTPError,e:
			print '[failed HTTPError]',e.code,self.website
			return False
		except URLError,e:
			print '[failed URLError] ',self.website
			return False
		else:
			word = html.read()
			fp = open(self.savepath+self.filename,'w')
			word = EDcode(word,code1,code2).get()
			fp.write('\xEF\xBB\xBF')#make it utf-8?
			fp.write(word)
			fp.close()
			print '[finish] ',self.website
			fp = open(self.savepath+'finish_list.txt','a+')
			fp.write(self.website+'\n')
			fp.close()
			return self.savepath+self.filename
			#return the complete filepath+name we download


from linecache import getlines
class grepurl:
	arglist = ['addsuffix','srcfile']
	def __init__(self,srcfile,suffix='-grep.txt'):
		print 'will grep file:',srcfile,'[add suffix: ',suffix,']'
		self.addsuffix = suffix
		self.srcfile = srcfile

	def __grepline__(self,line,keyhead,keytail,withinwordset,filterwordset):
		index1 = line.find(keyhead)
		if index1 == -1:
			return ""
		newhead1 = index1 + len(keyhead)
		line = line[newhead1:]
		index2 = line.find(keytail)
		if index2 == -1:
			return ""
		#cut [keyhead-keytail] finish, start pro grep
		line = line[0:index2]
		for no in filterwordset:
			if no in line:
				return ""
		for yes in withinwordset:
			if yes not in line:
				return ""
		return line

	def grep(self,keyhead = 'href="',keytail='"',addmiddle='',withinwordset=[],filterwordset=[]):
		grepfile = self.srcfile+addmiddle+self.addsuffix
		self.fp = open(grepfile,'w')
		word = getlines(self.srcfile)
		#urlset = []
		for i in word:
			i = self.__grepline__(i,keyhead,keytail,withinwordset,filterwordset)
			if i != '':
				#urlset.append(i)
				i+='\n'
			self.fp.write(i)
		self.fp.close()
		print '[grep finish] saved in ',grepfile
		return grepfile

class ListDownload:
	arglist_input = {'__init__':['listfile'],'start':['code1(utf-8)','code2(utf-8)']}
	arglist_retval = {}
	arglist_self = ['urlset','num_totoal','num_success','num_failed']
	def __init__(self,listfile,downloadpath):
		self.listfile = listfile
		self.downloadpath = downloadpath
		self.urlset = getlines(listfile)
		self.num_totoal = len(self.urlset)
	def start(self,code1='utf-8',code2='utf-8'):
		giveupset = []
		attemptset = {}
		while True:
			for i in self.urlset:
				i=i[:-1]#remove '\n'
				judge = downloadURL(i,self.downloadpath).save(code1,code2)
				if judge == False:
					if i in attemptset:
						attemptset[i]+=1
						if attemptset[i]>=3:
							giveupset.append(i)
					else:
						attemptset[i]=1

			lines = getlines(self.downloadpath+'finish_list.txt')
			num_finished = len(lines)
			if num_finished + len(giveupset)>=self.num_totoal:
				print '[Finish] URL IN ',self.listfile,'DOWNLOAD TO ',self.downloadpath,
				print '. TOTAL = ',self.num_totoal
				giveupfp = open(self.downloadpath+'giveup_list.txt','w')
				for url in giveupset:
					giveupfp.write(url+'\n')
				giveupfp.close()
				return
			else:
				print '[New Round] ',num_finished,'+ ',len(giveupset),'/ ',self.num_totoal,'Start after 3 seconds... ',
				sleep(1);print '1,',
				sleep(1);print '2,',
				sleep(1);print '3'