def reverse(txt):
    return txt[::-1]

def onlyalpha (txt) :
    x=""
    lent=0;
    for char in txt:
        lent+=1
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    for i in range(0,lent):
        #print "i = %d, len = %d"%(i,lent)
        if txt[i] in alpha:
            x+=txt[i]
    print x
    return x
#still not knowing how index in python works
           
def is_palindrome(txt):
    txt = onlyalpha(txt)
    txt = txt.lower()
    return txt == reverse(txt)
        
something = raw_input("enter string:")
onlyalpha(something)

print is_palindrome(something)
