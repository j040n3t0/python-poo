class X(object):
    def __init__(self, count):
        self.count = count
        self.y = Y(self) #create a y passing in the current instance of x
    def add2(self):
        self.count += 2

class Y(object):
    def __init__(self,parent):
        self.parent = parent #set the parent attribute to a reference to the X which has it
    def modify(self):
        self.parent.add2()

x = X(5)
x.y.modify()
print(x.count)

x = X(2)
x.y.modify()
print(x.count)