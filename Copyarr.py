import array as arr

vals = arr.array('i', [1, 2, 3, 4, 5])
newArr = arr.array(vals.typecode, (a for a in vals))

for x in newArr:
    print(x)

i=0
while i<len(newArr):
    print(newArr[i])
    i=i+1

vals.reverse()
print(vals)
