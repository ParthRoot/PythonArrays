import array as arr

a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
b = arr.array('i', [1, 2, 3])

# change the first element
a[0] = 0
print(a)

# changing 3rd to 6th
a[3:6] = arr.array('i', [55, 22, 33])
print(a)

# add element
a.append(10)
print(a)

# add list
a.extend([52, 45, 56])
print(a)

# delete element
del a[2]
print(a)

print(a.pop(2))

# remove the element
a.remove(8)
print(a)

c = [1,2,3,4]
d = arr.array('i', c)
print(d)

print(*a)

# char
e = arr.array('u', ['a', 'b', 'c'])
print(e)

# concat two array

h = arr.array('i')
h = a + b
print(h)





