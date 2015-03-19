import random
qsort_stack = []
def __quicksort_random__(a,top,end):
	#dictst1 = {'e1':12,'e2':12,'e3':12,'a':12,'b':7,'asd':7,'c':55,'d':7,'e':23}
	if top > end:
		return
	flag = a[top]
	i = top ; j = end
	write_top = top ; write_end = end
	list_Equal = [ ]
	list_Equal.append(flag)

	while(i<j):
		while(i<j):
			if a[j] < flag:
				a[write_end] = a[j]
				j -= 1
				write_end-=1
			elif a[j] == flag:
				list_Equal.append(a[j])
				j-=1
			else:
				break
		a[write_top] = a[j]
		a[i] = a[j]
		while(i<j):
			if a[i]>flag:
				a[write_top] = a[i]
				i+=1
				write_top += 1	
			elif a[i] == flag:
				list_Equal.append(a[i])
				i += 1
			else:
				break
		a[write_end] = a[i]
		a[j] =  a[i]

	len_list_Equal = len(list_Equal)
	for index_Equal in range(len_list_Equal):
		a[index_Equal + write_top] = list_Equal[index_Equal]
	qsort_stack.append( [ top, write_top-1 ] )
	qsort_stack.append( [ write_end+1, end ] )

def qsort(a):
	qsort_stack.append([0,len(a)-1])
	while qsort_stack != [ ] :
		top_end = qsort_stack.pop()
		top = top_end[0]
		end = top_end[1]
		__quicksort_random__(a,top , end )
	return a

filename = 'A+B_Freq.txt'
output = 'output.txt'
from linecache import getlines
lis = getlines(filename)
a = []
for i in lis:
	num = int(i.strip())
	a.append(num)

qsort(a)

fw = open(output,'w')
ifright = True
former = a[0]
for i in a :
	if i>a[0]:
		ifright = False
	fw.write(str(i)+'\n') 

print ifright




