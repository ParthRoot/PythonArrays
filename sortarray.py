from array import *

arr = array('i', [1,2,3,5])
number=int(input("enter the search number"))
k = 0
for x in arr:
    if x == number:
        print(arr[k])
        break
    k += 1
print(arr.index(number))








