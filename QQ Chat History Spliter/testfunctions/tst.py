#failkey: special word to be an return value, because members' name can be something like -1
failkey = "ThIsMuStBeUnIqUe!)_"
#this is the function changed
def splitbykey(line,sepa,num):
    if num<=0:
        return failkey
    index = line.find(sepa)
    if index == -1:
        return failkey
    retval = line[0:index]
    line = line[index+1:]
    for i in range(1,num):
        index = line.find(sepa)
        retval = line[0:index]
        line = line[index+1:]
    return retval

line1 = "hello world his"
print splitbykey(line1,' ',1)
print splitbykey(line1,' ',2)
print splitbykey(line1,' ',3)
print splitbykey(line1,' ',4)
print splitbykey(line1,' ',5)
print splitbykey(line1,' ',0)


#conclusion: def a function that find the nth position is better
