import numpy as np

##################################################################Search in Array
def search_array():
    grades = np.zeroes(5)
    for i in range(len(grades)):
        grades[i]=int(input("Enter a grade"))
    print("Array is:")
    print(grades)
    min=np.amin(grades,0)
    max=np.amax(grades,0)
    print("Max = ",max, "Min =",min)
    item = 20
    x=np.where(grades==item)
    if len(x[0]):
        print("Number ", item,"found at ", x[0])
    else:
        print("Number  ",item,"Not found")



 
##################################################################Binary in Array
def search_bubble(arr):
    for i in range(len(arr) -1, 0 , -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def seqSearch(arr,item):
    for i in range(len(arr)):
        if arr[i]==item:
            return i
    return -1


def binSearch(arr, item):
    low =0 
    high = len(arr)
    while low <= high:
        mid = (low + high) //2
        if arr[mid]==item:
            return mid
        elif item > arr[mid]:
            return mid
        else:
            high = mid -1
    return -1