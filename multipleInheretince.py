class a:
    def __init__(self):
        self.num1=10
    
    def show(self):
        print("Show() in class a : num1=",self.num1)
    

class b:
    def __init__(self):
        self.num2=20
    
    def show(self):
        print("show() in class b : num2=",self.num2)


class c(a,b):
    def __init__(self):
        a.__init__(self)
        b.__init__(self)
        self.num3=30
    
    def show(self):
        a.show()
        b.show()
        print("in class d: ")
        print("num1= ",self.num1 , "num2 = ",self.num2, "num3=",self.num3)
    

cObject = c()
c.show()