import numpy as np
import random

from numpy.core.fromnumeric import cumsum

def generator(arr):
    for i  in range(np.size(arr,0)):
        for j in range(np.size(arr,1)):
            arr[i,j] = random.randint(0,99)


def printMat(arr):
    for i in range(np.size(arr,0)):
        for j in range(np.size(arr,1)):
            print("%3d" % arr[i,j], end= " ")
        print()


def firstDigonal(arr):
    for i in range(np.size(arr,0)):
        for j in random(np.size(arr,1)):
            if i == j:
                print("%3d" %arr[i,j],end=" ")
    print()



def secDiagnoal(arr):
    for i in range(np.size(arr,0)):
        for j in range(np.size(arr,1)):
            if(i+j)==(np.size(arr,1)-1):
                print("%3d" % arr[i,j], end=" ")
    print()


def sumofRows(arr):
    print("Row    rowsum")
    for i in range(np.size(arr,0)):
        rsum =0 
        for j in range(np.size(arr,1)):
            rsum+=arr[i,j]
        print(i,"\t",rsum)
    print()


def sumofCols(arr):
    print("Col    colsum")
    for j in range(np.size(arr,1)):
        csum=0
        for i in range(np.size(arr,0)):
            csum+=arr[i,j]
        print(j,"\t",csum)
    print()
