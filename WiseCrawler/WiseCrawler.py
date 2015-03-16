import CrawLib

website1 = 'http://www.xbiquge.com/'
website2 = 'http://www.csdn.net/'
website3 = 'http://www.kekenet.com/'

chooseset = ''

rule1 = [['html','read'],[]]
rule2 = [['broadcast','CNN'],[]]
ruleset = [rule1,rule2]
filedict = CrawLib.Greper(website3,ruleset)

start = 1

if start :
	for i in filedict:
		down = CrawLib.ListDownload(i,filedict.get(i))
		down.start()