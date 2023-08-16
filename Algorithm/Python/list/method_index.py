# Reference : https://docs.python.org/3/tutorial/datastructures.html

# Methods of list

#7: index(x[, start[, end]])
#   Return zero-based index of first item whoae value is equal to x.
#   If there is no such value, it raises a ValueError.
#   OPTIONAL: start index, end index
#   start index 지정해도 return index is computed relative to the beginning of the full list.
#   (ZERO-BASED)
list = ['a','b','a','d','a','b','c','d']
print(list.index('c'))
print(list.index('a',3))
print(list.index('a',-5))
#   >>print(list.index('a',-3))
#   >>ValueError: 'a' is not in list
print(list.index('a',1,3))

