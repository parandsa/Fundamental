def enter(lst):
    while True :
        x=int(input("Enter a number, 0 to end : "))
        if x !=0 :
            lst.append(x)
        else:
            break

def negFunc(lst):
    print("\n Negatives are :")
    neg = 0 
    for item in lst:
        if item < 0 :
            print(item, " ", end = " ")
            neg +=1
    print("\n Number of negatives is :", neg)

def posFunc(lst):
    pos = 0 
    print("\n Positives are :")
    for item in lst:
        if item>0:
            print(item, " ", end= " ")
            pos +=1
    print("\n Number of positives is :",pos)


def find(lst):
    x=int(input("Enter a number to search :"))
    if x in lst:
        print(x, "is is list")
    else:
        print(x,"is not in list")


def getTemp(temp):
    for i in range(len(temp)):
        temp[i]=[int(x) for x in input("Enter five values:")].split()
    

def display(temp):
    print("Countents of list:")
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            print("{0:4d}".format(temp[i][j]), end = " ")
        print()


def findMean(temp):
    days= ["wed","Thur","Friday"]
    print("{0:7s} {1:7s}".format("Days", "Averages"))
    for i in range(len(temp)):
        daySum=0
        for j in range(len(temp[0])):
            daySum += temp[i][j]
        print("{0:7s} {1:8.2f}".format(days[i],daySum/len(temp[0])))