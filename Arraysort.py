import numpy as np

##################################################################bubble sorting 

def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

temp= np.array([' ']*5, dtype='object')
for i in range(len(temp)):
    temp[i]=input("Enter a word")


##################################################################Sort array elements
def arra_sort():
    a = np.array([0] * 5 , int)
    for i in range(len(a)):
        a[i] = int(input("Enter a number:"))
    print("Befor Sorting")
    print(a)
    a.sort(axis=0,kind="quicksort",order=None)
    print("After Sorting")
    print(a)
