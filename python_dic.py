def dicInsert(dic):
    state,center,=input("Enter state,center:").split()
    dic[state]=center

def dicSearch(dic):
    state=input("Eneter state to search:")
    if state in dic:
        print("{0:10s} {1:10s}".format("state","center"))
        print("{0:10s} {1:10s}".format(state,dic[state]))
    else:
        print("State",state,"not found")

def dicDisplay(dic):
    print("{0:10s} {1:10s}".format("state","center"))
    print("-"*20)
    for state in dic:
        print("{0:10s} {1:10s}".format(state,dic[state]))


def dicUpdate(dic):
    state,center,=input("Enter state,center:").split()
    d={state:center}
    dic.update(d)

def dicDelete(dic):
    state=input("Enter state to delete:")
    if state in dic:
        del dic[state]
        print("state",state,"delete")
    else:
        print("state",state,"not found")
    