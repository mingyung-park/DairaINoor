# Reference : https://docs.python.org/3/tutorial/datastructures.html

# Methods of list

#11: copy()
# Return a shallow copy of the list.
list = [2,3,4,5,1,2]
copy = list.copy()
print(copy)

# Equivalent to a[:]
copy = list[:]
print(copy)

copy = list[1:3]
print(copy)