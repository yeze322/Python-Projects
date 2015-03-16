import urllib
import urllib2

url = 'http://www.csdn.net/article/2015-03-16/2824247'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
req = urllib2.Request(url)

try:
	response = urllib2.urlopen(req)
except urllib2.HTTPError,e:
	print 1
except urllib2.URLError, e:
	print 1
else:
	print response.info()
