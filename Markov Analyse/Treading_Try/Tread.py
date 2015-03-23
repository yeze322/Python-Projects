from threading import *
from thread import *
from random import randint
from time import sleep

def f_Productor(datapool):
	for i in range(400):
		data = randint(0,999);
		print data,
		datapool.append(data)
def f_Consumer(dp):
	sleep(0.2)
	while dp != []:
		data = dp.pop()
		index = data%10;
		list_Dict[index].append(data);

def f_Deliver(datapool,dp):
	data = datapool.pop()
	dp[data%2].append(data)

def f_CountDiciEle(list_Dict):
	total = 0
	for i in list_Dict:
		total += len(i)
	return total

list_Dict = [ [ ] for i in range(10) ]
datapool = [ ]
dp = [ [ ] , [ ] ]
t1 = Thread(target = f_Consumer, name = None, args = (dp[0],))
t2 = Thread(target = f_Consumer, name = None, args = (dp[1],))

producor = Thread(target = f_Productor,name = None, args = (datapool,))
deliver = Thread(target = f_Deliver,name = None,args = (datapool,dp,) )

producor.run()
deliver.run()
t1.run()
t2.run()
	





print '\n',f_CountDiciEle(list_Dict)