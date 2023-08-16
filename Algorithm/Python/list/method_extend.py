# Reference : https://docs.python.org/3/tutorial/datastructures.html

# Methods of list

#2: extend(iterable)
#   Add all the items from the iterable.
list=[0]
list.extend([1,2,3,4,5])
print(list)

#   Equivalent
list=[0]
iterable=[1,2,3,4,5]
list[len(list):]=iterable
print(list)

#   iterable 이므로 tuple 가능. tuple: 수정 불가능, list: 수정 가능
list=[0]
tuple=(1,2,3,4,5)
list.extend(tuple)
print(list)

#   Equivalent
list=[0]
tuple=(1,2,3,4,5)
list[len(list):]=tuple
print(list)