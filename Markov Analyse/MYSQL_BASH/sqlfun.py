import mysql.connector
import sys
from mysql.connector import errorcode
try:
	mkv = mysql.connector.connect(user = 'root',password = '9503212',db = 'Markov')
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print 1;
		sys.exit(1)
	else:
		print 2;

cur = mkv.cursor(buffered=True)
#cur.execute("select * from word where word1 = 'hello' ;")
cur.execute("select word2 from word where word1 = 'continue' ;")
print cur.fetchone()
cur.close()
mkv.close()