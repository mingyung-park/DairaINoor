# Reference : https://docs.python.org/3/tutorial/datastructures.html

# Methods of list

#1: append(x)
#   add an item to the end of the list.   
list=[]
list.append("x")
print(list)

#   Equivalent
a=[]
a[len(a):]=["x"]
print(a)