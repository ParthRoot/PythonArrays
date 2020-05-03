from array import *

a = array('i',[])
n = int(input("Enter the length of array"))
for i in range(n):
    x = int(input("Enter the element"))
    a.append(x)
print(a)