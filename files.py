def inputstudent_file():
    f=open("test.dat","w")
    while True:
        st = input("Enter a student name:")
        if st == "":
            break
        f.write(st+"\n")

    f.close()
    f=open("test.dat","r")
    s=f.read()
    while s !="":
        print(s)
        s=f.read()
    f.close()

#########################

def read_file():
    f=open("test1.data","w")
    while True:
        st = input("Enter a course title:")
        if st == "":
            break
        f.write(st+"\n")
    f.close()
    f=open("test1.data","r")
    print("Contents of file using readline()")
    s=f.readline()
    while s!= "":
        print(s,end="")
        s=f.readline()
    f.close()
    print("contents of file using in opreator:")
    f=open("test1.data","r")
    for s in f:
        print(s,end="")

