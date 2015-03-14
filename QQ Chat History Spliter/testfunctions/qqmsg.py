# -*- coding: utf-8 -*-
import linecache

srcfile = "./王道(7th)交流群.txt"
word = linecache.getlines(srcfile)
filename = "./王道(7th)交流群-noblankline.txt"
after = open(filename,"w")
for i in word:
    if i in "\n\b":
        continue
    after.write(i)
after.close()

bit = raw_input()

def findpair(word) :
    a = word.find('(')
    b = word.find(')')
    if (a==-1 or b==-1):
        x = word.find(".com>")
        return -1
    qq = word[a+1:b]
    return qq

def judgeqq(word) :
    if len(word) < 12:
        print len(word)
        return 1
    return 0

nameset = []
qqset = []
msgset = []
former = ""
#word=linecache.getline(filename,1)
word=linecache.getlines(filename)
for i in word:
    ret = findpair(i)
    if (ret!=-1):
        if ((not ret.isdigit())or(len(ret)<7)):#if qq
            continue
        former = ret
        if ret not in qqset:#new people
            qqset.append(ret)
            i = i[i.find(' ')+1:]
            i = i[i.find(' ')+1:]
            name = i[0:i.find('(')]
            if name is -1:
                continue
            nameset.append(name)
    else:
        msgset.append(i)

            
for i in range(0,len(qqset)):
    print qqset[i],
    print "--",nameset[i]
    print "===="
print len(msgset)
