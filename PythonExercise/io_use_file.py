fp = open ('output.txt','w')

while True:
    name = raw_input("enter a sentence: ")
    if name == "EOF" :
        break
    name = name + '\n'
    fp.write(name)
fp.close()
#now read

print "now read"
fread = open('output.txt')
while True :
    line = fread.readline()
    if len(line) == 0 :
        break
    line = line.replace(line[len(line)-1],"a")
    #replace the '\n' at the end
    print line

fread.close()
