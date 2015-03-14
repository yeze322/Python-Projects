class getdate:
    def __init__(self):
        self.line = line
        self.sp1 = line.find(' ')
        self.sp2 = findnth(line,' ',2)
    def date():
        return line[0:sp1]
    def time():
        return line[sp1+1:sp2]
    def word():
        return line[sp2+1:]

class tst:
    def __init__(self,line):
        self.word=line
        
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
line = "2011 10:23 gekko"
#cls = getdate(line)
x = Complex(30,12)
print x.r,x.i

y= tst(line)
print y.word
