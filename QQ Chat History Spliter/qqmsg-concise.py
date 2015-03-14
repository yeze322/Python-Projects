# -*- coding: utf-8 -*-
#重用性做的不好。可把函数改为：以关键字划分，取出第一段、第n段的模式！
def findnth(line,word,n):
    if n <=1:
        return -1
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
whichTXT = linecache.getlines("WhichTXT.txt")
import os
if not os.path.exists("./msgrecord"):
    os.mkdir("./msgrecord")
#=======
src = whichTXT[0][0:-1]
filename = src+"-noblank-nohead.txt"
srcname = src + ".txt"
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
    name = failkey
    sp1 = line.find(' ')
    sp2 = findnth(line,' ',2)
    #sp3 = findnth(line,' ',3)
    if sp1==-1 or sp2==-1:# or sp3!=-1
        return failkey
    date = line[0:sp1]
    time = line[sp1+1:sp2]
    #judge rule
    judge = (len(date)==len("2014-03-03")) #and (len(time)==len("21:29:36"));
    judge = judge and ('-' in date) and (':' in time)
    if judge==0:
        return failkey
    return line[sp2+1:-1]

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
#temp = raw_input("pause")

#former: used to record former speaker
formeruser = 0
formerdate = ""
formertime = ""
ifwritedate = True#每个人每天第一次说话要写#不错这个蛋疼的了。直接写进去
onedayspeak = 0

fop = open("Pure_Msg.txt","w")
#now write into the msgset box
for i in word:
    position = indexfornamebox(i)
    if position != failkey:
        formeruser = position
        date = i[0:i.find(' ')]
        formerdate = date
        formertime = i[i.find(' '):findnth(i,' ',2)]
        continue
    else:
        msgset[formeruser].append(formerdate+formertime+' '+i)
        fop.write('['+formerdate+formertime+']'+": "+i)
fop.close()        

#write the list for people
src = srcname.decode('utf-8','ignore')
if not os.path.exists("./msgrecord/"+src):
    os.mkdir("./msgrecord/"+src)
fwrite = open("./msgrecord/"+src+"-namelist.txt","w")
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

class getdate:
    def __init__(self,line):
        self.sp1 = line.find(' ')
        self.sp2 = findnth(line,' ',2)
        self.date = line[0:self.sp1]
        self.time = line[self.sp1+1:self.sp2]
        self.word = line[self.sp2+1:]

#write msg box into different files
for index in range(0,len(nameset)):
    temp = nameset[index].decode('utf-8')
    temp = withoutspecialchar(temp)
    filename = "./msgrecord/"+src+'/'+temp+".txt"
    fwrite = open(filename,'w')
    fwrite.write(nameset[index]+"\nTOTAL lines: "+str(len(msgset[index]))+"\n==========\n\n")
    date = ""
    time = ""
    onedayspeak = 0
    totalspeak = 0
    date_speak = {}
    #应该把他们做成一个类在！！！！！！！！！！！！
    
    for i in msgset[index]:
        tmpclass = getdate(i)
        if date!=tmpclass.date:#bug sloved. naming convention
            if date!="":
                fwrite.write('\noneday speak: '+str(onedayspeak)+'\n==========')
                date_speak[date] = onedayspeak
                onedayspeak=0
            date = tmpclass.date
            fwrite.write('\n'+date+'\n\n')
        
        if time!=tmpclass.time:
            time = tmpclass.time
            fwrite.write('['+time+'] '+tmpclass.word)
            onedayspeak+=1
            totalspeak+=1
        else:
            fwrite.write('           '+tmpclass.word)
    date_speak[date] = onedayspeak
    fwrite.write("\noneday speak: "+str(onedayspeak)+'\n==========')
    fwrite.write("\n\nSTATICS:\n"+"   totoal speaks -- "+str(totalspeak)+"\n")
    fwrite.write("  [speaks every day]\n")
    for dic in date_speak:
        fwrite.write('  ['+dic+'] '+str(date_speak[dic])+'\n')
    fwrite.close()
