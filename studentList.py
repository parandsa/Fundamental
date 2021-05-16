class studentList:
    def __init__(self, name=" ", stno=0, ave=0.0):
        self.name=name
        self.__stno=stno
        self.__ave=ave
    
    def getAve(self):
        return self.__ave
    
    def getStno(self):
        return self.__stno
    
    def display(self):
        print("{0:10s} {1:4d} {2:8.2f}".format(self.name,self.__stno,self.__ave))
    


        