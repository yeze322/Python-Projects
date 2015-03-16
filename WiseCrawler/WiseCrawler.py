import CrawLib

website1 = 'http://www.xbiquge.com/'
website2 = 'http://www.csdn.net/'
website3 = 'http://www.kekenet.com/'

chooseset = 'kekenet'
if chooseset == 'kekenet':
	keke = CrawLib.downloadURL(website3)
	keke_finishfile = keke.save()
	keke_grep = CrawLib.grepurl(keke_finishfile)
	keke_grep_default = keke_grep.grep()

if chooseset == 'csdn':
	csdn = CrawLib.downloadURL(website3)
	csdn_finishfile = csdn.save()
	csdn_grep = CrawLib.grepurl(csdn_finishfile)
	csdn_grep_article = csdn_grep.grep('href="','" ','+article',['article'])
	csdn_grep_topic = csdn_grep.grep('href="','" ','+topic',['topic'])
	print csdn.downloadpath
	print csdn_grep_article

ifstart = False

if ifstart :
	csdn_article_down = CrawLib.ListDownload(csdn_grep_article,csdn.downloadpath)
	csdn_article_down.start()
'''childurlset = getlines(grepfile)
for i in childurlset:
	i=i[:-1]#remove \n
	downloadURL(i,tst.downloadpath).get()
'''
#grepurl('./hello/'+)