# -*- coding: utf-8 -*-
#重用性做的不好。可把函数改为：以关键字划分，取出第一段、第n段的模式！
def findnth(line,word,n):
    if n == 1:
        return line.find(word)
    index = -1
    thrownum = -1
    for i in range(n):
        index = line.find(word)
        if index == -1:
            return index
        thrownum += index+1
        line = line[index+1:]
    return thrownum
#failkey: special word to be an return value, because members' name can be something like -1
failkey = "ThIsMuStBeUnIqUe!)_"
#======#
import linecache
srcname = u"./王道(7th)交流群"
filename = srcname+"-noblank-nohead.txt"
srcname = srcname + ".txt"
#read file into word
word=linecache.getlines(srcname)
fpwrite = open(filename,"w")

#remove all the blank line, save it

for i in range(7,len(word)):#in your qq history have some head
    if word[i] in '\n\b':
        continue
    fpwrite.write(word[i])
fpwrite.close()

#update your 'word'
word=linecache.getlines(filename)

#create a nameset
nameset = []


def pickoutnamefromline(line):
    date = line[0:line.find(" ")]
    name = failkey
    if (len(date)==10)and("-"in date)and("20"in date):#example:2014-05-23
        name = line[line.find(" ")+1:]
        name = name[name.find(" ")+1:len(name)-1]
    return name

#identify username, save to nameset[]
for i in range(0,len(word)):
    name = pickoutnamefromline(word[i])
    if name != failkey:
        if name not in nameset:
            nameset.append(name)

#msgset: save one user's msg
msgset = []

#give a name, find its index
def indexfornamebox(line):
    retval = failkey
    name = pickoutnamefromline(line)
    if name == failkey:
        return retval
    for i in range(0,len(nameset)):
        if name == nameset[i]:
            return i
    return retval

#create a namelist to list people
for name in nameset:
    msgset.append([])

#screen show:
a = len(nameset)
print "size--nameset: ",a
temp = raw_input("pause")

#former: used to record former speaker
formeruser = 0
formerdate = ""

fop = open("Pure_Msg.txt","w")
#now write into the msgset box
for i in word:
    position = indexfornamebox(i)
    if position != failkey:
        formeruser = position
        continue
    else:
        msgset[formeruser].append(i)
        fop.write(str(formeruser)+":"+i)
fop.close()        

#write the list for people
fwrite = open("./msgrecord/namelist.txt","w")
fwrite.write("total members:\n"+str(len(nameset))+'\n')
for i in range(len(nameset)):
    fwrite.write(str(i)+" -- "+nameset[i]+" -- "+str(len(msgset[i]))+'\n')
fwrite.close()

#function: replace special signal to _, and encode it
braceset = ['<','>','!','/','"',':','?','\\','|']
def withoutspecialchar(name):
    for char in name:
        if char in braceset:
            index = name.find(char)
            name = name[0:index]+'_'+name[index+1:]
    return name

#write msg box into different files
for index in range(0,len(nameset)):
    temp = nameset[index].decode('utf-8')
    temp = withoutspecialchar(temp)
    filename = "./msgrecord/"+temp+".txt"
    fwrite = open(filename,'w')
    fwrite.write(nameset[index]+"total: "+str(len(msgset[index]))+"==========\n\n")
    for i in msgset[index]:
        fwrite.write(i)
    fwrite.close()
