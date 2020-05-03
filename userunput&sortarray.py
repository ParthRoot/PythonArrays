from array import *

def sort(snum, arr): #function search element in array
    for i in range(len(arr)):
        if snum == arr[i]:
            print("Found")
            break
        else:
            print("Not found")
            break


arr = array('i', []) # array
num = int(input("Enter the array len"))

for x in range(num): # user input in array
    a = int(input("Enter the array element"))
    arr.append(a)

print(arr)

snum = int(input("Enter the search number"))
sort(snum, arr) # call the function
