class person:
    def __init__(self,name="",idnumber=0):
        self.name = name
        self.idnumber =idnumber
    
    def display(self):
        print("{0:10s} {1:10s}".format("name","id"))
        print("{0:10s} {1:<5d}".format(self.name,self.idnumber))


class student(person):
    def __init__(self,name,idnumber,stno,ave):
        person.__init__(self,name,idnumber)
        self.stno = stno
        self.ave = ave
    
    def isExcelent(self):
        return self.ave >= 17
    
    def display(self):
        print("student information:")
        super().display()
        print("{0:10s} {1:10s}".format("stno","average"))
        print("{0:<5d} {1:9.2f}".format(self.name,self.idnumber))


class employee(person):
    def __init__(self,name,idnumber,salary):
        super().__init__(name,idnumber)
        self.salary= salary
    
    def netpay(self):
        tax = self.salary * 5 /100
        insurance = self.salary *7/100
        net = self.salary - (tax+insurance)
        return net,tax,insurance
    
    def diplay(self):
        print("Employee information:")
        super().display()
        net,tax,insurance=self.netpay()
        print("{0:10s} {1:10s} {2:10s}".format("tax","insurance","net pay"))
        print("{0:10.2f} {1:10.2f} {2:10.2f}".format(tax,insurance,net))