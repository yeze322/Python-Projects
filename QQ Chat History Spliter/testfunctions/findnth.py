def findnth(line,word,n):
#    if n == 1:
#       return line.find(word)
    if n<=1:
        return -1
    #don't want used when n <= 1
    index = -1
    thrownum = -1
    for i in range(n):
        index = line.find(word)
        if index == -1:
            return index
        thrownum += index+1
        line = line[index+1:]
    return thrownum

line = "hello world ! "
print len(line)
print findnth(line," ",0)
print findnth(line," ",1)
print findnth(line," ",2)
print findnth(line," ",3)
print findnth(line," ",4)
