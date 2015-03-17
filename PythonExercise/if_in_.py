dic = "hello world"
txt = raw_input("print a str:")
def ifin(txt):
    if txt in dic:
        print dic.replace(dic[1],"abs")
        print "yes"
    else:
        print "no"

ifin(txt)
print dic
