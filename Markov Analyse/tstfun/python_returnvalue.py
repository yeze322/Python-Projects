def list_ret_refer(lis):
	for i in lis:
		lis[lis.index(i)] = -1
	return lis

lis  = [1,2,3,4,5]
ret = list_ret_refer(lis)
print lis
print ret

def list_ret_copy2(lis):
	copy = lis[:]
	for i in copy:
		copy[copy.index(i)] = -1
	return copy
lis  = [1,2,3,4,5]
ret = list_ret_copy2(lis)
print lis
print ret

def list_ret_copy1(lis):
	copy = lis
	for i in copy:
		copy[copy.index(i)] = -1
	return copy

lis  = [1,2,3,4,5]
ret = list_ret_copy2(lis)
print lis
print ret