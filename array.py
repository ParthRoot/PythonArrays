import array as arr

a=arr.array('i' , [2,4,5])
print(a[2])
for x in a:
    print(x)
print("---------------------------------------")
b = arr.array('i',[1,2,3,4,5,6])
print(a[-2])
print(*b)
print(b[2:5])
print(a[1:5])
print(b[1])

for x in b:
    print(x,end=" ")


