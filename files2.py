import pickle
import os

class student:
    def __init__(self,name,stno,ave):
        self.name=name
        self.stno=stno
        self.ave=ave
    
    def display(self):
        print("{0:10s} {1:5d} {2:8.2f}".format(self.name,self.stno,self.ave))


def menu():
    print("1- Enter a student")
    print("2- Search a student")
    print("3- Delete a student")
    print("4- Update the ave of student")
    print("5- Display all students")
    print("6- Exit ")
    choice= int(input("Enter your selection(1-6):"))
    return choice


def insertData():
    print("Enter name, stno, ave :",end="")
    name,stno,ave = input().split()
    ob=student(name,int(stno),float(ave))
    pickle.dump(ob,myfile)

def reportData():
    myfile.seek(0,0)
    ob=pickle.load(myfile)
    print("{0:10s} {1:10d} {2:10f}".format("name","stno","ave"))
    while True:
        ob.display()
        try:
            ob=pickle.load(myfile)
        except(EOFError) as err:
            break

def searchData():
    myfile.seek(0,0)
    stno=int(input("Enter a stno to search :"))
    found = False
    ob=pickle.load(myfile)
    while True:
        if ob.stno == stno:
            found = True
            break
        try:
            ob=pickle.load(myfile)
        except(EOFError) as err:
            break
        
        if found:
             print("{0:10s} {1:10d} {2:10f}".format("name","stno","ave"))
             ob.display()
        else:
            print("Student not found")


def updateData():
    outfile = open("stfile1.data","wb")
    print("Enter stno and ave to change ", end="")
    myfile.seek(0,0)
    ob=pickle.load(myfile)
    found = False
    while True:
    if ob.stno = int(stno):
        found =True
        ob.ave = float(ave)
        pickle.dump(ob,outfile)
        break
    else:
        pickle.dump(ob,outfile)
        try:
            ob=pickle.load(myfile)
        except(EOFError) as err :
            break
    
    if found :
        while True:
            try:
                ob=pickle.load(myfile)
                pickle.dump(ob,outfile)
            except(EOFError) as err :
                break
    myfile.close()
    outfile.close()
    os.remove("stfile.dat")
    os.rename("stfile.data","stfile1.dat")


