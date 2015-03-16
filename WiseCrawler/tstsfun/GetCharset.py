import urllib2

website = 'http://www.kekenet.com/'
req = urllib2.Request(website)
html = urllib2.urlopen(req)
word = html.read()

index = word.find('charset=')+len('charset=')
code = word[index:index+3]
if code == 'utf':
	code = 'utf-8'
fw = open('tst.html','w')
fw.write('\xEF\xBB\xBF')
fw.write(word.decode(code).encode('utf-8'))
fw.close()
print code