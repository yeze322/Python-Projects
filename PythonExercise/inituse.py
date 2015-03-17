class Person:
    def __init__(self,name,age,address):
        self.NAME=name
        self.AGE=age
        self.home=address
    def say(self):
        print "My name is{}, {} this year, live in {}"\
              .format(self.NAME,self.AGE,self.home)

p=Person('yeze','20','beijng xueyuam')
p.say()
