try:
    text = raw_input ("inoput something:")
except EOFError :
    print 'EOF'
except KeyboardInterrupt :
    print "keyboard interrupt"
else :
    print "text = {} ".format(text)

fp = open ("output.txt","w")

while True:
    try : 
        a = raw_input("input a:")
        fp.write(a+"\n")
    except EOFError :
        print "end of file"
        fp.close()
        break
    except KeyboardInterrupt:
        print "cancel"
        break
