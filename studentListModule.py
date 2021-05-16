from studentList import studentList


def menu():
    print()
    print("1. Enter a student")
    print("2. Find best student")
    print("3. Delete a student")
    print("4. Search student")
    print("5. Report list")
    print("6. Exit")
    choice = int(input("\n Enter your select(1-6):"))
    return choice

def addtoList(stlist):
    name,stno,ave=input("Enter name,stno,ave:").split()
    st = studentList(name,int(stno),float(ave))
    stlist.append(st)


def findMax(stlist):
    mAve=stlist[0].getAve() #first ave
    p =0 # p is the position of max element
    for i in range(1,len(stlist)):
        if stlist[i].getAve() > mAve:
            mAve=stlist[i].getAve()
            p=i
    print("Student with max ave:")
    print("{0:10s} {1:10s} {2:10s}".format("Name","Stno","Ave"))
    stlist[p].display()

def searchStudent(stdlist):
    stno = int(input("Eneter stno to search:"))
    found = False
    i =0
    while i < len(stdlist) and not found:
        if stdlist[i].getStno() == stno:
            found = True
        else:
            i = i+1
    if not found:
        print("Student with ",stno ,"not exist")
    else:
        print("{0:10s} {1:10s} {2:10s}".format("Name","Stno","Ave"))
        stdlist[i].display()
    

def delStuden(stlist):
    stno = int(input("Eneter stno to search:"))
    found = False
    i =1
    while i < len(stdlist) and not found:
        if stdlist[i].getStno() == stno:
            found = True
        else:
            i = i+1
        if not found:
            print("Student with ",stno ,"not exist")
        else:
            stlist.pop(i)
            print("Student with",stno,"deleted")


def reportList(stlist):    
    print("{0:10s} {1:10s} {2:10s}".format("Name","Stno","Ave"))
    for i in range(len(stlist)):
        stlist[i].display()
    
    stlist=list()
    while True:
        c=menu()
        if c== 1:
            addtoList(stlist)
        elif c==2:
            findMax(stlist)
        elif c==3:
            delStuden(stlist)
        elif c==4:
            searchStudent(stlist)
        elif c==5:
            reportList(stlist)
        else:
            break

