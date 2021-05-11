import numpy as np
####################################################################Access array elements
def element_array():
    arr=np.arange(5)
    arr[3]=15
    print("Print selected numbers:")
    print("a[1]=",arr[1],"a[3]=",arr[3])
    print("Print array by for loop")
    for item in arr:
        print(item,end=" ")

    print("\n Print complete array: ")
    print(arr)

 







