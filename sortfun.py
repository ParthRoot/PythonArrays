from array import *
# Search function with parameter list name
# and the value to be searched
def search(list ,n):

    for i in range(len(list)):
        if list[i] == n:
            print("found")
            break


# list which contains both string and numbers.
list = array('i', [1, 2, 4, 6])

# Driver Code
n = 4

search(list, n)
 #   print("Found")
#else:
 #   print("Not Found")
