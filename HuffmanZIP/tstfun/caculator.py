expression = "-1+32-5\n"
def level1(explist):
	result = 0
	operator = 1
	temp = 0
	for i in explist:
		if i not in '+-\n':
			temp = float(i)
		else:
			result += temp*operator
			temp = 0
			if i == '\n':
				break
			if i == '-':
				operator = -1
			elif i == '+':
				operator = 1
	return result

explist = "5/3/4/6\n"

def level2(explist):
	result = 1
	temp = 0
	operator = '*'
	for i in explist:
		if i not in '*/\n':
			temp = float(i)
		else:
			if operator == '*':
				result = result*temp
			elif operator == '/':
				result = result/temp
			temp = 0
			operator = i
			if i == '\n':
				break
	return result

def exp_to_list(expression):
	explist = []
	former = ""
	for i in expression:
		if i in '+-/*()\n':
			if former != "":
				explist.append(former)
				former = ""
			explist.append(i)
			continue
		else:
			former+=i
	return explist

def calculevel2(explist):
	while True:
		for i in range(len(explist)):
			if explist[i] in '*/':
				newlist = explist[i-1:i+2]
				newlist.append('\n')
				result = level2(newlist)
				del(explist[i-1:i+2])
				explist.insert(i-1,str(result))
				break
			if explist[i] == '\n':
				result = calculevel1(explist)
				return result


def calculevel1(explist):
	return level1(explist)

from sys import exit
def rfindlist(ll,char):
	for i in range(len(ll)-1,-1,-1):
		if ll[i] == char:
			return i 
	return -1
def calculevel3(explist):
	result = 0
	while True:
		try:
			index1 = explist.index('(')
		except:
			index1 = -1
		try:
			index2 = rfindlist(explist,')')
		except:
			index2 = -1


		if index1 == -1 or index2 == -1:
			if index1 == -1 and index2 == -1:
				print "break because no brace"
				break
			else:
				print 'error!'
				exit(1)
		newlist = explist[index1+1:index2]
		newlist.append('\n')
		print newlist
		result = calculevel3(newlist)
		del(explist[index1:index2+1])
		explist.insert(index1,str(result))

	return calculevel2(explist)

if __name__ == '__main__':

	expression = "-(1+2432*(3-6)+5)*7\n"
	explist = exp_to_list(expression)
	print calculevel3(explist)